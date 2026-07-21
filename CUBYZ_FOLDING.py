"""CUBYZ_FOLDING_TUI.py -- Textual-based client rewrite.

Mirrors all the crunching/submission/benchmark logic from CUBYZ_FOLDING.py exactly,
but replaces its raw-terminal UI (print_terminal_status / DualStatusBoard / pause-menu
input() calls) with a Textual App that has:

  Left sidebar  – control buttons (same actions as the old pause-menu, always visible)
  Top bar       – campaign mode badge + volunteer name + global progress + ETA
  Lanes panel   – one box per active lane (GPU / CPU / P1 / P2 ...)
  Terminal log  – scrolling install/startup output + a text-input for prompts

All crunching runs in background threads exactly as before; the TUI is a separate
asyncio event-loop in the main thread (run_sync mode).  Thread->TUI communication
uses a thread-safe deque for log lines and a simple shared dict for lane states;
the TUI polls both every 0.5 s with set_interval.

Run:
    python3 CUBYZ_FOLDING_TUI.py

Requires textual and rich:
    pip install textual rich
"""

from __future__ import annotations

import os
import re
import sys
import ssl
import atexit
import json
import glob
import time
import platform
import subprocess
import shutil
import urllib.request
import urllib.error
import urllib.parse
import threading
import queue
import builtins
from collections import deque

# -- Textual / Rich Auto-installation ------------------------------------------
try:
    from rich.text import Text
    from textual.app import App, ComposeResult
    from textual.containers import Vertical, Horizontal
    from textual.widgets import Static, RichLog, Button, Input, Label
except ImportError:
    print("[~] Textual and Rich libraries not found. Auto-installing now...")
    for cmd in [
        [sys.executable, "-m", "pip", "install", "textual", "rich"],
        [sys.executable, "-m", "pip", "install", "--user", "textual", "rich"],
        [sys.executable, "-m", "pip", "install", "--break-system-packages", "textual", "rich"],
        [sys.executable, "-m", "pip", "install", "--user", "--break-system-packages", "textual", "rich"],
    ]:
        try:
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                break
        except Exception:
            pass
    try:
        from rich.text import Text
        from textual.app import App, ComposeResult
        from textual.containers import Vertical, Horizontal
        from textual.widgets import Static, RichLog, Button, Input, Label
        print("[OK] TUI dependencies (textual, rich) installed successfully!")
    except ImportError as e:
        print(f"[X] Auto-install of textual/rich failed: {e}")
        print("Please manually run: pip install textual rich")
        sys.exit(1)

# -- Platform detection --------------------------------------------------------
if sys.platform.startswith("linux"):
    PLATFORM = "linux"
elif sys.platform == "darwin":
    PLATFORM = "darwin"
elif sys.platform.startswith("win32"):
    PLATFORM = "win32"
else:
    print(f"[X] Unsupported operating system: {sys.platform}")
    sys.exit(1)

if PLATFORM == "win32":
    os.system('color')

# Always enable color codes -- Textual's RichLog interprets them via Text.from_ansi
class Colors:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    GRAY    = "\033[90m"
    WHITE   = "\033[97m"

MODE_COLORS = {
    "rag":      Colors.CYAN,
    "finetune": Colors.MAGENTA,
    "audit":    Colors.BLUE,
    "idle":     Colors.GRAY,
}
MODE_LABELS = {
    "rag":      "RAG",
    "finetune": "FINETUNE",
    "audit":    "AUDIT",
    "idle":     "IDLE",
}

def mode_color(mode: str) -> str:
    return MODE_COLORS.get(mode, Colors.BLUE)

# -- Server / client constants -------------------------------------------------
SERVER_URL       = "http://ashframe.net:7000"
OLLAMA_URL       = "http://localhost:11434/api/generate"
CONFIG_FILE      = os.path.expanduser("~/.cubyz_node_config.json")
DIAGNOSTICS_FILE = os.path.expanduser("~/.cubyz_node_diagnostics.jsonl")
VERSION          = "1.3.7"

print_lock = threading.Lock()

# -- Shared TUI state (written by background threads, read by TUI) -------------
# Lane state: { lane_tag: {"label": str, "task": str, "status": str, "speed": str} }
_lane_state: dict = {}
_lane_order: list = []
_lane_lock  = threading.Lock()

# Global progress (from last /get_work response)
_global_progress = {"comp": 0, "tot": 0, "eta": None, "mode": "idle"}
_progress_lock = threading.Lock()

# Log deque -- background threads push lines here; TUI drains it every poll
_log_queue: deque = deque(maxlen=2000)

# Input queue -- TUI pushes user input here; background threads block on it
_input_queue: queue.Queue = queue.Queue()

# Current volunteer info (set from main thread, read by TUI)
_volunteer_id: str = ""
_dual_controller_ref     = None
_parallel_controller_ref = None
_has_gpu: bool = False


def _tui_log(msg: str):
    _log_queue.append(msg)


def _tui_input(prompt: str = "") -> str:
    _tui_log(f"\n{Colors.YELLOW}{prompt}{Colors.RESET}")
    return _input_queue.get()


# Monkey-patch builtins so legacy code uses TUI I/O
_orig_print = builtins.print
_orig_input = builtins.input


def _patched_print(*args, **kwargs):
    sep  = kwargs.get("sep", " ")
    end  = kwargs.get("end", "\n")
    line = sep.join(str(a) for a in args) + end
    _log_queue.append(line.rstrip("\n"))


def _patched_input(prompt: str = "") -> str:
    return _tui_input(prompt)


builtins.print = _patched_print
builtins.input  = _patched_input


# -- Version helpers -----------------------------------------------------------
def _parse_version(v: str) -> tuple:
    try:
        return tuple(int(p) for p in v.strip().split("."))
    except Exception:
        return (0,)


# -- Config I/O ----------------------------------------------------------------
def load_config() -> dict:
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def save_config(config: dict):
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f)
    except Exception:
        pass


def load_saved_user() -> str:
    return load_config().get("user_id", "")


def save_user(user_id: str):
    config = load_config()
    config["user_id"] = user_id
    save_config(config)


def load_auto_update_preference():
    # Default to True -- auto-update is always enabled unless the volunteer has
    # explicitly turned it off via the settings menu. This ensures old clients
    # (which default to None/unset) also auto-update without blocking on input().
    return load_config().get("auto_update", True)


def save_auto_update_preference(enabled: bool):
    config = load_config()
    config["auto_update"] = enabled
    save_config(config)


def load_lane_override():
    return load_config().get("lane_override", None)


def save_lane_override(override):
    config = load_config()
    if override is None:
        config.pop("lane_override", None)
    else:
        config["lane_override"] = override
    save_config(config)


def load_benchmark_result() -> dict:
    return load_config().get("benchmark_result", {})


def save_benchmark_result(result: dict):
    config = load_config()
    config["benchmark_result"] = result
    save_config(config)


USER_ID_PATTERN = re.compile(r"^[a-zA-Z]+$")


def is_valid_user_id(user_id: str) -> bool:
    return bool(user_id) and 3 <= len(user_id) <= 12 and bool(USER_ID_PATTERN.fullmatch(user_id))



def make_request(url, payload=None, timeout=180, method=None):
    data = json.dumps(payload).encode('utf-8') if payload else None
    # method=None preserves the original behavior (urllib defaults to POST when data is present,
    # GET otherwise) -- only needed explicitly for a POST endpoint that takes no body, like
    # /delete_user, where relying on "data present" to imply POST doesn't work.
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'} if data else {}, method=method)
    # Default 180s (not RAG_FOLDING's original 120s) -- finetune generation prompts run longer
    # than RAG extraction, and this function serves both the Cubyz server calls and the local
    # Ollama call. Callers doing a quick status poll (version/get_work/leaderboard) pass a much
    # shorter timeout explicitly -- a 180s default there meant a genuinely unreachable server (as
    # opposed to a fast "connection refused") could leave the client silently hung for up to 3
    # minutes with nothing on screen and no way out short of Ctrl+C.
    with urllib.request.urlopen(req, timeout=timeout) as res: return json.loads(res.read().decode('utf-8'))

OLLAMA_HOST = OLLAMA_URL.rsplit("/api/", 1)[0]

def get_local_ollama_models() -> set:
    """Every model tag Ollama already has pulled on this machine, checked fresh each call (a
    /api/tags listing is a near-instant local call, not worth caching stale) -- used both to tell
    the server what this volunteer already has (see AUDIT_MODEL_ROSTER assignment, which prefers
    handing out a model the client won't need to download) and to decide whether an assigned model
    needs pulling at all before spending time on it."""
    try:
        tags = make_request(f"{OLLAMA_HOST}/api/tags", timeout=10)
        return {m.get("name") for m in tags.get("models", []) if m.get("name")} | \
               {m.get("model") for m in tags.get("models", []) if m.get("model")}
    except Exception:
        return set()

def ensure_audit_model_available(model: str, status_cb, local_models: set = None) -> bool:
    """Audit mode's model is assigned by the server from AUDIT_MODEL_ROSTER, not auto-detected
    from this machine's own benchmark like RAG/finetune's. The server already tries to assign
    something this volunteer reported having (see get_local_ollama_models() being sent with every
    /get_work call), so the common case here is just confirming that -- a pull only actually
    happens when the server had no choice but to assign something genuinely missing (e.g. every
    roster model this client already has is already claimed by someone else online)."""
    if local_models is None:
        local_models = get_local_ollama_models()
    if model in local_models:
        return True

    status_cb(f"Model '{model}' not found locally -- pulling now (may take a while)...")
    try:
        make_request(f"{OLLAMA_HOST}/api/pull", {"name": model, "stream": False}, timeout=1800)
        status_cb(f"✓ Pulled '{model}'.")
        return True
    except Exception as e:
        status_cb(f"⚠ Failed to pull '{model}': {e}")
        return False

# -- Diagnostic helpers --------------------------------------------------------
def log_diagnostic(event: dict):
    event["timestamp"] = time.time()
    try:
        with open(DIAGNOSTICS_FILE, "a") as f:
            f.write(json.dumps(event) + "\n")
    except Exception:
        pass


def submit_diagnostic_to_server(event: dict):
    try:
        make_request(f"{SERVER_URL}/diagnostics", event, timeout=10)
    except Exception:
        pass



def format_count(n) -> str:
    """1234 -> '1.2k', 1500000 -> '1.5M' -- keeps chunk/line counts readable once a campaign or a
    single user's lifetime total crosses four digits, instead of a wall of undifferentiated digits."""
    n = float(n)
    tiers = [(1_000_000_000, "B"), (1_000_000, "M"), (1_000, "k")]
    for idx, (div, suffix) in enumerate(tiers):
        if abs(n) >= div:
            value = n / div
            if round(value, 1) >= 1000 and idx > 0:
                # e.g. 999950 rounds to "1000.0k" at this tier -- bump to the next one up instead.
                bigger_div, bigger_suffix = tiers[idx - 1]
                return f"{n / bigger_div:.1f}{bigger_suffix}"
            return f"{value:.1f}{suffix}"
    return str(int(n))

def format_eta(seconds) -> str:
    if seconds is None or seconds < 0:
        return "calculating..."
    seconds = int(seconds)
    if seconds < 60:
        return f"{seconds}s"
    days, rem = divmod(seconds, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, _ = divmod(rem, 60)
    if days:
        return f"{days}d {hours}h"
    if hours:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"


# -- Update logic --------------------------------------------------------------
def _https_context() -> ssl.SSLContext:
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        pass
    for candidate in ("/etc/ssl/cert.pem", "/etc/ssl/certs/ca-certificates.crt"):
        if os.path.exists(candidate):
            return ssl.create_default_context(cafile=candidate)
    return ssl.create_default_context()


def check_for_update():
    try:
        info = make_request(f"{SERVER_URL}/version", timeout=10)
    except Exception:
        return "check_failed", None
    min_v    = info.get("min_client_version", "0.0.0")
    latest_v = info.get("latest_client_version", VERSION)
    if _parse_version(VERSION) < _parse_version(min_v):
        return "must_update", info
    if _parse_version(VERSION) < _parse_version(latest_v):
        return "update_available", info
    return "current", info


def download_update(download_url: str, expected_version: str) -> bool:
    # Retries with backoff on ANY version mismatch, not just an unparseable download -- a stale
    # raw.githubusercontent.com CDN edge cache can just as easily serve a valid, parseable OLD
    # version number (e.g. still "1.3.1") as it can serve garbage, and treating only the
    # unparseable case as retryable would miss that just as often as it catches the other. The
    # server only tells a client to download at all because it already believes expected_version
    # is live on GitHub -- so a mismatch right after that announcement is far more likely to be
    # propagation lag than a real integrity problem, and is worth a few attempts with increasing
    # backoff (3s/8s/15s, ~26s total) before actually giving up and surfacing it.
    delays = [3, 8, 15]
    for attempt in range(len(delays) + 1):
        try:
            with urllib.request.urlopen(download_url, timeout=30, context=_https_context()) as res:
                new_content = res.read()
        except Exception as e:
            print(f"{Colors.RED}[X] Update download failed: {e}{Colors.RESET}")
            return False
        match = re.search(rb'^VERSION\s*=\s*["\']([\d.]+)["\']', new_content, re.MULTILINE)
        downloaded_version = match.group(1).decode() if match else None
        if downloaded_version == expected_version:
            break
        if attempt < len(delays):
            print(f"{Colors.YELLOW}[~] Downloaded v{downloaded_version or '?'}, expected v{expected_version} -- "
                  f"likely still propagating, retrying in {delays[attempt]}s...{Colors.RESET}")
            time.sleep(delays[attempt])
            continue
        print(f"{Colors.YELLOW}[!] Downloaded v{downloaded_version or '?'} != expected v{expected_version} after retries. Skipping.{Colors.RESET}")
        return False
    this_file = os.path.abspath(__file__)
    try:
        with open(this_file, "wb") as f:
            f.write(new_content)
    except Exception as e:
        print(f"{Colors.RED}[X] Could not write update: {e}{Colors.RESET}")
        return False
    print(f"{Colors.GREEN}[OK] Update downloaded.{Colors.RESET}")
    return True


def offer_update(status: str, info: dict, mandatory: bool):
    latest_v     = info.get("latest_client_version", "?")
    download_url = info.get("download_url", "")
    if mandatory:
        print(f"\n{Colors.RED}{Colors.BOLD}[X] Client v{VERSION} no longer accepted -- update required.{Colors.RESET}")
    else:
        print(f"\n{Colors.YELLOW}[i] Update available: v{latest_v} (you have v{VERSION}).{Colors.RESET}")
    if load_auto_update_preference():
        print(f"    {Colors.CYAN}[~] Auto-update enabled -- downloading...{Colors.RESET}")
        choice = 'y'
    else:
        choice = input(f"    {Colors.YELLOW}Download the update now? (y/n): {Colors.RESET}").strip().lower()
    if choice != 'y':
        if mandatory:
            sys.exit(f"{Colors.RED}[X] Cannot continue on an unsupported version.{Colors.RESET}")
        return
    if download_update(download_url, latest_v):
        print(f"{Colors.GREEN}[OK] Restarting...{Colors.RESET}")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    elif mandatory:
        sys.exit(f"{Colors.RED}[X] Could not auto-update. Update manually: {download_url}{Colors.RESET}")


# -- Hardware detection --------------------------------------------------------
def get_linux_distro() -> str:
    try:
        with open("/etc/os-release", "r") as f:
            for line in f:
                if line.startswith("ID="):
                    return line.strip().split("=")[1].strip('"')
    except Exception:
        pass
    return "unknown"


def get_system_ram_gb() -> float:
    if PLATFORM == "darwin":
        try:
            out = subprocess.run(["sysctl", "-n", "hw.memsize"], capture_output=True, text=True, check=True).stdout.strip()
            return int(out) / (1024.0 ** 3)
        except Exception:
            pass
        print(f"{Colors.YELLOW}[!] Could not detect system RAM -- treating as unknown (0.0 GB), not guessing.{Colors.RESET}")
        return 0.0
    if PLATFORM == "win32":
        # ctypes/GlobalMemoryStatusEx first, not wmic -- confirmed live: a volunteer's real 16GB
        # machine reported as 8GB (the old hardcoded fallback below, silently triggered) because
        # `wmic` itself is deprecated and has been removed from newer Windows 11 builds entirely
        # (subprocess.run raised FileNotFoundError, caught by the bare except, fell through to
        # the fallback). That wrong 8GB then incorrectly blocked "enable parallel" (needs 14GB)
        # on a machine that actually had plenty. GlobalMemoryStatusEx is a raw Win32 API call via
        # the stdlib's ctypes -- no external process, nothing to be missing/deprecated out from
        # under it, works identically on every Windows version back to XP.
        try:
            import ctypes

            class _MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [
                    ("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                    ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                    ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                    ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                    ("sullAvailExtendedVirtual", ctypes.c_ulonglong),
                ]

            stat = _MEMORYSTATUSEX()
            stat.dwLength = ctypes.sizeof(_MEMORYSTATUSEX)
            if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
                return stat.ullTotalPhys / (1024.0 ** 3)
        except Exception:
            pass
        # wmic as a fallback, not the primary path -- still works on older Windows builds that
        # have it, so there's no harm trying it before giving up entirely.
        try:
            result = subprocess.run(["wmic", "ComputerSystem", "get", "TotalPhysicalMemory", "/value"],
                                    capture_output=True, text=True, timeout=15)
            for line in result.stdout.split("\n"):
                if "TotalPhysicalMemory" in line and "=" in line:
                    return int(line.split("=")[1].strip()) / (1024.0 ** 3)
        except Exception:
            pass
        print(f"{Colors.YELLOW}[!] Could not detect system RAM -- treating as unknown (0.0 GB), not guessing.{Colors.RESET}")
        return 0.0
    try:
        with open("/proc/meminfo", "r") as f:
            for line in f:
                if line.startswith("MemTotal:"):
                    return int(line.split()[1]) / (1024.0 * 1024.0)
    except Exception:
        pass
    print(f"{Colors.YELLOW}[!] Could not detect system RAM -- treating as unknown (0.0 GB), not guessing.{Colors.RESET}")
    return 0.0


def is_apple_silicon() -> bool:
    return platform.machine() == "arm64"


def check_apple_silicon_gpu() -> tuple:
    if not is_apple_silicon():
        return False, 0.0
    ram_gb = get_system_ram_gb()
    return True, min(ram_gb - 3.5, ram_gb * 0.75)


def check_nvidia_gpu() -> tuple:
    try:
        res = subprocess.run(['nvidia-smi', '--query-gpu=memory.total', '--format=csv,nounits,noheader'],
                             capture_output=True, text=True, check=True, timeout=15)
        vram = int(res.stdout.strip().split('\n')[0]) / 1024.0
        return True, vram
    except Exception:
        pass
    return False, 0.0


def _amd_vram_from_sysfs() -> float:
    try:
        for p in glob.glob("/sys/class/drm/card*/device/mem_info_vram_total"):
            with open(p) as f:
                val = int(f.read().strip())
                if val > 0:
                    return val / (1024.0 ** 3)
    except Exception:
        pass
    return 0.0


def check_amd_gpu() -> tuple:
    vram = _amd_vram_from_sysfs()
    if vram > 0:
        return True, vram
    for tool in ["rocm-smi", "/opt/rocm/bin/rocm-smi"]:
        try:
            res  = subprocess.run([tool, "--showmeminfo", "vram", "--json"],
                                  capture_output=True, text=True, timeout=10)
            data = json.loads(res.stdout)
            for card_data in data.values():
                total = card_data.get("VRAM Total Memory (B)", 0)
                if total:
                    return True, int(total) / (1024.0 ** 3)
        except Exception:
            pass
    try:
        pci = subprocess.run(['lspci'], capture_output=True, text=True).stdout
        if "amd" in pci.lower() or "radeon" in pci.lower():
            return True, vram
    except Exception:
        pass
    return False, 0.0


def check_intel_gpu() -> tuple:
    try:
        pci = subprocess.run(['lspci'], capture_output=True, text=True).stdout
        if "intel" in pci.lower() and ("vga" in pci.lower() or "display" in pci.lower()):
            return True, 0.0
    except Exception:
        pass
    return False, 0.0


# -- GPU tier / model selection ------------------------------------------------
# SPARE VRAM required on top of the model's own resident footprint before enabling parallel
# workers. These match CUBYZ_FOLDING.py exactly -- the floor is NOT the tier's minimum VRAM
# (that's gpu_tier_from_vram's job), it's how much must be free ABOVE the already-loaded model.
GPU_TIER_VRAM_FLOOR_GB = {"easy": 0.0, "medium": 4.5, "hard": 8.5}
CPU_TIER_RAM_FLOOR_GB  = {"easy": 6.0, "medium": 8.0}
DUAL_LANE_MIN_RAM_GB   = 12.0
DUAL_LANE_MIN_VRAM_GB  = 4.0
TIER_RANK              = {"easy": 0, "medium": 1, "hard": 2}
BENCHMARK_VERSION      = 6
BENCHMARK_TIMEOUT      = 90
# hard tier uses 2 workers (not 3) -- a 14b/32b model already saturates the GPU, so
# adding a third concurrent slot just causes thrashing rather than throughput gains.
PARALLEL_WORKERS_BY_TIER                      = {"easy": 3, "medium": 2, "hard": 2}
PARALLEL_WORKERS_MAX                          = max(PARALLEL_WORKERS_BY_TIER.values())
PARALLEL_WORKERS_VRAM_HEADROOM_PER_WORKER_GB  = {"easy": 1.0, "medium": 2.0, "hard": 3.5}
PARALLEL_WORKERS_RAM_HEADROOM_PER_WORKER_GB   = {"easy": 1.5, "medium": 3.0}



def gpu_tier_from_vram(vram: float) -> str:
    if vram <= 4.5:
        return "easy"
    if vram <= 8.5:
        return "medium"
    return "hard"


def get_cpu_model_tier(ram_gb: float):
    if ram_gb >= 8.0:
        return "qwen2.5-coder:7b", "medium"
    if ram_gb >= 6.0:
        return "qwen2.5-coder:3b", "easy"
    return None, None


def get_cpu_name() -> str:
    try:
        if PLATFORM == "darwin":
            res = subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"], capture_output=True, text=True, timeout=5)
            if res.returncode == 0 and res.stdout.strip():
                return res.stdout.strip()
        elif PLATFORM == "win32":
            res = subprocess.run(["wmic", "cpu", "get", "name"], capture_output=True, text=True, timeout=5)
            lines = [l.strip() for l in res.stdout.splitlines() if l.strip() and "Name" not in l]
            if lines:
                return lines[0]
        else:
            try:
                res = subprocess.run(["lscpu"], capture_output=True, text=True, timeout=5)
                for line in res.stdout.splitlines():
                    if "Model name:" in line:
                        return line.split(":", 1)[1].strip()
            except Exception:
                pass
            with open("/proc/cpuinfo", "r") as f:
                for line in f:
                    if "model name" in line:
                        return line.split(":", 1)[1].strip()
    except Exception:
        pass
    return "CPU"


def get_gpu_name(gpu_type: str) -> str:
    try:
        if gpu_type == "nvidia":
            res = subprocess.run(['nvidia-smi', '--query-gpu=name', '--format=csv,nounits,noheader'],
                                 capture_output=True, text=True, timeout=5)
            if res.returncode == 0 and res.stdout.strip():
                return res.stdout.strip().splitlines()[0]
        elif gpu_type == "amd":
            for tool in ["rocm-smi", "/opt/rocm/bin/rocm-smi"]:
                try:
                    res = subprocess.run([tool, "--showproductname", "--json"], capture_output=True, text=True, timeout=5)
                    data = json.loads(res.stdout)
                    for card in data.values():
                        name = card.get("Card series") or card.get("Card model")
                        if name:
                            return str(name)
                except Exception:
                    pass
            try:
                res = subprocess.run(['lspci'], capture_output=True, text=True, timeout=5)
                for line in res.stdout.splitlines():
                    if any(k in line.lower() for k in ["vga", "3d", "display"]) and ("amd" in line.lower() or "radeon" in line.lower()):
                        if "[" in line and "]" in line:
                            parts = line.split("[")
                            for p in parts[1:]:
                                if "]" in p:
                                    clean = p.split("]")[0].replace("Advanced Micro Devices, Inc.", "").replace("AMD/ATI", "").strip()
                                    if clean:
                                        return f"AMD {clean}"
            except Exception:
                pass
            return "AMD Radeon GPU"
        elif gpu_type == "apple_silicon":
            return get_cpu_name()
    except Exception:
        pass
    return gpu_type.upper()


def get_vram_and_choose_model() -> tuple:
    if PLATFORM == "darwin":
        ok, vram = check_apple_silicon_gpu()
        if ok:
            if vram >= 20.0: return "qwen2.5-coder:32b", "apple_silicon", vram
            if vram >= 12.0: return "qwen2.5-coder:14b", "apple_silicon", vram
            if vram >= 6.0:  return "qwen2.5-coder:7b",  "apple_silicon", vram
            return "qwen2.5-coder:3b", "apple_silicon", vram
        ok, vram = check_intel_gpu()
        if ok:
            return "qwen2.5-coder:3b", "intel_dgpu", vram
    ok, vram = check_nvidia_gpu()
    if ok:
        if vram >= 20.0: return "qwen2.5-coder:32b", "nvidia", vram
        if vram >= 12.0: return "qwen2.5-coder:14b", "nvidia", vram
        if vram >= 6.0:  return "qwen2.5-coder:7b",  "nvidia", vram
        return "qwen2.5-coder:3b", "nvidia", vram
    ok, vram = check_amd_gpu()
    if ok:
        if vram >= 20.0: return "qwen2.5-coder:32b", "amd", vram
        if vram >= 12.0: return "qwen2.5-coder:14b", "amd", vram
        if vram >= 6.0:  return "qwen2.5-coder:7b",  "amd", vram
        return "qwen2.5-coder:3b", "amd", vram
    ram_gb = get_system_ram_gb()
    cpu_model, cpu_tier = get_cpu_model_tier(ram_gb)
    if cpu_model is None:
        sys.exit(f"{Colors.RED}[X] Insufficient RAM ({ram_gb:.1f} GB). Min 6 GB required.{Colors.RESET}")
    return cpu_model, "cpu", 0.0


_BENCHMARK_SNIPPET = """pub fn calculateDamage(base: f32, multiplier: f32, armor: f32) f32 {
	const raw = base * multiplier;
	const reduction = armor / (armor + 100.0);
	return raw * (1.0 - reduction);
}

pub const DamageType = enum {
	physical,
	fire,
	poison,
};"""

def benchmark_lane(model: str, force_cpu: bool):
    """Times a real Ollama generation -- using the actual RAG_JSON_SCHEMA format constraint and
    prompt shape real crunching uses, not a trivial one-line completion -- to measure actual
    throughput on real-shaped work. Run once per machine (see main()'s use of
    load_benchmark_result()/save_benchmark_result()) to decide which of CPU/GPU actually performs
    better HERE, rather than guessing from declared hardware specs. VRAM detection in particular
    has repeatedly proven unreliable across GPU vendors and driver/tooling states (see
    check_amd_gpu()'s history in this file) -- and even when the VRAM number is accurate, a
    technically-present GPU can still be too weak, or too poorly supported by whatever backend
    Ollama uses for it, to actually be worth using at all. Measuring real throughput sidesteps
    needing to trust either signal.

    Deliberately NOT a trivial short completion: an earlier version used a bare one-sentence
    prompt capped at 40 tokens, which could finish quickly even on a GPU that then went on to
    hang or stall on real crunching calls (confirmed live -- a card whose 40-token benchmark
    completed in under 5 seconds, "winning" against CPU, turned out to get stuck indefinitely on
    real, much longer, schema-constrained generation once actually crunching). Using the same
    format constraint and a similarly-shaped prompt as real work is what makes this predictive of
    real usability rather than just "can it echo a sentence back quickly."

    Returns (elapsed_seconds, None) on success, or (None, error_description) if the lane failed
    outright or didn't finish within BENCHMARK_TIMEOUT. error_description used to just be
    discarded entirely (a bare `except Exception: return None`) -- confirmed live, this made a
    failed GPU benchmark completely unexplainable from the outside: "FAILED or timed out" could
    mean Ollama isn't running, the GPU driver crashed, the model doesn't fit in VRAM, a real
    request timeout, or something else, and there was no way to tell which without the volunteer
    manually digging through their own machine.
    """
    payload = {
        "model": model,
        "prompt": f"Context Source File: benchmark.zig\nRelative Path: benchmark.zig\nDirectory Module context: CODEBASE\nChunk Index: 0\nRaw Content:\n```\n{_BENCHMARK_SNIPPET}\n```\n",
        "system": RAG_PROMPTS["CODEBASE"],
        "stream": False,
        "think": False,
        "format": RAG_JSON_SCHEMA,
        "options": {"temperature": 0.15, **({"num_gpu": 0} if force_cpu else {})},
    }
    start = time.time()
    for attempt in range(2):
        try:
            make_request(OLLAMA_URL, payload, timeout=BENCHMARK_TIMEOUT)
            break
        except Exception as e:
            elapsed = time.time() - start
            kind = "timeout" if elapsed >= BENCHMARK_TIMEOUT - 1 else type(e).__name__
            # HTTPError's own str() is just "HTTP Error 500: Internal Server Error" -- the generic
            # reason phrase, not why. Ollama's actual JSON error body (e.g. an OOM message, "model
            # requires more system memory than is available", a corrupted-file read error) lives
            # in the response body instead, and was being silently dropped here -- confirmed live,
            # a volunteer's failed benchmark showed only the generic 500 text with no way to tell
            # whether that meant "Ollama ran out of memory," "the model file is corrupted," or
            # something else entirely, all of which need different fixes.
            detail = _http_error_body(e)
            # Belt-and-suspenders with warm_up_model()'s own repull -- this catches the case where
            # warm-up itself already "succeeded" against a corrupted file (some corruption doesn't
            # surface until a longer, differently-shaped request) and only shows up here instead.
            if attempt == 0 and _is_corrupt_model_error(detail) and _repull_model(model):
                start = time.time()
                continue
            return None, f"{kind}: {e}{(' -- ' + detail.strip()) if detail else ''}"[:300]
    elapsed = time.time() - start

    if not force_cpu:
        # A "GPU" call finishing within budget does NOT actually prove Ollama ran it on the GPU --
        # omitting num_gpu just means "let Ollama decide," and Ollama silently falls back to CPU
        # whenever it can't really use the GPU (an unsupported ROCm architecture, no
        # HSA_OVERRIDE_GFX_VERSION set for an unlisted AMD card, etc). Confirmed live: on a machine
        # where Ollama couldn't actually use its AMD GPU, this "GPU" call quietly ran on CPU and
        # still finished in time -- reported as "GPU benchmarked successfully" -- while the
        # explicitly CPU-forced call, now contending for the same CPU cores concurrently, timed out
        # and got mislabeled as "CPU failed." Reality was the exact opposite of what got reported.
        # /api/ps reports how many bytes of the loaded model are actually resident on GPU
        # (size_vram) -- checked here instead of just trusted.
        try:
            ps = make_request(f"{OLLAMA_HOST}/api/ps", timeout=10)
            entry = next((m for m in ps.get("models", []) if m.get("model") == model or m.get("name") == model), None)
            size_vram = (entry or {}).get("size_vram", 0)
            if not size_vram:
                return None, f"no_gpu_offload: request finished in {elapsed:.1f}s but Ollama reports 0 bytes resident on GPU -- it silently ran on CPU instead"
        except Exception:
            pass  # /api/ps itself failing shouldn't invalidate an otherwise-successful benchmark
    return elapsed, None

# -- Ollama install / run ------------------------------------------------------
def install_docker():
    distro = get_linux_distro()
    try:
        if distro in ["ubuntu", "debian", "pop", "mint"]:
            subprocess.run("sudo apt-get update && sudo apt-get install -y docker.io", shell=True, check=True)
        elif distro in ["arch", "manjaro"]:
            subprocess.run("sudo pacman -S --noconfirm docker", shell=True, check=True)
        else:
            subprocess.run("curl -fsSL https://get.docker.com | sh", shell=True, check=True)
        subprocess.run("sudo systemctl enable --now docker", shell=True, check=True)
    except KeyboardInterrupt:
        sys.exit(f"\n{Colors.CYAN}[X] Docker install cancelled.{Colors.RESET}")
    except Exception as e:
        sys.exit(f"{Colors.RED}[X] Docker install failed: {e}{Colors.RESET}")


def install_ollama_container(gpu_type: str):
    gpu_flags, image_name = "", "ollama/ollama"
    if gpu_type == "amd":
        gpu_flags, image_name = "--device /dev/kfd --device /dev/dri", "ollama/ollama:rocm"
    elif gpu_type == "nvidia":
        gpu_flags = "--gpus all"
    try:
        subprocess.run(
            f"sudo docker run -d -e OLLAMA_NUM_PARALLEL={PARALLEL_WORKERS_MAX} {gpu_flags} "
            f"-v ollama:/root/.ollama -p 11434:11434 --name ollama {image_name}",
            shell=True, check=True,
        )
    except Exception as e:
        sys.exit(f"{Colors.RED}[X] Container deploy failed: {e}{Colors.RESET}")


def ensure_ollama_installed(gpu_type: str = None):
    if PLATFORM == "linux":
        has_docker = bool(shutil.which("docker"))
        if shutil.which("ollama") or (has_docker and "ollama" in subprocess.run(
                ["docker", "ps", "-a", "--format", "{{.Names}}"], capture_output=True, text=True).stdout):
            return
        print(f"{Colors.CYAN}[~] Ollama not found. Initializing setup...{Colors.RESET}")
        if input("Run Ollama inside Docker? (y/n): ").strip().lower() == 'y':
            if not has_docker:
                install_docker()
            install_ollama_container(gpu_type)
        else:
            try:
                subprocess.run("curl -fsSL https://ollama.com/install.sh | sh", shell=True, check=True)
            except Exception as e:
                sys.exit(f"{Colors.RED}[X] Install failed: {e}{Colors.RESET}")
        return
    if shutil.which("ollama"):
        return
    if PLATFORM == "darwin":
        if shutil.which("brew"):
            try:
                subprocess.run(["brew", "install", "ollama"], check=True)
                return
            except Exception:
                pass
        sys.exit(f"{Colors.RED}[X] Install Ollama from https://ollama.com/download/mac{Colors.RESET}")
    if PLATFORM == "win32":
        print(f"{Colors.CYAN}[~] Install Ollama from: https://ollama.com/download/windows{Colors.RESET}")
        input("[?] Once installed, press [ENTER] to continue... ")
        if not shutil.which("ollama"):
            sys.exit("[X] Ollama still not found. Restart terminal and try again.")


def _is_ollama_running() -> bool:
    try:
        urllib.request.urlopen("http://localhost:11434", timeout=3)
        return True
    except Exception:
        return False


def _start_ollama_native():
    # OLLAMA_NUM_PARALLEL defaults to 1 (Ollama serializes generation requests) unless set --
    # the Docker deployment path (install_ollama_container) already sets this explicitly, but
    # nothing did for a native install, since this is the only place that actually launches an
    # Ollama process this script controls. Only helps when WE start it -- if Ollama's already
    # running (the common case on Windows, where the official installer sets it up to auto-start
    # in the background before this script ever runs), an env var here can't reach into an
    # already-running process; that case is instead flagged to the user directly at the point
    # they try to enable parallel workers (see _get_gpu_worker_slots's caller).
    env = {**os.environ, "OLLAMA_NUM_PARALLEL": str(PARALLEL_WORKERS_MAX)}
    try:
        subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, env=env)
    except Exception:
        pass


def _http_error_body(e: Exception) -> str:
    if isinstance(e, urllib.error.HTTPError):
        try:
            return e.read().decode("utf-8", errors="replace")
        except Exception:
            pass
    return ""


def _is_corrupt_model_error(text: str) -> bool:
    """True for Ollama's own "this model's files on disk are broken" signature -- not a GPU
    problem, not this script's request, not slowness. Confirmed live: a volunteer's GPU benchmark
    failed with `"error loading model: read error: Data error (cyclic redundancy check)"` -- a
    corrupted GGUF blob, almost certainly from an interrupted first download -- which had been
    surfacing as an opaque "HTTP Error 500" (and, before that fix, as what looked like a plain
    timeout, since Ollama loads, fails immediately, and unloads with no visible generation
    progress under stream:false) until the error body itself was actually being read and shown."""
    if not text:
        return False
    low = text.lower()
    return any(s in low for s in ("cyclic redundancy check", "data error", "error loading model", "checksum"))


def _repull_model(model_name: str) -> bool:
    """Deletes and re-downloads model_name -- the actual fix for _is_corrupt_model_error, not
    just a better error message for it. Without this, a volunteer with one corrupted download
    would silently lose their GPU lane forever (every future run hits the identical error and
    falls back to CPU) unless they happened to notice the raw error and knew to run `ollama rm`/
    `ollama pull` themselves."""
    print(f"{Colors.YELLOW}[~] {model_name} looks corrupted on disk (failed integrity check) -- re-downloading...{Colors.RESET}")
    try:
        make_request(f"{OLLAMA_HOST}/api/delete", {"name": model_name}, timeout=30, method="DELETE")
    except Exception:
        pass  # already gone / never existed -- the pull below is what actually matters
    try:
        make_request(f"{OLLAMA_HOST}/api/pull", {"name": model_name, "stream": False}, timeout=1800)
        print(f"{Colors.GREEN}[OK] {model_name} re-downloaded.{Colors.RESET}")
        return True
    except Exception as e:
        print(f"{Colors.RED}[X] Re-download failed: {e}{Colors.RESET}")
        return False


def warm_up_model(model_name: str):
    """Forces Ollama to actually load model_name into memory, with a generous, untimed-feeling
    budget -- called once before the real timed benchmark so a slow FIRST load (reading a
    multi-GB file off disk, GPU driver/kernel JIT on first use, antivirus scanning the model file
    on Windows -- all real, all observed) doesn't eat into BENCHMARK_TIMEOUT and get misreported
    as "GPU benchmark timed out"/GPU failure. Confirmed live: a volunteer on an RTX 4060 Ti (12GB,
    plenty for these models, CUDA fully supported) got a benchmark timeout on Windows -- a machine
    that capable timing out on ~90s of actual generation makes far less sense than the FIRST-load
    overhead alone blowing that budget before generation even started, which this eliminates by
    paying that cost here instead, off the benchmark clock.

    Also self-heals a corrupted local model file (see _is_corrupt_model_error) by re-pulling and
    retrying once -- this is the earliest point that failure can be caught, before the real timed
    benchmark ever runs into the same dead end. Any other failure just returns quietly; the real
    benchmark right after will hit the same problem and report a real, actionable error there.
    """
    for attempt in range(2):
        try:
            make_request(OLLAMA_URL, {
                "model": model_name, "prompt": "hi", "stream": False,
                "options": {"num_predict": 1},
            }, timeout=300)
            return
        except Exception as e:
            if attempt == 0 and _is_corrupt_model_error(_http_error_body(e)) and _repull_model(model_name):
                continue
            return


def ensure_ollama_running_and_model_pulled(model_name: str):
    if not _is_ollama_running():
        print(f"{Colors.CYAN}[~] Starting Ollama...{Colors.RESET}")
        _start_ollama_native()
        for _ in range(30):
            time.sleep(1)
            if _is_ollama_running():
                break
        else:
            sys.exit(f"{Colors.RED}[X] Ollama failed to start. Start it manually and re-run.{Colors.RESET}")

    # Use the HTTP /api/tags endpoint instead of the CLI -- works when Ollama runs inside
    # Docker with no 'ollama' binary on PATH (the CLI raises FileNotFoundError in that case).
    try:
        tags = make_request(f"{OLLAMA_HOST}/api/tags", timeout=10)
        pulled = {m.get("name") for m in tags.get("models", [])} | \
                 {m.get("model") for m in tags.get("models", [])}
        if model_name not in pulled:
            print(f"{Colors.CYAN}[~] Pulling model {model_name} (one-time download)...{Colors.RESET}")
            make_request(f"{OLLAMA_HOST}/api/pull", {"name": model_name, "stream": False}, timeout=1800)
            print(f"{Colors.GREEN}[OK] Model {model_name} pulled.{Colors.RESET}")
    except Exception as e:
        # If the tags check itself fails, attempt a native pull as fallback
        if shutil.which("ollama"):
            try:
                subprocess.run(["ollama", "pull", model_name], timeout=600, check=True)
            except Exception:
                pass
        else:
            print(f"{Colors.YELLOW}[!] Could not verify/pull model '{model_name}': {e}{Colors.RESET}")


# -- GPU architecture check ----------------------------------------------------
GPU_ARCH_COMPATIBILITY = {"amd": {"unsupported": ["gfx803","gfx900","gfx902","gfx906","gfx908"]}}


def check_gpu_architecture_support(gpu_type: str) -> tuple:
    if gpu_type != "amd":
        return False, ""
    unsupported = GPU_ARCH_COMPATIBILITY.get("amd", {}).get("unsupported", [])
    try:
        for tool in ["rocminfo", "/opt/rocm/bin/rocminfo"]:
            if shutil.which(tool) or os.path.exists(tool):
                res = subprocess.run([tool], capture_output=True, text=True, timeout=15)
                for arch in unsupported:
                    if arch in res.stdout:
                        return True, f"GPU uses unsupported arch {arch}"
                return False, ""
    except Exception:
        pass
    return False, ""


# -- Leaderboard / userlist helpers --------------------------------------------
def fetch_leaderboard_text() -> str:
    try:
        stats = make_request(f"{SERVER_URL}/leaderboard", timeout=10)
    except Exception as e:
        return f"{Colors.RED}[X] Could not reach server: {e}{Colors.RESET}"
    is_audit = stats.get("mode") == "audit"
    tot      = stats.get("total_chunks_in_codebase") or stats.get("total_chunks_due") or 1
    comp     = stats.get("total_chunks_completed", 0)
    pct      = stats.get("global_percentage", 0.0)
    bar_len  = 20
    filled   = max(0, min(bar_len, int(round(bar_len * comp / float(tot))))) if tot else 0
    p_bar    = chr(9608) * filled + chr(9617) * (bar_len - filled)
    lines    = [
        f"{Colors.YELLOW}--- [ CUBYZ LEADERBOARD ] ---{Colors.RESET}",
        f"  Progress : [{Colors.GREEN}{p_bar}{Colors.RESET}] {format_count(comp)}/{format_count(tot)} ({pct:.2f}%)",
        f"  ETA      : {format_eta(stats.get('eta_seconds'))}",
    ]
    for u in stats.get("rankings", []):
        rank  = u.get('rank', '?')
        color = f"{Colors.YELLOW}{Colors.BOLD}" if rank == 1 else ""
        reset = Colors.RESET if rank == 1 else ""
        if is_audit:
            stat_text = (f"{format_count(u.get('chunks_audited', 0))} audited  "
                         f"{format_count(u.get('issues_found', 0))} issues  "
                         f"{format_count(u.get('reviews_done', 0))} reviewed  "
                         f"{format_count(u.get('fixes_applied', 0))} fixes")
        else:
            lc        = u.get("lines_crunched", u.get("pairs_generated", 0))
            stat_text = f"{format_count(u.get('chunks_completed', 0))} chunks  {format_count(lc)} lines"
        lines.append(f"  {color}#{rank:<3}{reset} {u.get('user_id', '?'):<14} {stat_text}")
    lines.append(f"{Colors.YELLOW}-----------------------------{Colors.RESET}")
    return "\n".join(lines)


def fetch_userlist_text() -> str:
    try:
        stats = make_request(f"{SERVER_URL}/leaderboard", timeout=10)
    except Exception as e:
        return f"{Colors.RED}[X] Could not reach server: {e}{Colors.RESET}"
    users   = stats.get("rankings", [])
    online  = [u for u in users if "ONLINE" in u.get("status", "")]
    offline = [u for u in users if "ONLINE" not in u.get("status", "")]
    lines   = [
        f"{Colors.CYAN}--- [ ACTIVE NODE ROSTER ] ---{Colors.RESET}",
        f"  {Colors.GREEN}{len(online)} online{Colors.RESET}  {Colors.GRAY}{len(offline)} offline{Colors.RESET}",
    ]
    for u in online + offline:
        is_on = "ONLINE" in u.get("status", "")
        sc    = Colors.GREEN if is_on else Colors.GRAY
        lines.append(f"  {sc}{u.get('status', '?'):<10}{Colors.RESET} {u.get('user_id', '?')}")
    lines.append(f"{Colors.CYAN}------------------------------{Colors.RESET}")
    return "\n".join(lines)


# -- GPU diagnostic ------------------------------------------------------------
def run_live_gpu_diagnostic():
    print(f"{Colors.CYAN}[~] Running GPU diagnostic...{Colors.RESET}")
    ok, vram = check_nvidia_gpu()
    if ok:
        print(f"{Colors.GREEN}[OK] NVIDIA GPU detected, {vram:.1f} GB VRAM{Colors.RESET}")
        return
    ok, vram = check_amd_gpu()
    if ok:
        print(f"{Colors.GREEN}[OK] AMD GPU detected, {vram:.1f} GB VRAM{Colors.RESET}")
        return
    ok, vram = check_apple_silicon_gpu()
    if ok:
        print(f"{Colors.GREEN}[OK] Apple Silicon, {vram:.1f} GB effective{Colors.RESET}")
        return
    print(f"{Colors.YELLOW}[!] No dedicated GPU detected -- CPU-only mode{Colors.RESET}")


RAG_JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "summary": {
            "type": "string",
            "description": "A concise 1-2 sentence overview of the chunk's primary purpose."
        },
        "comprehensive_explanation": {
            "type": "string",
            "description": "Dense, explicit technical explanation of only what is present: logic, flow, architecture, algorithms, state changes, interactions, memory ownership, serialization, networking, validation, or gameplay mechanics."
        },
        "symbols": {
            "type": "array",
            "description": "Important identifiers explicitly declared or referenced in the chunk.",
            "items": {"type": "string"}
        },
        "concepts": {
            "type": "array",
            "description": "High-level engine or gameplay concepts represented by the chunk.",
            "items": {"type": "string"}
        },
        "keywords": {
            "type": "array",
            "description": "Short searchable technical keywords for retrieval.",
            "items": {"type": "string"},
            "minItems": 5,
            "maxItems": 15
        },
        "chunk_type": {
            "type": "string",
            "enum": [
                "implementation", "algorithm", "api", "serialization", "networking", "world_generation",
                "configuration", "documentation", "review", "ui", "asset", "gameplay", "other"
            ]
        },
        "code_example": {
            "type": ["string", "null"],
            "description": "Minimal code snippet illustrating the core implementation. Null if none exists."
        },
        "synthetic_queries": {
            "type": "array",
            "description": "Natural developer questions likely to retrieve this chunk.",
            "items": {"type": "string"},
            "minItems": 6,
            "maxItems": 12
        }
    },
    "required": [
        "summary",
        "comprehensive_explanation",
        "symbols",
        "concepts",
        "keywords",
        "chunk_type",
        "code_example",
        "synthetic_queries"
    ],
    "additionalProperties": False
}

RAG_PROMPTS = {
    "CODEBASE": """You are a deterministic data-extraction compiler documenting the Cubyz voxel engine codebase.
Your task is to parse raw content and emit strict JSON describing only the technical realities explicitly present in the source.

Source role: FUNCTIONAL_CODEBASE_LOGIC (.zig, .zon) -- architecture, execution flow, data structures, APIs, engine behavior.

Constraints:
- ZERO EXTRAPOLATION: do not infer or assume anything not explicit; preserve identifiers exactly.
- LANGUAGE ADAPTATION:
    - .zig: extract executable logic; preserve function names and signatures where visible.
    - .zon: treat as configuration/data; extract exact structure; do not invent wrappers.
- DENSE FACTS: each sentence must convey concrete technical information; no introductions or opinions; avoid repetition.
- SUMMARY: 1-2 sentences; state primary chunk responsibility only.
- COMPREHENSIVE_EXPLANATION: describe only information found in the chunk; focus on execution flow, function responsibilities, state transitions, algorithms, dependencies, data structures, error handling, concurrency, memory ownership, serialization, file I/O, networking, and inter-component interactions; do not repeat the summary.
- SYMBOLS: each entry is a bare NAME only -- never a full statement, never containing `(`, `)`, `{`, `;`, or `=`. Include a name only if this chunk itself declares it via `const NAME = struct`, `const NAME = enum`, `const NAME = union`, `fn NAME(`, `pub fn NAME(`, a struct field `NAME:`, or `pub const NAME = @import(...)` (a PUBLIC re-export -- this file is choosing to expose NAME as part of its own API, so it counts as declared here even though the value comes from another file). Exclude anything that is only a local variable inside a function body, only the target of a function call, only a builtin (`@memcpy`, `@import`, ...), or a PRIVATE (non-`pub`) `const NAME = @import(...)` alias used just for internal convenience. If a `fn` or field is declared inside another struct's body, qualify it as `Parent.name`; top-level declarations stay bare.
  - CORRECT pattern: a chunk defining `pub const SomeStruct = struct { fieldName: SomeType, pub fn someMethod(...) T {...} }` has symbols `SomeStruct`, `SomeStruct.fieldName`, `SomeStruct.someMethod` -- names copied from THIS chunk's own declarations, never from an example.
  - CORRECT pattern: a chunk that is only `pub const SomeName = @import("other_file.zig");` (no `struct`/`fn` anywhere) has symbols `SomeName`, because it's a `pub const` re-export -- this file's entire declared surface.
  - INCORRECT: including an imported type used only as a field's type annotation (not declared here); including a whole statement instead of a bare name; or including `someLocalVar.someMethod()` (a call inside a function body, not a declaration).
- CONCEPTS: name the high-level engine/gameplay concepts the chunk implements (e.g. chunk meshing, entity ECS, world generation, networking protocol).
- KEYWORDS: 5-15 short (1-3 word) technical terms a developer would search for -- domain nouns and mechanism names (e.g. "reference counting", "binary serialization", "mutex locking"). Never a raw code expression, dotted call, or anything containing `(`, `)`, or `.` taken verbatim from the source.
- CHUNK_TYPE: pick exactly one enum value by what the chunk's code DOES, not its file location: "serialization" = binary/text encode-decode, read/write formats; "networking" = sockets, packets, protocol messages; "algorithm" = a self-contained computational procedure (pathing, compression, hashing); "api" = a public interface surface meant for other modules to call; "world_generation" = terrain/structure/biome generation; "configuration" = static settings/config data with no executable logic; "gameplay" = player-facing mechanics (combat, inventory, movement rules); "implementation" = general engine logic not covered by the above; use "other" only if truly none apply.
- CODE_EXAMPLE: mechanical procedure, follow it exactly: (1) find every function/method body in the chunk; (2) count the raw lines between each one's opening `{` and matching closing `}`; (3) copy the one with the FEWEST lines VERBATIM, character-for-character, from THIS chunk's own raw content, including every line of its body -- ignore how "important" or "illustrative" it looks, line count is the only criterion. This must be a fresh copy of text that is actually present in the raw content you were given for THIS chunk -- never reuse, recall, or adapt a snippet from any other file or from these instructions themselves. Never omit or replace any part of the body with "..." -- if that impulse comes up, you picked the wrong (too long) function; go back to step 3 and pick the next-shortest one instead. Set null ONLY if the chunk truly has no function bodies or struct/enum definitions at all (e.g. pure imports or comments).
  - CORRECT: the chunk's own shortest complete function or struct/enum body, copied character-for-character from the raw content above -- e.g. if the chunk has a 3-line getter and a 40-line initializer, extract the getter's full 3 lines verbatim, nothing more and nothing paraphrased.
  - INCORRECT: a truncated body with "..." in place of real lines; a function signature with no body at all; or ANY code that does not appear verbatim in this specific chunk's raw content, no matter how plausible it looks.
- SYNTHETIC_QUERIES: generate as many retrieval questions as this chunk's actual content genuinely supports (architecture, implementation, debugging, API lookup, symbol lookup, execution flow, dependency lookup), minimum 6, maximum 12. The minimum of 6 is a legitimate, common outcome for a small or simple chunk -- do NOT stretch toward 12 by inventing speculative questions about "best practices," "potential issues," "future considerations," "how this might affect other code," or any other topic the chunk itself does not address. Every question must be answerable using only what is explicitly in this chunk. Fewer real questions is always better than more invented ones.

OUTPUT: valid JSON conforming to the schema. No markdown, no commentary.
""",
    "WIKI": """You are a deterministic data-extraction compiler documenting Cubyz voxel engine documentation.
Parse documentation and emit strict JSON describing only explicitly documented information.

Source role: DEFINITIVE_WIKI_DOCUMENTATION (.md, .txt, .html)

Constraints:
- ZERO EXTRAPOLATION: rely exclusively on explicitly mentioned game concepts, features, specs, and config properties.
- DENSE FACTS: each sentence must convey concrete technical information; no introductions or opinions; avoid repetition.
- SUMMARY: 1-2 sentences.
- COMPREHENSIVE_EXPLANATION: capture mechanics, gameplay systems, configuration, terminology, limitations, workflows, design intent, requirements, examples; no undocumented behavior.
- VERBATIM FACT PRESERVATION: if the source states a specific number, exact command/config syntax, named value, or a direct question-and-answer pair (e.g. an FAQ entry), COMPREHENSIVE_EXPLANATION must state that value or answer explicitly and completely -- never replace it with a description of its topic or existence. Failure example: writing "covers healing mechanics" when the source literally says "there is no way to heal" is a failure; the actual answer must appear. For FAQ-style, table, or list-structured content specifically, restate each individual entry's actual content one by one, not just an overview of what the list covers as a whole.
- SYMBOLS: explicitly documented commands, configuration keys, block/item/biome/API/entity names.
- CONCEPTS: name the high-level gameplay or documentation topics the chunk covers.
- KEYWORDS: generate 5-15 concise technical keywords present in the chunk.
- CHUNK_TYPE: classify using exactly one enum value that best matches the chunk's role.
- CODE_EXAMPLE: literal code/config examples; otherwise null.
- SYNTHETIC_QUERIES: generate 6-12 retrieval questions (gameplay, mechanics, configuration, terminology, troubleshooting).

OUTPUT: schema-compliant JSON only.
""",
    "GITHUB_REVIEWS": """You are a deterministic data-extraction compiler documenting Cubyz development history.

Source role: GITHUB_REVIEWS (.json, review comments, diffs)

Constraints:
- ZERO EXTRAPOLATION: rely exclusively on explicit statements in the review/diff; never invent motive.
- SUMMARY: summarize the change in 1-2 sentences.
- COMPREHENSIVE_EXPLANATION: focus on bug cause, reviewer concerns, architectural reasoning, regression prevention, refactor motivation, performance, correctness.
- SYMBOLS: extract functions, files, classes, structs, modules, APIs mentioned.
- CONCEPTS: name the high-level engineering concepts at stake (e.g. thread safety, backwards compatibility, memory leak).
- KEYWORDS: generate 5-15 concise technical keywords present in the chunk.
- CHUNK_TYPE: classify using exactly one enum value that best matches the chunk's role (typically "review").
- CODE_EXAMPLE: smallest modified diff portion (<=60 lines); otherwise null.
- SYNTHETIC_QUERIES: generate 6-12 debugging-oriented retrieval questions.

OUTPUT: valid JSON.
""",
    "ADDON_STUDIO": """You are a deterministic data-extraction compiler documenting the Cubyz Addon Creator workspace.

Source role: ADDON_STUDIO_BLUEPRINTS (.js, .html)

Constraints:
- ZERO EXTRAPOLATION: describe only explicit bindings.
- SUMMARY: UI component responsibility in 1-2 sentences.
- COMPREHENSIVE_EXPLANATION: extract UI controls, event handlers, validation, defaults, templates, bindings, engine mappings, configuration generation.
- SYMBOLS: classes, functions, exported objects, UI components, IDs, event handlers.
- CONCEPTS: name the high-level editor/UI concepts the chunk implements (e.g. data-binding, form validation, live preview).
- KEYWORDS: generate 5-15 concise UI/editor keywords.
- CHUNK_TYPE: classify using exactly one enum value that best matches the chunk's role (typically "ui").
- CODE_EXAMPLE: smallest binding/config snippet (<=60 lines); otherwise null.
- SYNTHETIC_QUERIES: generate 6-12 questions about UI behavior, bindings, validation, templates, addon creation, configuration.

OUTPUT: valid JSON.
"""
}

LOW_VRAM_REASONING_RULE = """
Additional constraint for constrained hardware: work in a single deterministic pass. Do not restate these instructions and do not add caveats or meta-commentary. Keep every field as short as the schema allows while remaining accurate, and always fill every required field -- never omit one.
"""

# ============================================================
# FINETUNE MODE -- schema, prompts (from finetune/scripts/FINETUNE_FOLDING.py)
# ============================================================

FINETUNE_SCHEMA = {
    "type": "object",
    "properties": {
        "pairs": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "instruction": {"type": "string"},
                    "response": {"type": "string"},
                },
                "required": ["instruction", "response"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["pairs"],
    "additionalProperties": False,
}

# Shared by docs + codebase: the input record already passed this project's own "zero
# extrapolation" grounding checks during RAG crunching. This prompt's only job is to RESTYLE
# already-validated content into natural training pairs -- a constrained rephrasing task, not a
# fresh-extraction task, which is deliberately safer against hallucination than re-deriving facts
# from raw source a second time.
FINETUNE_RESTYLE_PROMPT = """You are creating fine-tuning training data for a Cubyz voxel-engine assistant. You are given an already-validated, fact-checked knowledge record. Treat every field in the input as ground truth -- your job is ONLY to restyle this content into natural instruction/response training pairs, never to add new facts.

For 3 to 6 of the most genuinely distinct synthetic_queries provided (fewer if the chunk doesn't support that many), write a pair:
- "instruction": the question, phrased as a real developer would naturally ask it in conversation. You may lightly rephrase the synthetic_query for naturalness, but must not change its meaning or add specifics not already implied by it.
- "response": a direct, specific, confident answer in the voice of a helpful, precise Cubyz expert who already knows this -- never phrases like "the retrieved context says" or "according to the documentation."
  - Factual/simple questions: 1-3 sentences, no padding.
  - "how does X work" / mechanism questions: explain the mechanism, then include the code_example verbatim if it's relevant and available.
  - Never state a fact, name, number, or claim that is not explicitly present in the summary, comprehensive_explanation, or code_example you were given.
  - Make sure the response actually answers what its own instruction specifically asks -- not just adjacent or generally-related information from the input.
  - Don't pad a thin or generic answer by appending an unrelated fact from elsewhere in the source just because it's salient (e.g. don't tack "the project also discourages AI-written PRs" onto an answer about memory allocation just because both facts appear somewhere in the same chunk). Every sentence in a response must actually belong to answering that response's own instruction.
  - Don't just restate the instruction's own words back as if that were an answer (e.g. instruction "What happens when X is called during Y?" answered with "During Y, X handles Y-related things"). If you can't add genuinely new, specific detail beyond what the question itself already implies, that question isn't well-supported by this chunk -- pick a different synthetic_query instead.

Before including a pair, check whether you're about to write a hedge like "is not specified", "is not provided", "is not detailed", "is not mentioned", or anything similar (in any verb tense/form -- "are not provided" is just as much a hedge as "is not provided"). If so, that question isn't actually answerable from what you were given -- DROP it entirely and pick a different synthetic_query instead of keeping a pair with a hedge in it. A hedge in the training data is worse than one fewer pair; it teaches the model to give unhelpful non-answers instead of either a real answer or honest silence.

If the input record's own content is too thin, short, or stub-like to support ANY genuinely specific question (e.g. it's just a page title or placeholder with no real body text), output {"pairs": []} entirely rather than inventing generic-sounding questions and answers about the general topic.

The number of pairs must scale with how much genuinely distinct, specific content the input actually contains -- this applies even when the input isn't completely empty. A one- or two-sentence summary supports at most one or two real questions, not three to six. Once you've asked everything the input specifically supports, STOP -- do not keep generating pairs by filling gaps with your own general knowledge of voxel games, Minecraft-like mechanics, or what a system "probably" does. If you notice a candidate answer isn't actually traceable to a specific word or fact in the input you were given, that's fabrication, not restyling -- drop it, even if it sounds plausible.

Do not pad with redundant or speculative pairs just to hit 6 -- fewer genuine pairs is better than inventing marginal ones.

Output strict JSON matching the schema. No markdown, no commentary.
"""

# Reviews get a different, higher-stakes prompt: this is the material that teaches developer
# JUDGMENT, not facts, so grounding discipline matters even more here.
FINETUNE_REVIEWS_PROMPT = """You are creating fine-tuning training data for a Cubyz assistant, teaching it the judgment shown in a real code review. comprehensive_explanation is the ground-truth extracted account of that real diff and review comment -- treat it as reliable, not as something to be suspicious of. Do not invent additional context, a different bug, or advice beyond what it describes.

Generate exactly ONE training pair, choosing whichever shape genuinely fits:

SHAPE A (debugging/diagnosis) -- if this review is about a bug or a "why doesn't this work" issue:
  "instruction": a natural first-person description of hitting this exact problem, as if a developer pasted their own code/situation and asked for help. Paraphrase the symptom comprehensive_explanation describes -- do not invent a different scenario.
  "response": the diagnosis and reasoning, grounded strictly in what comprehensive_explanation says the actual reviewer identified. Write it as direct advice from you -- never "the reviewer said X."

SHAPE B (code review) -- if this review is about a design/style/architecture choice rather than a bug:
  "instruction": "Can you review this approach: [a natural paraphrase of what the original code attempted]"
  "response": constructive review feedback matching the real concern raised, in the voice of a direct, technically precise maintainer. Explain WHY, not just what to change.

Most reviews in this dataset ARE substantial enough to support a pair -- a multi-sentence comprehensive_explanation describing a real function, struct, refactor, or design concern is exactly the kind of content this task is FOR, even though you only have the explanation and not the raw diff text itself. Only output {"pairs": []} when comprehensive_explanation itself is a single short sentence describing a trivial rename, import path change, or line-shortening tweak with no design/correctness reasoning behind it at all. When in doubt between generating and skipping, and the explanation gives you a real mechanism or concern to explain, generate the pair.

Never state a fact, name, or claim not present in comprehensive_explanation, symbols, or concepts -- if you can't ground a specific detail, ground the response in a more general but still-true statement from what IS there rather than reaching for an unstated specific (e.g. don't guess at a renamed identifier's exact new spelling if it isn't given).

Output strict JSON matching the schema. No markdown, no commentary.
"""

AUDIT_SCHEMA = {
    "type": "object",
    "properties": {
        "verdict": {"type": "string", "enum": ["ok", "needs_fix"]},
        "reason": {
            "type": "string",
            "description": "If needs_fix: the specific fact/value/number/name/command in raw_content that kb_content drops, generalizes away, or contradicts. If ok: empty string."
        },
        "corrected_summary": {"type": ["string", "null"]},
        "corrected_explanation": {"type": ["string", "null"]},
        "corrected_related_questions": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["verdict", "reason", "corrected_summary", "corrected_explanation", "corrected_related_questions"],
    "additionalProperties": False,
}

AUDIT_PROMPT = """You are auditing an already-published Cubyz knowledge-base entry against the real source content it was supposedly extracted from. You are NOT extracting a fresh summary -- you are checking whether an EXISTING summary (kb_content) faithfully preserves every concrete, enumerable fact that raw_content actually states.

The single most common real bug found in this knowledge base: kb_content mentions that a topic is COVERED, without ever stating the actual VALUE for it. Concrete confirmed examples from this exact project:
- kb_content said an FAQ "covers... healing mechanics" -- raw_content actually says "there is currently no means to heal." The topic was named; the answer was never given. This is a failure.
- kb_content said "tools can increase damage based on the block type they are specialized for" -- raw_content actually lists exactly which tool damages which material (pickaxe/stone, axe/wood, etc). This is a failure.
- kb_content said "the recipes cover transformations such as converting logs to planks..." -- raw_content actually gives the EXACT recipe (4 planks -> 1 workbench) and kb_content's own related-questions list literally asked "what are the inputs required to craft a workbench?" without ever answering it in the explanation. This is a failure.

What counts as needs_fix:
- A specific number, exact command/config syntax, named value, or enumerated list item that raw_content explicitly states, but kb_content only refers to generically (e.g. "various settings," "several options," "certain requirements") instead of stating the actual value(s).
- A direct question-and-answer pair in raw_content (FAQ-style) where kb_content mentions the question was covered but never states the answer.
- kb_content stating something that directly CONTRADICTS what raw_content says (not just omits -- actively wrong).
- An enumerated list in raw_content (a table, a bullet list, several named items) where kb_content's related_questions ask about specific items from that list but the explanation never actually answers them.

What does NOT count as needs_fix (do not flag these):
- kb_content is more concise than raw_content but still states every concrete value raw_content gives -- brevity alone is not a bug.
- kb_content omits something raw_content itself treats as unimportant framing/narrative (e.g. an introductory sentence, a rhetorical aside) rather than a concrete fact.
- Minor rephrasing that preserves the same specific values.
- raw_content itself doesn't actually contain the fact in question (don't invent a "missing fact" that was never there to begin with -- re-read raw_content carefully before flagging anything).

If you find at least one genuine instance of the pattern above: set verdict to "needs_fix", explain the specific dropped/wrong fact in "reason", and write a corrected_explanation that is comprehensive_explanation, DENSE, and includes every concrete fact/value/number/name/command from raw_content that the current kb_content dropped -- write it as a replacement for the ENTIRE Explanation section, not just an addendum, since it fully replaces the old text. Only include corrected_summary if the Summary section itself is also wrong or misleadingly vague (set to null otherwise). Only include corrected_related_questions if you're adding genuinely new questions the corrected explanation now answers (set to an empty list otherwise, keeping the existing ones).

If kb_content already states every concrete fact raw_content gives (even if worded differently or more concisely): set verdict to "ok", reason to "", and all three correction fields to null/empty.

Never invent a fact that isn't in raw_content. Never flag something as wrong just because it's phrased differently. Output strict JSON matching the given schema, nothing else.
"""

REVIEW_SCHEMA = {
    "type": "object",
    "properties": {
        "verdict": {"type": "string", "enum": ["approve", "reject", "revise"]},
        "feedback": {
            "type": "string",
            "description": "If reject: why the original diagnosis is wrong (the 'issue' isn't real). If revise: specifically what's wrong with the proposed fix and what it still needs. If approve: empty string."
        },
    },
    "required": ["verdict", "feedback"],
    "additionalProperties": False,
}

REVIEW_PROMPT = """You are the SECOND, INDEPENDENT reviewer of a proposed fix to a Cubyz knowledge-base entry. Someone else's LLM already looked at this and proposed a change -- your job is not to redo their work from scratch, it's to check THEIR specific reasoning and THEIR specific fix.

You are given:
- raw_content: the real source the entry is supposed to summarize.
- kb_content: the CURRENT, already-published entry (before any fix).
- proposal_reason: why the proposer thinks kb_content is wrong.
- proposed_explanation (and possibly proposed_summary / proposed_related_questions): their suggested replacement.

Check, in this order:
1. Is the proposer's diagnosis actually real? Re-read raw_content yourself. If kb_content already states the fact the proposer claims is missing (even worded differently), or if raw_content doesn't actually contain what the proposer claims it does, the diagnosis itself is wrong -- verdict "reject", and explain what the proposer got wrong.
2. If the diagnosis IS real: does proposed_explanation actually fix it -- does it now state the specific fact/value/number/name/command that was missing, without fabricating anything not in raw_content? If yes so far, continue to the next check.
3. REGRESSION CHECK (the most important check, and the one most likely to be skipped): compare proposed_explanation against the CURRENT kb_content's Explanation side by side. Does the proposed version drop, generalize away, or contradict ANY fact that kb_content already stated correctly, in the process of fixing the one thing the proposer targeted? A fix that solves one problem while quietly deleting an unrelated fact that was already right is not an improvement -- it's a regression, and should be treated as harshly as leaving the original bug in place. If you find this, verdict "revise" and say exactly which previously-correct fact got dropped and that it must be kept.
4. If the fix passes all three checks: verdict "approve", feedback "".
5. If the diagnosis is real but the fix has smaller issues (unclear wording, a fact stated but not precisely enough, minor omissions) that don't rise to a full regression: verdict "revise" with specific, actionable feedback on what to change.

Be genuinely skeptical -- your entire purpose is to catch a fix that looks plausible but is wrong, incomplete, or introduces a new problem, not to rubber-stamp the first plausible-sounding thing you're shown. Output strict JSON matching the given schema, nothing else.
"""

def format_chunk_descriptor(task: dict) -> str:
    # GITHUB_REVIEWS tasks don't have a real sequential chunk_index -- each review comment stands
    # alone with no natural position within the file it touches, so the source dataset reuses
    # chunk_index to carry the comment's own (huge, unique) numeric ID instead. Displayed as
    # "Chunk 3295308100" that looks like a bug rather than what it actually is. Issue-discussion
    # chunks (from extract_issues.py) reuse the same GITHUB_REVIEWS category with chunk_index set
    # to the actual issue number, so they get their own equally-readable case.
    match = re.match(r'github_pr_(\d+)_comment_\d+', task.get("chunk_id", ""))
    if match:
        return f"PR #{match.group(1)} review diff"
    match = re.match(r'github_issue_(\d+)_discussion', task.get("chunk_id", ""))
    if match:
        return f"Issue #{match.group(1)} discussion"
    return f"Chunk {task['chunk_index']}"

def format_current_task_line(task: dict) -> str:
    # raw_content for a GITHUB_REVIEWS task is a git diff plus its reviewer comment, pulled from a
    # real PR -- relative_path only names the diff's target file, it is NOT that file's own source
    # being processed. A filename-first line reads exactly like "processing this file's code",
    # which is wrong, so lead with the diff/PR framing instead to make the distinction obvious.
    # Issue-discussion chunks have no target file at all (relative_path is a synthetic
    # issues/issue_N.md path), so they get their own framing rather than the misleading
    # "touching issues/issue_N.md" phrasing that would otherwise result.
    match = re.match(r'github_pr_(\d+)_comment_\d+', task.get("chunk_id", ""))
    if match:
        return f"GitHub PR #{match.group(1)} review diff, touching {task['relative_path']} ({task['lines']} lines)"
    match = re.match(r'github_issue_(\d+)_discussion', task.get("chunk_id", ""))
    if match:
        return f"GitHub Issue #{match.group(1)} discussion ({task['lines']} lines)"
    return f"{task['relative_path']} ({format_chunk_descriptor(task)} • {task['lines']} lines)"

def format_finetune_task_line(task: dict) -> str:
    record = task.get("record") or {}
    title = record.get("title")
    label = f'"{title}"' if title else task.get("chunk_id", "?")
    return f"[{task.get('source_type', '?')}] {label}"


def _find_anchor_index(line: str, raw_content: str):
    line = line.strip()
    if not line:
        return None
    tokens = line.split()
    if not tokens:
        return None
    pattern = r'\s+'.join(re.escape(t) for t in tokens)
    match = re.search(pattern, raw_content)
    return match.start() if match else None

def _skip_balanced(raw_content: str, open_pos: int, open_char: str, close_char: str):
    depth = 0
    i = open_pos
    while i < len(raw_content):
        if raw_content[i] == open_char:
            depth += 1
        elif raw_content[i] == close_char:
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return None

def _find_declaration_body_brace(raw_content: str, decl_start: int):
    paren_pos = raw_content.find('(', decl_start)
    brace_pos = raw_content.find('{', decl_start)
    if paren_pos != -1 and (brace_pos == -1 or paren_pos < brace_pos):
        after_params = _skip_balanced(raw_content, paren_pos, '(', ')')
        if after_params is None:
            return None
        tail = raw_content[after_params:]
        error_set = re.match(r'[^{;]*?error\s*\{[^{}]*\}', tail)
        search_from = after_params + error_set.end() if error_set else after_params
        return raw_content.find('{', search_from)
    return brace_pos if brace_pos != -1 else None

def repair_code_example(candidate_code, raw_content):
    if not isinstance(candidate_code, str) or not candidate_code.strip():
        return None

    lines = [l for l in candidate_code.splitlines() if l.strip()]
    if not lines:
        return None
    first_line = lines[0]

    anchor_idx = _find_anchor_index(first_line, raw_content)

    if anchor_idx is None:
        name_match = re.search(r'\b(?:fn|struct|enum|union)\s+(\w+)', first_line)
        if name_match:
            name = name_match.group(1)
            decl_match = re.search(rf'\b(?:pub\s+)?(?:fn|const)\s+{re.escape(name)}\b', raw_content)
            if decl_match:
                anchor_idx = decl_match.start()

    if anchor_idx is None:
        return None

    brace_start = _find_declaration_body_brace(raw_content, anchor_idx)
    if brace_start is None or brace_start == -1:
        return None

    # If the model's anchor text isn't actually a declaration signature (e.g. it picked a bare
    # statement instead of a function/struct/enum), the brace found above could belong to a
    # completely unrelated, later block. A genuine signature never contains a statement
    # terminator before its own opening brace, so treat one as a sign this anchor can't be
    # repaired this way -- find_shortest_declaration() is the fallback for that case instead.
    if ';' in raw_content[anchor_idx:brace_start]:
        return None

    depth = 0
    for i in range(brace_start, len(raw_content)):
        if raw_content[i] == '{':
            depth += 1
        elif raw_content[i] == '}':
            depth -= 1
            if depth == 0:
                return raw_content[anchor_idx:i + 1]
    return None

def find_shortest_declaration(raw_content: str):
    # Mirrors the prompt's own "shortest complete function/struct/enum/union, fewest lines wins"
    # procedure, but run deterministically in code as a fallback for when the model's own
    # code_example wasn't declaration-shaped at all (e.g. it picked a bare local-variable
    # statement) and so can't be anchored/repaired from. Correctly returns None -- not a wrong
    # guess -- when no declaration in this specific chunk has a complete body within it (e.g. a
    # long function whose body is cut off by the chunk boundary).
    candidates = []
    pattern = r'\b(?:pub\s+)?(?:fn\s+\w+\s*\(|(?:const|var)\s+\w+\s*(?::[^=;{}]*)?=\s*(?:struct|enum|union)\b)'
    for match in re.finditer(pattern, raw_content):
        brace_start = _find_declaration_body_brace(raw_content, match.start())
        if brace_start is None or brace_start == -1:
            continue
        depth = 0
        end = None
        for i in range(brace_start, len(raw_content)):
            if raw_content[i] == '{':
                depth += 1
            elif raw_content[i] == '}':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end is not None:
            candidates.append(raw_content[match.start():end])
    if not candidates:
        return None
    return min(candidates, key=lambda c: c.count('\n'))

def sanitize_extraction(data: dict, raw_content: str, p_key: str = "CODEBASE") -> dict:
    code_example = data.get("code_example")
    if isinstance(code_example, str) and code_example.strip():
        normalized_raw = re.sub(r'\s+', ' ', raw_content)
        normalized_example = re.sub(r'\s+', ' ', code_example)
        has_ellipsis = "..." in code_example or "…" in code_example
        is_verbatim = normalized_example in normalized_raw
        looks_like_declaration = bool(re.search(r'\b(fn|struct|enum|union)\b', code_example))
        balanced_braces = code_example.count('{') == code_example.count('}')

        needs_repair = has_ellipsis or not is_verbatim
        if p_key == "CODEBASE":
            needs_repair = needs_repair or not looks_like_declaration or not balanced_braces

        if needs_repair:
            repaired = repair_code_example(code_example, raw_content)
            if repaired is None and p_key == "CODEBASE":
                repaired = find_shortest_declaration(raw_content)
            data["code_example"] = repaired

    if isinstance(data.get("symbols"), list):
        private_imports = set(re.findall(r'(?m)^[ \t]*const\s+(\w+)\s*=\s*@import\(', raw_content))
        data["symbols"] = [s for s in data["symbols"] if s not in private_imports]

        public_reexports = re.findall(r'(?m)^[ \t]*pub\s+const\s+(\w+)\s*=\s*@import\(', raw_content)
        for name in public_reexports:
            if name not in data["symbols"]:
                data["symbols"].append(name)

    for list_field in ("symbols", "concepts", "keywords", "synthetic_queries"):
        if isinstance(data.get(list_field), list):
            data[list_field] = list(dict.fromkeys(data[list_field]))

    if len(raw_content) < 400 and isinstance(data.get("synthetic_queries"), list):
        data["synthetic_queries"] = data["synthetic_queries"][:6]

    return data

# The WIKI prompt already tells the model not to do this (see RAG_PROMPTS["WIKI"]'s "VERBATIM FACT
# PRESERVATION" rule, with this exact healing example baked in) -- but that's a request, not an
# enforcement, and it demonstrably doesn't always work: a live knowledge_base/docs/docs_docs_faq.md
# chunk was found (2026-07-18, during RAG debugging) doing precisely this on the live FAQ source,
# with the effect confirmed against real webapp/local_rag_chat.py runs -- "Can the player heal?"
# answered "Yes" because the chunk's Explanation only said the FAQ "covers... healing mechanics"
# instead of restating the source's actual "there is currently no means to heal." CODEBASE chunks
# get a real verbatim check on code_example (below); WIKI chunks had no code-level check at all for
# the equivalent failure on prose facts. This is a narrow, source-comparison heuristic for exactly
# that shape of bug -- not a general fact-checker -- so it only fires when all of these hold: (1)
# raw_content has a markdown "## question?" heading followed by a short (<=40 word) answer, (2)
# that answer contains an explicit negation word, (3) the explanation clearly discusses the same
# topic (shares a keyword with the question), and (4) no negation word appears anywhere in the
# explanation at all. That combination is what a dropped yes/no fact looks like; it won't fire on
# longer/discursive answers or topics the model never mentions at all (those are already caught by
# the existing "doesn't answer" behavior, not this bug).
_FAQ_QA_PATTERN = re.compile(r'(?m)^#{1,6}\s*(.+?\??)\s*$\n+(.*?)(?=\n#{1,6}\s|\Z)', re.S)
_NEGATION_WORDS = {"no", "not", "cannot", "can't", "isn't", "doesn't", "don't", "never", "none", "nothing", "n't"}
_STOPWORDS = {"the", "and", "for", "are", "you", "your", "with", "this", "that", "how", "what",
              "does", "will", "can", "there", "way", "currently", "right", "now"}


def check_wiki_faq_grounding(data: dict, raw_content: str) -> tuple:
    explanation = (data.get("comprehensive_explanation") or "").lower()
    if not explanation:
        return True, ""

    for question, answer in _FAQ_QA_PATTERN.findall(raw_content):
        question = question.strip()
        if not question.endswith("?"):
            continue
        answer_clean = " ".join(answer.split())
        if not answer_clean or len(answer_clean.split()) > 40:
            continue  # only short, single-fact FAQ-style answers -- not general prose
        answer_words = set(re.findall(r"[a-z']+", answer_clean.lower()))
        if not (answer_words & _NEGATION_WORDS):
            continue  # this particular Q&A isn't a negation-shaped fact
        q_keywords = {w for w in re.findall(r"[a-z']+", question.lower())
                      if len(w) >= 4 and w not in _STOPWORDS}
        if not q_keywords:
            continue

        # A negation word appearing SOMEWHERE in a multi-topic explanation doesn't mean THIS
        # topic's negation was preserved -- a dense, comma-separated topic list (exactly the shape
        # a condensed FAQ explanation tends to take) packs unrelated topics within a fixed
        # character window of each other, so a character-radius check falsely "found" an unrelated
        # neighboring negation (confirmed live: "...doesn't start, healing mechanics, eating..." --
        # the "doesn't" belongs to the previous topic, not healing). Splitting on clause boundaries
        # (,;.) and requiring the topic keyword and a negation to land in the SAME clause fixes
        # that false-negative while still catching the real bug, where the negation is missing
        # from the sentence/clause that actually discusses this topic (substring match on the
        # keyword since "heal"/"healing" share a root but aren't the same token).
        clauses = re.split(r"[,;.]", explanation)
        found_topic, found_negation_nearby = False, False
        for clause in clauses:
            clause_words = set(re.findall(r"[a-z']+", clause))
            if any(qk in w or w in qk for qk in q_keywords for w in clause_words if len(w) >= 4):
                found_topic = True
                if clause_words & _NEGATION_WORDS:
                    found_negation_nearby = True
                    break
        if found_topic and not found_negation_nearby:
            return False, (f"source Q&A {question!r} answers with a negation "
                            f"('no'/'cannot'/etc.) but comprehensive_explanation mentions the same "
                            f"topic without stating that negation nearby -- likely dropped the "
                            f"actual answer the way the FAQ healing bug did")
    return True, ""


def validate_extraction(data: dict, raw_content: str, p_key: str) -> tuple:

    if p_key == "WIKI":
        ok, reason = check_wiki_faq_grounding(data, raw_content)
        if not ok:
            return False, reason

    code_example = data.get("code_example")
    if isinstance(code_example, str) and code_example.strip():
        normalized_raw = re.sub(r'\s+', ' ', raw_content)
        normalized_example = re.sub(r'\s+', ' ', code_example)
        if normalized_example not in normalized_raw:
            return False, "code_example is not a verbatim substring of raw_content"
        if p_key == "CODEBASE":
            if not re.search(r'\b(fn|struct|enum|union)\b', code_example):
                return False, "code_example doesn't look like a function/struct/enum body"
            if code_example.count('{') != code_example.count('}'):
                return False, "code_example has unbalanced braces (likely an incomplete snippet)"

    symbols = data.get("symbols")
    if isinstance(symbols, list) and symbols and p_key == "CODEBASE":
        symbol_set = set(symbols)
        # "." shows up in plenty of non-qualification text too (version numbers like "OpenGL
        # 4.3", decimals, etc.) -- a real Zig Parent.child reference is always a single
        # contiguous identifier with no spaces, so require that to avoid false positives. Also
        # require every dot-separated segment to actually look like a Zig identifier (starts with
        # a letter/underscore, no leading digit or "@" -- "@" is reserved for real builtins like
        # @import, never a user identifier). Without this, something like "@lod0.5Distance" --
        # the model mashing together a value ("lod0"), a number ("0.5"), and a field name
        # ("Distance") into one garbled string -- gets treated as a genuine qualified reference
        # and then rejected as an unfounded "call-chain," when it was never a real symbol at all.
        qualified = [
            s for s in symbols
            if "." in s and " " not in s
            and all(re.match(r'^[A-Za-z_]\w*$', part) for part in s.split("."))
        ]
        if qualified:
            # A qualified symbol's root being absent from the model's own reported symbol list
            # doesn't mean it's fabricated -- orchestration/entry-point code (main.zig's entry
            # point, in particular) is naturally full of calls into imported modules
            # (heap.allocators.deinit, std.log.err) whose root is an import alias the chunk
            # uses, not something the chunk itself declares. Requiring "the root is ALSO in
            # symbol_set" made every genuinely call-heavy chunk fail every single attempt
            # forever (confirmed live: codebase_src_main.zig_chunk_3 hit this 191 times across
            # the diagnostic log before ever being traced to this check). What actually matters
            # is grounding -- does the root token appear anywhere in the chunk's real source at
            # all? A genuinely fabricated dotted reference wouldn't.
            orphaned = [
                s for s in qualified
                if s.split(".")[0] not in symbol_set
                and not re.search(r'\b' + re.escape(s.split(".")[0]) + r'\b', raw_content)
            ]
            if len(orphaned) / len(qualified) > 0.5:
                return False, f"most qualified symbols look like call-chains, not declarations (e.g. {orphaned[0]!r})"

    text_fields = " ".join([
        data.get("summary", "") or "",
        data.get("comprehensive_explanation", "") or "",
        " ".join(data.get("synthetic_queries", []) or []),
    ])
    for name in set(re.findall(r'`([A-Za-z_][A-Za-z0-9_]*)`', text_fields)):
        if not re.search(r'\b' + re.escape(name) + r'\b', raw_content):
            return False, f"'{name}' is quoted as an identifier but doesn't appear in raw_content"

    if not data.get("summary") or not data.get("comprehensive_explanation"):
        return False, "summary or comprehensive_explanation is empty"

    return True, ""


def generate_rag_analysis(task: dict, chosen_model: str, max_threads, status_cb, force_cpu: bool = False) -> tuple:
    raw_content = task.get("raw_content", "")
    ctx_upper = task.get("directory_context", "").upper()
    if "DEFINITIVE_WIKI_DOCUMENTATION" in ctx_upper or "WIKI" in ctx_upper:
        p_key, temp = "WIKI", 0.30
    elif "GITHUB_REVIEWS" in ctx_upper or "REVIEW" in ctx_upper:
        p_key, temp = "GITHUB_REVIEWS", 0.20
    elif "ADDON_STUDIO" in ctx_upper or "ADDON" in ctx_upper:
        p_key, temp = "ADDON_STUDIO", 0.20
    else:
        p_key, temp = "CODEBASE", 0.15

    payload = {
        "model": chosen_model,
        "prompt": f"Context Source File: {task['file_name']}\nRelative Path: {task['relative_path']}\nDirectory Module context: {task['directory_context']}\nChunk Index: {task['chunk_index']}\nRaw Content:\n```\n{raw_content}\n```\n",
        "system": RAG_PROMPTS[p_key] + (LOW_VRAM_REASONING_RULE if chosen_model in ["qwen2.5-coder:3b"] else ""),
        "think": False,
        "stream": False, "format": RAG_JSON_SCHEMA, "options": {
            "temperature": temp,
            **({"num_thread": max_threads} if max_threads else {}),
            # num_gpu=0 tells Ollama to keep every layer on the CPU for this request specifically,
            # regardless of what a concurrent GPU-backed request from the other lane is doing --
            # this is what lets one machine run a GPU lane and a CPU lane against the same Ollama
            # server at once (see run_dual_lane_if_capable()) without them fighting over VRAM.
            **({"num_gpu": 0} if force_cpu else {}),
        }
    }

    # Diagnostic logging here is deliberately scoped to retries/failures only -- a chunk that
    # succeeds on attempt 1 (the normal case) logs nothing at all. The point is "why did this
    # chunk need to be redone," not a full audit trail of routine work.
    #
    # `extra` carries whatever's actually available at each failure point -- the raw unparsed
    # model output on a JSON parse error, or the parsed-but-rejected candidate dict on a
    # self-check failure -- so a later investigation doesn't have to re-simulate the exact
    # request just to see what the model actually produced (this gap is exactly what made
    # diagnosing the "code_example doesn't look like a function/struct/enum body" failures slow
    # to trace live). Capped in size since some raw model output can be large.
    def _log_retry(attempt_num, reason, extra=None):
        event = {
            "event": "task_retry", "mode": "rag", "chunk_id": task.get("chunk_id"),
            "attempt": attempt_num + 1, "reason": reason,
        }
        if extra:
            event.update({k: (v[:2000] if isinstance(v, str) else v) for k, v in extra.items()})
        log_diagnostic(event)

    parsed_data = None
    last_failure_reason = "no attempts made"
    for attempt in range(3):
        if attempt > 0:
            time.sleep(5)

        payload["options"]["temperature"] = temp + (attempt * 0.15)

        try:
            res = make_request(OLLAMA_URL, payload)
            json_string = res.get("response", "").strip()
        except Exception as e:
            last_failure_reason = f"{type(e).__name__}: {e}"
            status_cb(f"⚠ Attempt {attempt+1} failed: {last_failure_reason}")
            _log_retry(attempt, last_failure_reason)
            continue

        if not json_string:
            last_failure_reason = "Ollama returned HTTP 200 with an empty 'response' field"
            status_cb(f"⚠ Attempt {attempt+1}: model returned empty output. Retrying...")
            _log_retry(attempt, last_failure_reason)
            continue

        if json_string.startswith("```"):
            lines = json_string.splitlines()
            if lines and lines[0].startswith("```"): lines = lines[1:]
            if lines and lines[-1].startswith("```"): lines = lines[:-1]
            json_string = "\n".join(lines).strip()
        try:
            candidate = json.loads(json_string[json_string.find("{"):json_string.rfind("}")+1] if "{" in json_string else json_string)
        except Exception as e:
            last_failure_reason = f"JSON parse error: {e}"
            status_cb(f"⚠ Attempt {attempt+1}: {last_failure_reason}. Retrying...")
            _log_retry(attempt, last_failure_reason, {"raw_response": json_string})
            continue

        candidate = sanitize_extraction(candidate, raw_content, p_key)

        is_valid, validation_reason = validate_extraction(candidate, raw_content, p_key)
        if is_valid:
            parsed_data = candidate
            break
        last_failure_reason = f"Self-check failed: {validation_reason}"
        status_cb(f"⚠ Attempt {attempt+1}: {last_failure_reason}. Retrying...")
        _log_retry(attempt, last_failure_reason, {"candidate": candidate})

    if parsed_data is None:
        gave_up_event = {
            "event": "task_gave_up", "mode": "rag", "chunk_id": task.get("chunk_id"),
            "final_reason": last_failure_reason,
        }
        log_diagnostic(gave_up_event)
        submit_diagnostic_to_server(gave_up_event)

    return parsed_data, last_failure_reason

def generate_audit_analysis(task: dict, chosen_model: str, status_cb, force_cpu: bool = False) -> tuple:
    raw_content = task.get("raw_content", "")
    kb_content = task.get("kb_content", "")

    prompt_text = f"raw_content (the real source):\n```\n{raw_content}\n```\n\nkb_content (the existing knowledge-base entry to audit):\n```\n{kb_content}\n```\n"
    system_text = AUDIT_PROMPT
    if task.get("task_type") == "revise":
        # A reviewer already confirmed a real issue exists here (see task["proposal_reason"]) and
        # rejected the SPECIFIC fix below for a SPECIFIC reason (task["review_feedback"]) -- this
        # is not a fresh audit, it's fixing a fix. Producing another generic "covers X" non-answer
        # would just repeat the exact failure this whole system exists to catch, one level deeper.
        prompt_text += (
            f"\nA previous attempt to fix this diagnosed issue was reviewed and rejected as inadequate:\n"
            f"Diagnosed issue: {task.get('proposal_reason', '')}\n"
            f"Previously proposed (rejected) explanation:\n```\n{task.get('proposed_explanation', '')}\n```\n"
            f"Reviewer's specific feedback on why that fix wasn't good enough:\n{task.get('review_feedback', '')}\n\n"
            f"Write a genuinely improved corrected_explanation that addresses the reviewer's specific feedback -- "
            f"don't just resubmit something similar to the rejected version. Set verdict to \"needs_fix\" "
            f"(the issue is already confirmed real; your job now is only to produce a better fix for it)."
        )

    payload = {
        "model": chosen_model,
        "prompt": prompt_text,
        "system": system_text,
        "think": False,
        "stream": False, "format": AUDIT_SCHEMA,
        "options": {
            "temperature": 0.1,  # low but nonzero -- this is a judgment call (does X count as "dropped"?), not pure extraction
            **({"num_gpu": 0} if force_cpu else {}),
        }
    }

    def _log_retry(attempt_num, reason, extra=None):
        event = {
            "event": "task_retry", "mode": "audit", "chunk_id": task.get("chunk_id"),
            "attempt": attempt_num + 1, "reason": reason,
        }
        if extra:
            event.update({k: (v[:2000] if isinstance(v, str) else v) for k, v in extra.items()})
        log_diagnostic(event)

    parsed_data = None
    last_failure_reason = "no attempts made"
    for attempt in range(3):
        if attempt > 0:
            time.sleep(5)
        payload["options"]["temperature"] = 0.1 + (attempt * 0.1)

        try:
            res = make_request(OLLAMA_URL, payload)
            json_string = res.get("response", "").strip()
        except Exception as e:
            last_failure_reason = f"{type(e).__name__}: {e}"
            status_cb(f"⚠ Attempt {attempt+1} failed: {last_failure_reason}")
            _log_retry(attempt, last_failure_reason)
            continue

        if not json_string:
            last_failure_reason = "Ollama returned HTTP 200 with an empty 'response' field"
            status_cb(f"⚠ Attempt {attempt+1}: model returned empty output. Retrying...")
            _log_retry(attempt, last_failure_reason)
            continue

        if json_string.startswith("```"):
            lines = json_string.splitlines()
            if lines and lines[0].startswith("```"): lines = lines[1:]
            if lines and lines[-1].startswith("```"): lines = lines[:-1]
            json_string = "\n".join(lines).strip()

        try:
            candidate = json.loads(json_string[json_string.find("{"):json_string.rfind("}")+1] if "{" in json_string else json_string)
        except Exception as e:
            last_failure_reason = f"JSON parse error: {e}"
            status_cb(f"⚠ Attempt {attempt+1}: {last_failure_reason}. Retrying...")
            _log_retry(attempt, last_failure_reason, {"raw_response": json_string})
            continue

        # Self-check, same spirit as validate_extraction() for RAG mode: a "needs_fix" verdict
        # must actually justify itself -- if the model says something's wrong but its own
        # corrected_explanation is empty, or if it claims a fact is missing that provably IS in
        # kb_content already (crude substring-overlap heuristic, not exhaustive), reject and retry
        # rather than silently forwarding a self-contradictory audit result to the server.
        if candidate.get("verdict") == "needs_fix" and not (candidate.get("corrected_explanation") or "").strip():
            last_failure_reason = "Self-check failed: verdict is needs_fix but corrected_explanation is empty"
            status_cb(f"⚠ Attempt {attempt+1}: {last_failure_reason}. Retrying...")
            _log_retry(attempt, last_failure_reason, {"candidate": candidate})
            continue

        parsed_data = candidate
        break

    if parsed_data is None:
        gave_up_event = {
            "event": "task_gave_up", "mode": "audit", "chunk_id": task.get("chunk_id"),
            "final_reason": last_failure_reason,
        }
        log_diagnostic(gave_up_event)
        submit_diagnostic_to_server(gave_up_event)

    return parsed_data, last_failure_reason

def generate_audit_review(task: dict, chosen_model: str, status_cb, force_cpu: bool = False) -> tuple:
    prompt_text = (
        f"raw_content (the real source):\n```\n{task.get('raw_content', '')}\n```\n\n"
        f"kb_content (CURRENT published entry, before any fix):\n```\n{task.get('kb_content', '')}\n```\n\n"
        f"proposal_reason (why the proposer flagged this):\n{task.get('proposal_reason', '')}\n\n"
        f"proposed_explanation (their suggested replacement):\n```\n{task.get('proposed_explanation', '')}\n```\n"
    )
    if task.get("proposed_summary"):
        prompt_text += f"\nproposed_summary:\n```\n{task['proposed_summary']}\n```\n"
    if task.get("proposed_related_questions"):
        prompt_text += f"\nproposed_related_questions: {task['proposed_related_questions']}\n"

    payload = {
        "model": chosen_model,
        "prompt": prompt_text,
        "system": REVIEW_PROMPT,
        "think": False,
        "stream": False, "format": REVIEW_SCHEMA,
        "options": {
            "temperature": 0.1,
            **({"num_gpu": 0} if force_cpu else {}),
        }
    }

    def _log_retry(attempt_num, reason, extra=None):
        event = {
            "event": "task_retry", "mode": "audit_review", "chunk_id": task.get("chunk_id"),
            "attempt": attempt_num + 1, "reason": reason,
        }
        if extra:
            event.update({k: (v[:2000] if isinstance(v, str) else v) for k, v in extra.items()})
        log_diagnostic(event)

    parsed_data = None
    last_failure_reason = "no attempts made"
    for attempt in range(3):
        if attempt > 0:
            time.sleep(5)
        payload["options"]["temperature"] = 0.1 + (attempt * 0.1)

        try:
            res = make_request(OLLAMA_URL, payload)
            json_string = res.get("response", "").strip()
        except Exception as e:
            last_failure_reason = f"{type(e).__name__}: {e}"
            status_cb(f"⚠ Attempt {attempt+1} failed: {last_failure_reason}")
            _log_retry(attempt, last_failure_reason)
            continue

        if not json_string:
            last_failure_reason = "Ollama returned HTTP 200 with an empty 'response' field"
            status_cb(f"⚠ Attempt {attempt+1}: model returned empty output. Retrying...")
            _log_retry(attempt, last_failure_reason)
            continue

        if json_string.startswith("```"):
            lines = json_string.splitlines()
            if lines and lines[0].startswith("```"): lines = lines[1:]
            if lines and lines[-1].startswith("```"): lines = lines[:-1]
            json_string = "\n".join(lines).strip()

        try:
            candidate = json.loads(json_string[json_string.find("{"):json_string.rfind("}")+1] if "{" in json_string else json_string)
        except Exception as e:
            last_failure_reason = f"JSON parse error: {e}"
            status_cb(f"⚠ Attempt {attempt+1}: {last_failure_reason}. Retrying...")
            _log_retry(attempt, last_failure_reason, {"raw_response": json_string})
            continue

        if candidate.get("verdict") in ("reject", "revise") and not (candidate.get("feedback") or "").strip():
            last_failure_reason = f"Self-check failed: verdict is {candidate.get('verdict')} but feedback is empty"
            status_cb(f"⚠ Attempt {attempt+1}: {last_failure_reason}. Retrying...")
            _log_retry(attempt, last_failure_reason, {"candidate": candidate})
            continue

        parsed_data = candidate
        break

    if parsed_data is None:
        gave_up_event = {
            "event": "task_gave_up", "mode": "audit_review", "chunk_id": task.get("chunk_id"),
            "final_reason": last_failure_reason,
        }
        log_diagnostic(gave_up_event)
        submit_diagnostic_to_server(gave_up_event)

    return parsed_data, last_failure_reason

def build_prompt_input(task: dict) -> str:
    record = task["record"]
    source_type = task["source_type"]
    if source_type == "reviews":
        # No raw_content field actually exists in the crunched review records (the RAG campaign
        # never preserved the literal diff text) -- presenting a fake empty "raw_content" block
        # here was misleading, so comprehensive_explanation is presented directly as the ground
        # truth instead of implying there's a raw diff backing it that the model isn't seeing.
        return (
            f"comprehensive_explanation (ground truth, extracted from the real diff/review):\n{record.get('comprehensive_explanation', '')}\n\n"
            f"summary: {record.get('summary', '')}\n"
            f"symbols: {record.get('symbols', [])}\n"
            f"concepts: {record.get('concepts', [])}\n"
        )
    return (
        f"title: {record.get('title', '')}\n"
        f"summary: {record.get('summary', '')}\n"
        f"comprehensive_explanation: {record.get('comprehensive_explanation', '')}\n"
        f"code_example: {record.get('code_example') or 'null'}\n"
        f"symbols: {record.get('symbols', [])}\n"
        f"concepts: {record.get('concepts', [])}\n"
        f"synthetic_queries: {record.get('synthetic_queries', [])}\n"
    )

def grounding_text_for(task: dict) -> str:
    record = task["record"]
    if task["source_type"] == "reviews":
        symbols_text = " ".join(record.get("symbols") or [])
        return f"{record.get('comprehensive_explanation', '')} {symbols_text}"
    symbols_text = " ".join(record.get("symbols") or [])
    return f"{record.get('summary', '')} {record.get('comprehensive_explanation', '')} {record.get('code_example') or ''} {symbols_text}"

def validate_pairs(pairs, grounding_text: str) -> tuple:
    if not isinstance(pairs, list):
        return False, "pairs is not a list"
    for pair in pairs:
        if not isinstance(pair, dict) or "instruction" not in pair or "response" not in pair:
            return False, "malformed pair"
        for name in set(re.findall(r'`([A-Za-z_][A-Za-z0-9_]*)`', pair["response"])):
            if not re.search(r'\b' + re.escape(name) + r'\b', grounding_text):
                return False, f"'{name}' quoted in response but not found in source grounding text"
    return True, ""

def generate_finetune_pairs(task: dict, chosen_model: str, status_cb, force_cpu: bool = False) -> tuple:
    source_type = task["source_type"]
    prompt_text = FINETUNE_RESTYLE_PROMPT if source_type in ("docs", "codebase") else FINETUNE_REVIEWS_PROMPT
    payload = {
        "model": chosen_model,
        "prompt": build_prompt_input(task),
        "system": prompt_text,
        "think": False,
        "stream": False,
        "format": FINETUNE_SCHEMA,
        "options": {"temperature": 0.3, **({"num_gpu": 0} if force_cpu else {})},
    }

    # Same scoping as generate_rag_analysis's _log_retry -- only retries/failures get logged, a
    # clean first-attempt success logs nothing. `extra` captures whatever's actually available at
    # each failure point (see generate_rag_analysis's _log_retry for the full reasoning).
    def _log_retry(attempt_num, reason, extra=None):
        event = {
            "event": "task_retry", "mode": "finetune", "chunk_id": task.get("chunk_id"),
            "attempt": attempt_num + 1, "reason": reason,
        }
        if extra:
            event.update({k: (v[:2000] if isinstance(v, str) else v) for k, v in extra.items()})
        log_diagnostic(event)

    grounding_text = grounding_text_for(task)
    parsed = None
    last_failure = "no attempts made"
    for attempt in range(3):
        if attempt > 0:
            time.sleep(3)
        try:
            res = make_request(OLLAMA_URL, payload)
            raw = res.get("response", "").strip()
        except Exception as e:
            last_failure = f"{type(e).__name__}: {e}"
            status_cb(f"⚠ Attempt {attempt+1} failed: {last_failure}")
            _log_retry(attempt, last_failure)
            continue
        if raw.startswith("```"):
            lines = raw.splitlines()
            if lines and lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].startswith("```"):
                lines = lines[:-1]
            raw = "\n".join(lines).strip()
        try:
            candidate = json.loads(raw[raw.find("{"):raw.rfind("}") + 1] if "{" in raw else raw)
        except Exception as e:
            last_failure = f"JSON parse error: {e}"
            status_cb(f"⚠ Attempt {attempt+1}: {last_failure}. Retrying...")
            _log_retry(attempt, last_failure, {"raw_response": raw})
            continue

        ok, reason = validate_pairs(candidate.get("pairs", []), grounding_text)
        if ok:
            parsed = candidate
            break
        last_failure = f"Self-check failed: {reason}"
        status_cb(f"⚠ Attempt {attempt+1}: {last_failure}. Retrying...")
        _log_retry(attempt, last_failure, {"candidate": candidate})

    if parsed is None:
        gave_up_event = {
            "event": "task_gave_up", "mode": "finetune", "chunk_id": task.get("chunk_id"),
            "final_reason": last_failure,
        }
        log_diagnostic(gave_up_event)
        submit_diagnostic_to_server(gave_up_event)

    return parsed, last_failure

MODE_BANNERS = {
    "rag": f"{Colors.CYAN}{Colors.BOLD}★ RAG MODE ACTIVATED -- receiving knowledge-extraction tasks{Colors.RESET}",
    "finetune": f"{Colors.MAGENTA}{Colors.BOLD}★ FINETUNE MODE ACTIVATED -- receiving training-pair generation tasks{Colors.RESET}",
    "audit": f"{Colors.YELLOW}{Colors.BOLD}★ AUDIT MODE ACTIVATED -- checking existing knowledge_base entries against their source{Colors.RESET}",
}

# -- TUI status board (replaces DualStatusBoard) -------------------------------
class TuiStatusBoard:
    """Thread-safe board that writes into _lane_state for the TUI to render."""

    LANE_COLORS = ["\033[96m", "\033[95m", "\033[93m", "\033[94m", "\033[92m", "\033[91m"]

    def __init__(self):
        self._lock = threading.Lock()

    def set_label(self, lane_tag: str, label: str):
        with _lane_lock:
            if lane_tag not in _lane_order:
                _lane_order.append(lane_tag)
            _lane_state.setdefault(lane_tag, {
                "label": label, "task": "(waiting for a task...)",
                "status": "Starting...", "speed": "calculating...",
            })
            _lane_state[lane_tag]["label"] = label

    def drop_lane(self, lane_tag: str):
        with _lane_lock:
            if lane_tag in _lane_order:
                _lane_order.remove(lane_tag)
            _lane_state.pop(lane_tag, None)

    def should_announce_mode(self, mode: str) -> bool:
        return False

    def update(self, lane_tag: str, task_desc: str, step_msg: str,
               comp: int, tot: int, eta, speed: str):
        with _lane_lock:
            if lane_tag not in _lane_order:
                _lane_order.append(lane_tag)
            _lane_state.setdefault(lane_tag, {})
            _lane_state[lane_tag].update({"task": task_desc, "status": step_msg, "speed": speed})
        with _progress_lock:
            _global_progress["comp"] = comp
            _global_progress["tot"]  = tot
            _global_progress["eta"]  = eta

    def note(self, msg: str):
        _log_queue.append(msg)

    def rendered_once(self):
        return True


def interruptible_sleep(seconds: float, dual_controller=None, parallel_controller=None, has_gpu=False, stop_event=None):
    end = time.time() + seconds
    while time.time() < end:
        if stop_event is not None and stop_event.is_set():
            break
        time.sleep(0.5)

def crunch_lane(lane_tag: str, user_id: str, hardware_tier: str, chosen_model: str, max_threads,
                 cooldown: float, mode_desc: str, hardware_label: str, force_cpu: bool = False,
                 fancy_ui: bool = True, pause_event: "threading.Event | None" = None,
                 board: "DualStatusBoard | None" = None, stop_event: "threading.Event | None" = None,
                 dual_controller: "DualLaneController | None" = None,
                 parallel_controller: "ParallelWorkerPoolController | None" = None,
                 has_gpu: bool = False, always_use_board: bool = False):
    """Runs the poll -> crunch -> submit cycle forever for one lane. A "lane" is one independent
    identity polling /get_work and calling Ollama on its own -- there's normally just one (the
    whole client, as before dual-lane support existed), but a machine with both a real GPU and
    enough spare RAM (see run_dual_lane_if_capable()) runs two: this function unmodified in the
    main thread for the GPU lane (Ctrl+C/the interrupt menu behave exactly as they always have),
    and a second call in a background thread for the CPU lane (force_cpu=True routes that lane's
    Ollama calls through num_gpu=0 so it never competes with the GPU lane for VRAM).

    fancy_ui (this lane's own independent redrawing box) is only ever used for a genuinely solo
    lane with nothing else concurrently active on this machine. Whenever a second lane exists at
    all -- a dual-lane secondary, or any parallel worker -- every lane instead reports into one
    shared `board` (DualStatusBoard): a lane's own box (or even just printing plain lines)
    assumes it's the only thing touching the terminal, which a second lane's output would break
    no matter how the printing itself is locked, since a lock only stops characters from
    interleaving, not the cursor math from landing in the wrong place. `always_use_board=True` is
    given to any lane whose entire lifetime already implies multi-lane mode is active (a dual-lane
    secondary, or a parallel worker) -- for those, board presence alone is authoritative. The
    PRIMARY lane persists regardless of what's toggled on/off around it, so its own board usage is
    decided dynamically instead, from dual_controller.active / parallel_controller.active.

    pause_event coordinates the two lanes without needing the background thread to handle Ctrl+C
    itself (Python only ever delivers SIGINT/KeyboardInterrupt to the main thread, so a background
    lane can't catch it directly regardless). The lane running in the main thread sets it right
    before opening the interrupt menu and clears it on resume; both lanes check it at the top of
    every cycle and idle without polling for new work while it's set. Solo (non-dual) runs never
    pass an event here at all, so this is a no-op and behavior is identical to before dual-lane
    support existed.

    stop_event, when set, makes this call return (ending the thread it's running in) at the top
    of the next cycle -- only ever given to a CPU lane spawned by DualLaneController, letting the
    pause menu's "toggle dual-lane" option actually stop and later restart it, rather than the
    lane count being fixed for the whole process lifetime.

    dual_controller is only ever given to the GPU/primary lane (the one running in the main
    thread) -- it's how that lane finds out, on every single report()/banner() call, whether
    dual-lane is *currently* active (which can change at runtime via the pause menu) and which
    board to report into if so. Solo lanes and the CPU lane itself never receive it.
    """

    def safe_print(msg):
        _log_queue.append(msg)

    def current_board():
        return board

    # Rolling window of this lane's own last few *successful* task times (dispatch -> confirmed
    # submitted) -- retried/abandoned attempts don't count, they'd skew this toward "how slow is
    # a bad chunk" instead of "how fast is this lane" (what the number's actually for).
    task_durations = []
    MAX_DURATION_SAMPLES = 10

    def record_duration(seconds):
        task_durations.append(seconds)
        del task_durations[:-MAX_DURATION_SAMPLES]

    def avg_task_seconds():
        """None until this lane has completed at least one task -- sent to the server on every
        /get_work poll so it can compute a capacity-based ETA (sum of 1/speed across online
        nodes) instead of only inferring throughput from how recently chunks finished server-side."""
        return (sum(task_durations) / len(task_durations)) if task_durations else None

    def speed_str():
        avg = avg_task_seconds()
        if avg is None:
            return "calculating..."
        return f"{avg:.1f}s/chunk avg (last {len(task_durations)})"


    def report(task_desc, step_msg, is_first, comp, tot, eta, speed=None):
        s = speed if speed is not None else speed_str()
        if board is not None:
            board.update(lane_tag, task_desc, step_msg, comp, tot, eta, s)
        else:
            _log_queue.append(f"[{lane_tag}] {task_desc}: {step_msg}")


    def banner(msg):
        if board is not None:
            board.note(msg)
        else:
            _log_queue.append(msg)

    current_mode = None
    first_stat_print = True
    # Set right before a task's heavy generation call, cleared right after -- lets the
    # KeyboardInterrupt handler below know whether a task was actually in-flight when the
    # interrupt landed, so a Ctrl+C mid-crunch can be reported as a cancelled task (chunk_id and
    # all) instead of silently vanishing with no record anywhere of what was abandoned.
    current_task_chunk_id = None
    while True:
        try:
            if stop_event is not None and stop_event.is_set():
                return

            if pause_event is not None and pause_event.is_set():
                time.sleep(1)
                continue

            # Checked every cycle, not just at startup -- a new version can land while this
            # client is mid-campaign. With auto-update ON, offer_update() below downloads and
            # os.execv()'s immediately with no prompt (restarting re-enters main() from the top,
            # which naturally resumes polling/crunching once it reaches this loop again). With
            # auto-update OFF, it prints the notice and blocks on a real y/n prompt -- crunching
            # is effectively stopped right here until answered, then resumes if declined
            # (unless mandatory, which exits instead). Only the fancy_ui (main-thread) lane checks
            # this -- a background lane restarting the whole process out from under the primary
            # lane would be worse than just missing an update check on that one thread.
            if fancy_ui:
                update_status, update_info = check_for_update()
                if update_status == "must_update":
                    offer_update(update_status, update_info, mandatory=True)
                elif update_status == "update_available":
                    offer_update(update_status, update_info, mandatory=False)

            # Reported on every poll (cheap -- a local /api/tags call, not a network round trip)
            # regardless of mode, since we don't know we're in audit mode until the response comes
            # back: the server uses this to prefer assigning a roster model this volunteer already
            # has pulled, only falling back to something that needs a fresh download when it has no
            # other choice (see AUDIT_MODEL_ROSTER's assignment logic).
            local_ollama_models = get_local_ollama_models()
            available_models_param = urllib.parse.quote(",".join(sorted(local_ollama_models)))
            # avg_task_seconds is omitted (not sent as 0 or similar) until this lane has completed
            # at least one task -- see avg_task_seconds()'s comment; the server keeps whatever
            # speed it last heard from this user_id rather than treating a missing value as "0".
            speed = avg_task_seconds()
            speed_param = f"&avg_task_seconds={speed}" if speed is not None else ""
            # lane_tag ("GPU"/"CPU"/"MAIN") lets the server's admin dashboard show which physical
            # lane a given user_id actually is -- previously invisible server-side; an admin could
            # only infer dual-lane setups from volunteers' own user_id naming conventions.
            work_package = make_request(f"{SERVER_URL}/get_work?user_id={user_id}&hardware_tier={hardware_tier}&model={urllib.parse.quote(chosen_model)}&client_version={VERSION}&available_models={available_models_param}{speed_param}&lane={lane_tag}", timeout=10)

            mode = work_package.get("mode", "rag")

            if mode != current_mode:
                first_stat_print = True
                # In dual-lane mode this transition is shared server-global state, not a
                # lane-specific event -- only the first lane to notice it announces it (see
                # should_announce_mode's comment). No active board (solo, or dual-lane currently
                # toggled off) means this is always True and behavior is unchanged.
                announce_board = current_board()
                if announce_board is None or announce_board.should_announce_mode(mode):
                    if mode == "idle":
                        # No lane_tag prefix here (unlike the mode-activated banner below) --
                        # idle is server-global, not a per-lane event, and every lane hits it at
                        # the same time, so "[CPU] no tasks available" just read as a confusing,
                        # meaningless label rather than useful info.
                        banner(f"{Colors.GRAY}Server online -- no tasks available (idle mode).{Colors.RESET}")
                    else:
                        banner(f"\n[{lane_tag}] [{MODE_BANNERS.get(mode, mode.upper() + ' MODE ACTIVATED')}]\n")
                current_mode = mode
                with _progress_lock:
                    _global_progress["mode"] = mode

            if mode == "idle":
                report("(idle)", "No tasks (idle)", True, 0, 0, None, speed="idle")
                time.sleep(30)
                continue

            if mode not in ("rag", "finetune", "audit"):
                banner(f"{Colors.YELLOW}[{lane_tag}] [!] Unrecognized mode '{mode}' from server -- skipping this cycle.{Colors.RESET}")
                report("(error)", "Unrecognized mode", True, 0, 0, None, speed="idle")
                time.sleep(5)
                continue

            total_chunks, completed_chunks = work_package.get("total_chunks", 0), work_package.get("completed_chunks", 0)
            eta_seconds = work_package.get("eta_seconds")

            if work_package.get("status") == "done":
                # Doesn't exit -- the server can switch this client into a different mode (or back
                # to idle) later, and it should just keep following along rather than requiring a
                # manual restart every time one campaign's queue empties out.
                banner(f"\n{mode_color(mode)}{Colors.BOLD}[{lane_tag}] [★] {mode.upper()} campaign complete -- all chunks processed. Waiting for the next campaign...{Colors.RESET}")
                report("(done)", "Campaign complete!", True, total_chunks, total_chunks, None, speed="idle")
                time.sleep(30)
                continue
            if work_package.get("status") == "waiting":
                banner(f"{Colors.GRAY}[{lane_tag}] [~] Server online -- no matched tasks left for hardware tier '{hardware_tier}'. Sleeping...{Colors.RESET}")
                report("(waiting)", "No matched tasks", True, completed_chunks, total_chunks, None, speed="idle")
                time.sleep(30); continue


            task = work_package["task"]
            task_start_time = time.time()

            if mode == "rag":
                task["lines"] = len(task.get('raw_content', '').splitlines())
                task_desc = format_current_task_line(task)
                report(task_desc, "Generating analysis...", first_stat_print, completed_chunks, total_chunks, eta_seconds)

                current_task_chunk_id = task["chunk_id"]
                parsed_data, last_failure_reason = generate_rag_analysis(
                    task, chosen_model, max_threads,
                    lambda msg: report(task_desc, msg, False, completed_chunks, total_chunks, eta_seconds),
                    force_cpu,
                )
                current_task_chunk_id = None

                if parsed_data is None:
                    report(task_desc, f"✗ Skipped after 3 failed attempts ({last_failure_reason}). Releasing chunk for another node.", False, completed_chunks, total_chunks, eta_seconds)
                    time.sleep(cooldown if cooldown > 0 else 1)
                    continue

                parsed_data.update({
                    "chunk_id": task["chunk_id"],
                    "title": f"[{task['relative_path']}] - {format_chunk_descriptor(task)}",
                    "user_id": user_id,
                    "lines_crunched": task["lines"],
                    "mode": "rag",
                    "client_version": VERSION,
                })
                report(task_desc, "Submitting analysis to master server...", False, completed_chunks, total_chunks, eta_seconds)
                make_request(f"{SERVER_URL}/submit_work", parsed_data)

                record_duration(time.time() - task_start_time)
                report(task_desc, "✓ Analysis uploaded successfully!", False, completed_chunks + 1, total_chunks, eta_seconds)

            elif mode == "audit":
                task_type = task.get("task_type", "propose")
                task_desc = f"[AUDIT/{task_type.upper()}] {task['chunk_id']} ({task.get('collection', '?')})"
                current_task_chunk_id = task["chunk_id"]

                # Audit mode's model is assigned by the server (see AUDIT_MODEL_ROSTER server-side)
                # rather than auto-detected like RAG/finetune's -- that's the whole mechanism that
                # keeps concurrent volunteers reviewing each other with genuinely different models
                # instead of everyone defaulting to the same one. Falls back to this lane's own
                # auto-detected model only if the server is old enough not to send one.
                audit_model = work_package.get("audit_model") or chosen_model
                if audit_model != chosen_model and not ensure_audit_model_available(
                    audit_model, lambda msg: report(task_desc, msg, False, completed_chunks, total_chunks, eta_seconds),
                    local_ollama_models,
                ):
                    report(task_desc, f"✗ Assigned model '{audit_model}' unavailable and couldn't be pulled -- skipping this cycle.", False, completed_chunks, total_chunks, eta_seconds)
                    time.sleep(cooldown if cooldown > 0 else 5)
                    continue

                if task_type in ("propose", "revise"):
                    verb = "Checking against source..." if task_type == "propose" else "Working on an improved fix..."
                    report(task_desc, verb, first_stat_print, completed_chunks, total_chunks, eta_seconds)
                    parsed_data, last_failure_reason = generate_audit_analysis(
                        task, audit_model,
                        lambda msg: report(task_desc, msg, False, completed_chunks, total_chunks, eta_seconds),
                        force_cpu,
                    )
                    current_task_chunk_id = None

                    if parsed_data is None:
                        report(task_desc, f"✗ Skipped after 3 failed attempts ({last_failure_reason}). Releasing chunk for another node.", False, completed_chunks, total_chunks, eta_seconds)
                        time.sleep(cooldown if cooldown > 0 else 1)
                        continue

                    if task_type == "propose":
                        submission = {
                            "mode": "audit", "task_type": "propose",
                            "chunk_id": task["chunk_id"], "user_id": user_id, "client_version": VERSION,
                            "verdict": parsed_data["verdict"],
                            "reason": parsed_data.get("reason", ""),
                            "corrected_summary": parsed_data.get("corrected_summary"),
                            "corrected_explanation": parsed_data.get("corrected_explanation"),
                            "corrected_related_questions": parsed_data.get("corrected_related_questions") or [],
                        }
                        verdict_msg = "✓ No issue found." if parsed_data["verdict"] == "ok" else f"⚠ Proposed a fix: {parsed_data.get('reason', '')[:80]}"
                    else:  # revise
                        submission = {
                            "mode": "audit", "task_type": "revise",
                            "chunk_id": task["chunk_id"], "user_id": user_id, "client_version": VERSION,
                            "corrected_summary": parsed_data.get("corrected_summary"),
                            "corrected_explanation": parsed_data.get("corrected_explanation"),
                            "corrected_related_questions": parsed_data.get("corrected_related_questions") or [],
                        }
                        verdict_msg = "✓ Submitted a revised fix."

                    report(task_desc, "Submitting to master server...", False, completed_chunks, total_chunks, eta_seconds)
                    make_request(f"{SERVER_URL}/submit_work", submission)
                    record_duration(time.time() - task_start_time)
                    report(task_desc, verdict_msg, False, completed_chunks + 1, total_chunks, eta_seconds)

                else:  # task_type == "review"
                    report(task_desc, "Reviewing another node's proposed fix...", first_stat_print, completed_chunks, total_chunks, eta_seconds)
                    parsed_data, last_failure_reason = generate_audit_review(
                        task, audit_model,
                        lambda msg: report(task_desc, msg, False, completed_chunks, total_chunks, eta_seconds),
                        force_cpu,
                    )
                    current_task_chunk_id = None

                    if parsed_data is None:
                        report(task_desc, f"✗ Skipped after 3 failed attempts ({last_failure_reason}). Releasing chunk for another node.", False, completed_chunks, total_chunks, eta_seconds)
                        time.sleep(cooldown if cooldown > 0 else 1)
                        continue

                    submission = {
                        "mode": "audit", "task_type": "review",
                        "chunk_id": task["chunk_id"], "user_id": user_id, "client_version": VERSION,
                        "review_verdict": parsed_data["verdict"],
                        "review_feedback": parsed_data.get("feedback", ""),
                    }
                    report(task_desc, "Submitting review to master server...", False, completed_chunks, total_chunks, eta_seconds)
                    make_request(f"{SERVER_URL}/submit_work", submission)
                    record_duration(time.time() - task_start_time)
                    verdict_labels = {"approve": "✓ Approved -- fix applied.", "reject": "✗ Rejected -- no real issue.", "revise": "⚠ Sent back for revision."}
                    report(task_desc, verdict_labels.get(parsed_data["verdict"], parsed_data["verdict"]), False, completed_chunks + 1, total_chunks, eta_seconds)

            else:  # mode == "finetune"
                task_desc = format_finetune_task_line(task)
                report(task_desc, "Generating training pairs...", first_stat_print, completed_chunks, total_chunks, eta_seconds)

                current_task_chunk_id = task["chunk_id"]
                parsed, last_failure = generate_finetune_pairs(
                    task, chosen_model,
                    lambda msg: report(task_desc, msg, False, completed_chunks, total_chunks, eta_seconds),
                    force_cpu,
                )
                current_task_chunk_id = None

                if parsed is None:
                    # Submit a 0-pairs result instead of just skipping past it: without this, the
                    # chunk is never reported to the server, so its lock just expires and it gets
                    # handed back out again -- forever, if the failure is deterministic.
                    report(task_desc, f"✗ Skipped after 3 failed attempts ({last_failure}). Marking as done with 0 pairs.", False, completed_chunks, total_chunks, eta_seconds)
                    try:
                        make_request(f"{SERVER_URL}/submit_work", {
                            "chunk_id": task["chunk_id"],
                            "source_type": task["source_type"],
                            "pairs": [],
                            "user_id": user_id,
                            "lines_crunched": 0,
                            "mode": "finetune",
                            "client_version": VERSION,
                        })
                    except Exception:
                        pass
                    time.sleep(1)
                    continue

                pairs_generated = len(parsed["pairs"])
                submission = {
                    "chunk_id": task["chunk_id"],
                    "source_type": task["source_type"],
                    "pairs": parsed["pairs"],
                    "user_id": user_id,
                    "lines_crunched": pairs_generated,
                    "mode": "finetune",
                    "client_version": VERSION,
                }
                report(task_desc, "Submitting pairs to master server...", False, completed_chunks, total_chunks, eta_seconds)
                make_request(f"{SERVER_URL}/submit_work", submission)

                record_duration(time.time() - task_start_time)
                report(task_desc, f"✓ Submitted {pairs_generated} training pairs!", False, completed_chunks + 1, total_chunks, eta_seconds)

            first_stat_print = False
            if cooldown > 0: time.sleep(cooldown)

        except urllib.error.HTTPError as he:
            first_stat_print = True
            if he.code == 426:
                # The server raised its MIN_CLIENT_VERSION while this session was already
                # running -- re-check /version for the real current requirement and prompt the
                # same way the startup check does, rather than just retrying forever.
                status, info = check_for_update()
                if info is not None:
                    offer_update(status, info, mandatory=True)
                else:
                    try:
                        detail = json.loads(he.read().decode('utf-8'))
                    except Exception:
                        detail = he.reason
                    sys.exit(f"\n{Colors.RED}[X] Server rejected this client as outdated (HTTP 426): {detail}{Colors.RESET}")
            if he.code == 403:
                sys.exit(f"\n{Colors.RED}[X] Username '{user_id}' already exists on the network.{Colors.RESET}")
            elif he.code in (400, 422):
                try:
                    detail = json.loads(he.read().decode('utf-8'))
                except Exception:
                    detail = he.reason
                sys.exit(
                    f"\n{Colors.RED}[X] Server rejected the request as invalid (HTTP {he.code}): {detail}\n"
                    f"    This is a data/config problem, not a network hiccup -- retrying won't fix it.\n"
                    f"    Check your volunteer ID and, if this persists, report it as a bug.{Colors.RESET}"
                )
            banner(f"\n{Colors.YELLOW}[{lane_tag}] [Warning] Server error {he.code}. Retrying in 15 seconds...{Colors.RESET}"); interruptible_sleep(15, stop_event=stop_event)
        except urllib.error.URLError:
            current_mode = None
            first_stat_print = True
            banner(f"\n{Colors.RED}[{lane_tag}] [X] Server offline -- no tasks available. Retrying in 15 seconds...{Colors.RESET}"); interruptible_sleep(15, stop_event=stop_event)
        except Exception as e:
            first_stat_print = True
            banner(f"\n{Colors.RED}[{lane_tag}] [Error] Failure path encounter: {e}. Retrying in 5 seconds...{Colors.RESET}"); interruptible_sleep(5, stop_event=stop_event)


def _background_lane(**kwargs):
    try:
        crunch_lane(**kwargs)
    except SystemExit as se:
        _log_queue.append(f"\n{Colors.YELLOW}[{kwargs.get('lane_tag', '?')}] Lane stopped: {se}{Colors.RESET}")


# =============================================================================
# DualLaneController / ParallelWorkerPoolController
# =============================================================================

class DualLaneController:
    def __init__(self, board: TuiStatusBoard, cpu_lane_kwargs: dict):
        self.board           = board
        self.cpu_lane_kwargs = cpu_lane_kwargs
        self.pause_event     = threading.Event()
        self.active          = False
        self._thread         = None
        self._stop_event     = None

    def start(self):
        if self.active:
            return
        self.board.set_label(self.cpu_lane_kwargs["lane_tag"], self.cpu_lane_kwargs["hardware_label"])
        self._stop_event = threading.Event()
        kwargs = dict(self.cpu_lane_kwargs, board=self.board, always_use_board=True,
                      pause_event=self.pause_event, stop_event=self._stop_event)
        self._thread = threading.Thread(target=_background_lane, kwargs=kwargs, daemon=True)
        self._thread.start()
        self.active = True

    def stop(self):
        if not self.active:
            return
        self._stop_event.set()
        self.active = False
        self.board.drop_lane(self.cpu_lane_kwargs["lane_tag"])
        sec_uid = self.cpu_lane_kwargs.get("user_id", "")
        sec_tag = self.cpu_lane_kwargs.get("lane_tag", "CPU")
        if sec_uid:
            threading.Thread(target=_disconnect_lane, args=(sec_uid, sec_tag), daemon=True).start()


class ParallelWorkerPoolController:
    def __init__(self, worker_kwargs: dict, user_id: str, hardware_tier: str,
                 total_vram_gb: float, system_ram_gb: float, force_cpu: bool,
                 board: TuiStatusBoard):
        self.worker_kwargs = worker_kwargs
        self.user_id       = user_id
        self.hardware_tier = hardware_tier
        self.total_vram_gb = total_vram_gb
        self.system_ram_gb = system_ram_gb
        self.force_cpu     = force_cpu
        self.board         = board
        self.worker_count  = PARALLEL_WORKERS_BY_TIER.get(hardware_tier, 1)
        self.active        = False
        self._threads:     list = []
        self._stop_events: list = []
        self._lane_tags:   list = []

    def check_headroom(self) -> tuple:
        if self.force_cpu:
            floor    = CPU_TIER_RAM_FLOOR_GB.get(self.hardware_tier, 0.0)
            per_w    = PARALLEL_WORKERS_RAM_HEADROOM_PER_WORKER_GB.get(self.hardware_tier, 3.0)
            required = floor + per_w * self.worker_count
            if self.system_ram_gb >= required:
                return True, ""
            return False, f"needs {required:.1f} GB RAM, have {self.system_ram_gb:.1f} GB"
        floor    = GPU_TIER_VRAM_FLOOR_GB.get(self.hardware_tier, 0.0)
        per_w    = PARALLEL_WORKERS_VRAM_HEADROOM_PER_WORKER_GB.get(self.hardware_tier, 3.5)
        required = floor + per_w * self.worker_count
        if self.total_vram_gb >= required:
            return True, ""
        return False, f"needs {required:.1f} GB VRAM, have {self.total_vram_gb:.1f} GB"

    def start(self) -> tuple:
        if self.active:
            return True, ""
        ok, reason = self.check_headroom()
        if not ok:
            return False, reason
        # There's no API to ask Ollama what its own OLLAMA_NUM_PARALLEL is set to, so this can't
        # be a hard gate -- but it's worth saying every time, since the failure mode if it's still
        # at Ollama's default (1) is silent and easy to misread as "parallel isn't helping" rather
        # than "Ollama itself is still only running one request at a time." _start_ollama_native()
        # sets this automatically when THIS script is the one launching Ollama, but can't reach an
        # Ollama that was already running before this script started (the common case, e.g.
        # Windows' official installer auto-starts it in the background) -- that case needs the
        # volunteer to set it system-wide and restart Ollama themselves.
        print(f"{Colors.CYAN}[i] For parallel workers to actually run in parallel, Ollama itself needs "
              f"OLLAMA_NUM_PARALLEL >= {self.worker_count} (its default is 1, one request at a time). "
              f"If Ollama was already running before this script started, set that environment "
              f"variable system-wide and restart Ollama.{Colors.RESET}")
        self._threads, self._stop_events, self._lane_tags = [], [], []
        suffixes = "pqrstuvwxyz"
        for i in range(self.worker_count):
            stop_event = threading.Event()
            worker_id  = self.user_id[:11] + suffixes[i % len(suffixes)]
            lane_tag   = f"P{i + 1}"
            self.board.set_label(lane_tag, f"Parallel worker {i + 1}")
            kwargs = dict(self.worker_kwargs, user_id=worker_id, lane_tag=lane_tag,
                          stop_event=stop_event, board=self.board, always_use_board=True)
            t = threading.Thread(target=_background_lane, kwargs=kwargs, daemon=True)
            t.start()
            self._threads.append(t)
            self._stop_events.append(stop_event)
            self._lane_tags.append(lane_tag)
        self.active = True
        return True, ""

    def stop(self):
        if not self.active:
            return
        suffixes = "pqrstuvwxyz"
        for i, tag in enumerate(self._lane_tags):
            worker_uid = self.user_id[:11] + suffixes[i % len(suffixes)] if self.user_id else ""
            if worker_uid:
                threading.Thread(target=_disconnect_lane, args=(worker_uid, tag), daemon=True).start()
            self.board.drop_lane(tag)
        self._lane_tags = []
        for e in self._stop_events:
            e.set()
        self._threads, self._stop_events = [], []
        self.active = False


# =============================================================================
# Textual TUI
# =============================================================================

class _LanesPanel(RichLog):
    """Centre panel: one box per active lane, live-updated every 0.5 s."""

    def __init__(self, **kwargs):
        super().__init__(wrap=False, markup=False, auto_scroll=False, **kwargs)
        self._last_render: str = ""

    def on_mount(self):
        self.set_interval(0.5, self._refresh)

    def _refresh(self):
        width  = self.content_size.width or 80
        lines  = self._build(width)
        render = "\n".join(lines)
        if render == self._last_render:
            return
        self._last_render = render
        self.clear()
        for line in lines:
            self.write(Text.from_ansi(line, no_wrap=True, overflow="crop"))

    @staticmethod
    def _build(width: int) -> list:
        LANE_COLORS = ["\033[96m", "\033[95m", "\033[93m", "\033[94m", "\033[92m", "\033[91m"]
        sep         = chr(9472) * max(1, width - 2)

        with _lane_lock:
            order = list(_lane_order)
            state = {k: dict(v) for k, v in _lane_state.items()}

        if not order:
            return [f"  \033[90m No active lanes yet...\033[0m"]

        lines = []
        for i, tag in enumerate(order):
            info   = state.get(tag, {})
            color  = LANE_COLORS[i % len(LANE_COLORS)]
            label  = info.get("label",  tag)
            task   = info.get("task",   "(waiting...)")
            status = info.get("status", "")
            speed  = info.get("speed",  "calculating...")

            if status.startswith("OK") or status.startswith(chr(10003)):
                sc = "\033[92m"
            elif "fail" in status.lower() or status.startswith("X"):
                sc = "\033[91m"
            else:
                sc = ""

            tag_col = f" {color}{tag:<3}\033[0m"
            lines.append(f"{tag_col} {chr(9474)} {label}")
            lines.append(f"      {chr(9474)} Task  : {task}")
            lines.append(f"      {chr(9474)} Status: {sc}{status}\033[0m")
            lines.append(f"      {chr(9474)} Speed : {speed}")
            lines.append(f"{color}{sep}\033[0m")

        return lines


class _HeaderPanel(Static):
    """Full-width top bar: mode + volunteer name + progress bar + ETA."""

    def __init__(self, **kwargs):
        super().__init__("", **kwargs)
        self._last: str = ""

    def on_mount(self):
        self.set_interval(1, self._refresh)

    def _refresh(self):
        text = self._build(self.content_size.width or 80)
        if text != self._last:
            self._last = text
            self.update(Text.from_ansi(text))

    @staticmethod
    def _build(width: int) -> str:
        with _progress_lock:
            comp = _global_progress["comp"]
            tot  = _global_progress["tot"]
            eta  = _global_progress["eta"]
            mode = _global_progress["mode"]

        mc     = MODE_COLORS.get(mode, "\033[94m")
        ml     = MODE_LABELS.get(mode, mode.upper())
        vol    = _volunteer_id or "?"
        clock  = time.strftime("%H:%M:%S")
        pct    = (comp / tot * 100) if tot else 0.0
        bar_w  = max(10, width - 55)
        filled = round(bar_w * pct / 100)
        bar    = f"\033[92m{chr(9608) * filled}\033[0m\033[2m{chr(9617) * (bar_w - filled)}\033[0m"
        eta_s  = "N/A" if mode == "idle" else format_eta(eta)

        left_plain  = f" CUBYZ CLIENT  [{ml}]  {vol}"
        right_plain = clock
        pad         = max(1, width - len(left_plain) - len(right_plain) - 2)
        line1       = (f" \033[1mCUBYZ CLIENT\033[0m"
                       f"  {mc}\033[1m{ml}\033[0m"
                       f"  \033[96m{vol}\033[0m"
                       + " " * pad + clock)
        label2 = f"  {format_count(comp)}/{format_count(tot)} ({pct:.1f}%)  ETA: {eta_s}"
        line2  = f"  [{bar}]{label2}"
        return line1 + "\n" + line2


class _TerminalPanel(RichLog):
    """Bottom panel: all startup/runtime output, scrollable."""

    def __init__(self, **kwargs):
        super().__init__(wrap=True, markup=False, auto_scroll=True, **kwargs)

    def on_mount(self):
        self.set_interval(0.25, self._drain)

    def _drain(self):
        while _log_queue:
            try:
                line = _log_queue.popleft()
            except IndexError:
                break
            self.write(Text.from_ansi(line))


class CubyzClientApp(App):
    CSS = """
    Screen {
        layout: horizontal;
        background: #0d1117;
    }

    #sidebar {
        width: 28;
        border: round #1e3a5f;
        padding: 1 1;
        height: 100%;
        background: #0d1117;
    }

    #sidebar-title {
        color: #58a6ff;
        text-style: bold;
        margin-bottom: 1;
        width: 100%;
        text-align: center;
    }

    #sidebar Label.section-label {
        color: #484f58;
        margin-top: 1;
        margin-bottom: 0;
    }

    #sidebar Button {
        width: 100%;
        margin-bottom: 1;
        border: none;
    }

    Button.action-btn {
        background: #161b22;
        color: #c9d1d9;
        border: tall #30363d;
    }

    Button.action-btn:hover {
        background: #1f2937;
        color: #58a6ff;
        border: tall #58a6ff;
    }

    Button.danger-btn {
        background: #3d1c1c;
        color: #f85149;
        border: tall #6e2a2a;
    }

    Button.danger-btn:hover {
        background: #6e2a2a;
    }

    Button.warn-btn {
        background: #2a2200;
        color: #e3b341;
        border: tall #6a4e00;
    }

    Button.warn-btn:hover {
        background: #3d3200;
    }

    #main {
        layout: vertical;
        height: 100%;
    }

    #topbar {
        height: 4;
        border: round #1e3a5f;
        background: #0d1117;
        color: #c9d1d9;
    }

    #lanes {
        height: 1fr;
        border: round #1e3a5f;
        background: #0d1117;
        overflow-y: auto;
    }

    #terminal {
        height: 14;
        border: round #1e3a5f;
        background: #0a0d12;
        overflow-y: auto;
    }

    #input-row {
        height: 3;
        layout: horizontal;
        border: round #1e3a5f;
        background: #0d1117;
    }

    #prompt-label {
        width: 3;
        padding: 1 0 1 1;
        color: #58a6ff;
    }

    #user-input {
        width: 1fr;
        border: none;
        background: transparent;
    }
    """

    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        with Vertical(id="sidebar"):
            yield Label("CUBYZ CLIENT", id="sidebar-title")
            yield Label("Actions", classes="section-label")
            yield Button("Leaderboard",   id="btn_leaderboard", classes="action-btn")
            yield Button("Active Users",  id="btn_users",       classes="action-btn")
            yield Label("Settings", classes="section-label")
            yield Button("Rename ID",           id="btn_rename",   classes="action-btn")
            yield Button("Toggle Dual-Lane",    id="btn_dual",     classes="action-btn")
            yield Button("Toggle Parallel",     id="btn_parallel", classes="action-btn")
            yield Label("Diagnostics", classes="section-label")
            yield Button("GPU Diagnostic",      id="btn_gpu_diag",   classes="action-btn")
            yield Button("Clear Benchmark",     id="btn_benchmark",  classes="warn-btn")
            yield Label("", classes="section-label")
            yield Button("Safe Exit",           id="btn_exit",       classes="danger-btn")

        with Vertical(id="main"):
            yield _HeaderPanel(id="topbar")
            yield _LanesPanel(id="lanes")
            yield _TerminalPanel(id="terminal")
            with Horizontal(id="input-row"):
                yield Label(">", id="prompt-label")
                yield Input(placeholder="Type response to prompts here and press Enter", id="user-input")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        text = event.value.strip()
        event.input.value = ""
        if text:
            _log_queue.append(f"\033[96m> {text}\033[0m")
            _input_queue.put(text)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        bid = event.button.id

        if bid == "btn_leaderboard":
            def _fetch():
                text = fetch_leaderboard_text()
                for line in text.split("\n"):
                    _log_queue.append(line)
            threading.Thread(target=_fetch, daemon=True).start()

        elif bid == "btn_users":
            def _fetch():
                text = fetch_userlist_text()
                for line in text.split("\n"):
                    _log_queue.append(line)
            threading.Thread(target=_fetch, daemon=True).start()

        elif bid == "btn_rename":
            def _do_rename():
                current = load_saved_user()
                new_id  = _tui_input(f"Current: {current}. Enter new ID (3-12 letters, blank = cancel): ")
                if not new_id:
                    _log_queue.append(f"\033[90m[~] Rename cancelled.\033[0m")
                    return
                if not is_valid_user_id(new_id):
                    _log_queue.append(f"\033[91m[X] Invalid ID -- 3-12 letters only.\033[0m")
                    return
                try:
                    make_request(f"{SERVER_URL}/rename_user?old_user_id={current}&new_user_id={new_id}", timeout=15)
                except Exception as e:
                    _log_queue.append(f"\033[91m[X] Rename failed: {e}\033[0m")
                    return
                save_user(new_id)
                _log_queue.append(f"\033[92m[OK] Renamed to '{new_id}'. Restart to apply.\033[0m")
            threading.Thread(target=_do_rename, daemon=True).start()

        elif bid == "btn_dual":
            dc = _dual_controller_ref
            if dc is None:
                _log_queue.append(f"\033[90m[~] Dual-lane not available on this machine.\033[0m")
            elif dc.active:
                dc.stop()
                _log_queue.append(f"\033[90m[OK] Dual-lane DISABLED.\033[0m")
            else:
                dc.start()
                _log_queue.append(f"\033[92m[OK] Dual-lane ENABLED.\033[0m")

        elif bid == "btn_parallel":
            pc = _parallel_controller_ref
            if pc is None:
                _log_queue.append(f"\033[90m[~] Parallel workers not available.\033[0m")
            elif pc.active:
                pc.stop()
                _log_queue.append(f"\033[90m[OK] Parallel workers DISABLED.\033[0m")
            else:
                started, reason = pc.start()
                if started:
                    _log_queue.append(f"\033[92m[OK] Parallel workers ENABLED.\033[0m")
                else:
                    _log_queue.append(f"\033[91m[X] Cannot enable: {reason}\033[0m")

        elif bid == "btn_benchmark":
            def _do():
                save_benchmark_result({})
                _log_queue.append(f"\033[96m[~] Benchmark cache cleared. Restart to re-benchmark.\033[0m")
            threading.Thread(target=_do, daemon=True).start()

        elif bid == "btn_gpu_diag":
            threading.Thread(target=run_live_gpu_diagnostic, daemon=True).start()

        elif bid == "btn_exit":
            _notify_server_disconnect()
            self.exit()

    def action_quit(self):
        _notify_server_disconnect()
        self.exit()


_primary_stop_event = threading.Event()

def _disconnect_lane(user_id: str, lane_tag: str):
    if not user_id:
        return
    try:
        make_request(
            f"{SERVER_URL}/disconnect?user_id={user_id}&lane={lane_tag}",
            method="POST",
            timeout=5,
        )
        _log_queue.append(f"{Colors.GRAY}    [{lane_tag}] offline.{Colors.RESET}")
    except Exception as e:
        _log_queue.append(f"{Colors.YELLOW}    [{lane_tag}] disconnect notify failed: {e}{Colors.RESET}")


# -- Server disconnect notification -------------------------------------------
def _notify_server_disconnect():
    """POST /disconnect for every lane that was active in this session so the server marks
    them offline immediately. Signals stop events first to prevent background polling threads
    from re-registering as online right after disconnect."""
    _primary_stop_event.set()
    lanes_to_notify = []

    # Primary lane
    if _volunteer_id:
        lanes_to_notify.append((_volunteer_id, "GPU" if _has_gpu else "CPU"))

    # Dual-lane CPU secondary
    dc = _dual_controller_ref
    if dc is not None:
        if dc.active:
            sec_uid = dc.cpu_lane_kwargs.get("user_id", "")
            sec_tag = dc.cpu_lane_kwargs.get("lane_tag", "CPU")
            if sec_uid:
                lanes_to_notify.append((sec_uid, sec_tag))
        dc.stop()

    # Parallel worker lanes
    pc = _parallel_controller_ref
    if pc is not None:
        if pc.active:
            suffixes = "pqrstuvwxyz"
            for i, tag in enumerate(pc._lane_tags):
                worker_uid = _volunteer_id[:11] + suffixes[i % len(suffixes)] if _volunteer_id else ""
                if worker_uid:
                    lanes_to_notify.append((worker_uid, tag))
        pc.stop()

    if not lanes_to_notify:
        return

    _log_queue.append(f"{Colors.GRAY}[~] Notifying server of disconnect...{Colors.RESET}")
    for uid, lane_tag in lanes_to_notify:
        _disconnect_lane(uid, lane_tag)


atexit.register(_notify_server_disconnect)


# =============================================================================
# Entry point
# =============================================================================

def main():
    global _volunteer_id, _dual_controller_ref, _parallel_controller_ref, _has_gpu

    app = CubyzClientApp()

    def _startup():
        global _volunteer_id, _dual_controller_ref, _parallel_controller_ref, _has_gpu

        print(f"\033[1m=== CAFS -- Cubyz AI Folding System (TUI v{VERSION}) ===\033[0m")

        # Volunteer ID
        user_id = load_saved_user()
        if user_id and is_valid_user_id(user_id):
            print(f"\033[92m[OK] Auto-logged in as: {user_id}\033[0m")
        else:
            if user_id:
                print(f"\033[93m[!] Saved ID '{user_id}' is invalid. Please re-enter.\033[0m")
            user_id = ""
            while not is_valid_user_id(user_id):
                user_id = input("Enter your volunteer ID (3-12 letters): ").strip()
            save_user(user_id)

        _volunteer_id = user_id
        with _progress_lock:
            _global_progress["mode"] = "idle"

        # Auto-update preference
        if load_auto_update_preference() is None:
            print(f"\n\033[96m\033[1m[i] AUTO-UPDATE OPTION\033[0m")
            print(f"\033[96m    y = download and restart automatically when updates release")
            print(f"    n = ask me each time\033[0m")
            choice = input("Enable auto-update? (y/n): ").strip().lower()
            save_auto_update_preference(choice == 'y')
            print(f"\033[92m[OK] Auto-update {'enabled' if choice == 'y' else 'disabled'}.\033[0m")

        # Version check
        update_status, update_info = check_for_update()
        if update_status == "must_update":
            offer_update(update_status, update_info, mandatory=True)
        elif update_status == "update_available":
            offer_update(update_status, update_info, mandatory=False)
        elif update_status == "check_failed":
            print(f"\033[90m[~] Could not reach server for update check -- continuing.\033[0m")

        # Hardware detection
        print(f"\033[96m[~] Detecting hardware...\033[0m")
        chosen_model, gpu_type, total_vram_gb = get_vram_and_choose_model()
        system_ram_gb = get_system_ram_gb()
        cpu_model, cpu_tier = get_cpu_model_tier(system_ram_gb)
        _has_gpu = gpu_type != "cpu"

        if gpu_type == "cpu":
            chosen_model = cpu_model

        # Ollama setup
        print(f"\033[96m[~] Checking Ollama...\033[0m")
        ensure_ollama_installed(gpu_type)
        ensure_ollama_running_and_model_pulled(chosen_model)
        if gpu_type != "cpu" and chosen_model != cpu_model:
            ensure_ollama_running_and_model_pulled(cpu_model)

        # Benchmark
        primary_is_gpu = gpu_type != "cpu"
        gpu_time = cpu_time = None
        gpu_error = cpu_error = None

        if gpu_type != "cpu":
            fingerprint = f"v{BENCHMARK_VERSION}:{gpu_type}:{round(total_vram_gb,1)}:{os.cpu_count()}:{round(system_ram_gb,1)}:{chosen_model}:{cpu_model}"
            cached = load_benchmark_result()
            if cached.get("fingerprint") == fingerprint:
                primary_is_gpu = cached["primary_is_gpu"]
                gpu_time  = cached.get("gpu_time")
                cpu_time  = cached.get("cpu_time")
                gpu_error = cached.get("gpu_error")
                cpu_error = cached.get("cpu_error")
                print(f"\033[92m[OK] Using cached benchmark result.\033[0m")
            else:
                print(f"\033[96m[~] Warming up models (first load can be slow, doesn't count against the benchmark)...\033[0m")
                warm_up_model(chosen_model)
                if cpu_model != chosen_model:
                    warm_up_model(cpu_model)

                print(f"\033[96m[~] Running hardware benchmark (one-time, up to 4 minutes)...\033[0m")
                # Sequential, not two threads racing each other -- these used to run concurrently,
                # which assumed Ollama could actually serve both requests in parallel. It usually
                # can't: OLLAMA_NUM_PARALLEL defaults to 1 (serializing generation requests
                # server-side) unless a volunteer has explicitly set it otherwise, which almost no
                # native Windows/Mac install does. Under that default, "concurrent" client threads
                # don't get concurrent GPU/CPU work -- whichever request Ollama picks up second
                # just sits queued behind the first for its ENTIRE duration, then still only gets
                # its own BENCHMARK_TIMEOUT budget to run in once it starts. A slow-but-legitimate
                # first request (e.g. the CPU lane on a big model) can easily eat enough of that
                # queueing time to make an otherwise-healthy GPU look like it timed out -- confirmed
                # live: a volunteer's RTX 4060 Ti (12GB, easily capable) kept reporting "GPU
                # benchmark failed (timeout: timed out)" even after warm-up eliminated cold-load
                # time as a cause. Running them one at a time doubles the worst-case wall time for
                # this one-time startup step, but each lane now gets an honest, uncontended shot at
                # its own timeout budget instead of a result that depends on which one Ollama
                # happened to schedule first.
                _bench = {}
                arch_bad, arch_reason = check_gpu_architecture_support(gpu_type)
                if arch_bad:
                    print(f"\033[93m[!] GPU arch unsupported: {arch_reason} -- skipping GPU bench.\033[0m")
                    _bench["gpu"] = (None, arch_reason)
                else:
                    _bench["gpu"] = benchmark_lane(chosen_model, force_cpu=False)
                _bench["cpu"] = benchmark_lane(cpu_model, force_cpu=True)
                gpu_time, gpu_error = _bench.get("gpu", (None, None))
                cpu_time, cpu_error = _bench.get("cpu", (None, None))
                gpu_tier_cmp = gpu_tier_from_vram(total_vram_gb)

                if gpu_time is None:
                    primary_is_gpu = False
                    # no_gpu_offload and "unsupported arch" both mean the same thing to a
                    # volunteer: this GPU can't actually be used by Ollama here, for reasons
                    # that are a driver/backend-support problem, not something they did wrong or
                    # can fix from this console. The raw diagnostic string (still logged via
                    # save_benchmark_result()/diagnostics for us to actually debug with) reads
                    # like an error in OUR software otherwise -- confirmed live, a Polaris (AMD
                    # gfx803, unsupported by ROCm) card's rocminfo wasn't found so the arch
                    # blocklist check below never caught it, and the real benchmark ran and
                    # failed with the raw "no_gpu_offload: ..." string front and center.
                    if gpu_error and ("no_gpu_offload" in gpu_error or "unsupported arch" in gpu_error):
                        print(f"\033[93m[!] GPU not supported by Ollama on this machine -- using CPU instead.\033[0m")
                    else:
                        print(f"\033[93m[!] GPU benchmark failed ({gpu_error}) -- using CPU.\033[0m")
                elif cpu_time is None:
                    primary_is_gpu = True
                    print(f"\033[92m[OK] GPU ({gpu_time:.1f}s) primary.\033[0m")
                elif TIER_RANK.get(cpu_tier, 0) != TIER_RANK.get(gpu_tier_cmp, 0):
                    primary_is_gpu = TIER_RANK[gpu_tier_cmp] > TIER_RANK[cpu_tier]
                    winner = "GPU" if primary_is_gpu else "CPU"
                    print(f"\033[92m[OK] {winner} chosen (higher capability tier).\033[0m")
                else:
                    primary_is_gpu = gpu_time <= cpu_time
                    winner = "GPU" if primary_is_gpu else "CPU"
                    print(f"\033[92m[OK] {winner} chosen: GPU {gpu_time:.1f}s vs CPU {cpu_time:.1f}s.\033[0m")

                save_benchmark_result({
                    "fingerprint": fingerprint, "primary_is_gpu": primary_is_gpu,
                    "gpu_time": gpu_time, "cpu_time": cpu_time,
                    "gpu_error": gpu_error, "cpu_error": cpu_error,
                })

        # Lane override
        lane_override = load_lane_override()
        if lane_override == "cpu" and primary_is_gpu:
            primary_is_gpu = False
            print(f"\033[96m[~] Primary lane overridden to CPU.\033[0m")
        elif lane_override == "gpu" and not primary_is_gpu and gpu_time is not None:
            primary_is_gpu = True
            print(f"\033[96m[~] Primary lane overridden to GPU.\033[0m")

        gpu_native_model = chosen_model
        gpu_native_tier  = gpu_tier_from_vram(total_vram_gb) if gpu_type != "cpu" else None

        real_cpu_name = get_cpu_name()
        real_gpu_name = get_gpu_name(gpu_type) if gpu_type != "cpu" else ""

        if not primary_is_gpu:
            chosen_model      = cpu_model
            hardware_tier     = cpu_tier
            mode_desc         = f"Eco Profile ({real_cpu_name}, {cpu_model})"
            cooldown          = 4.0
            max_threads       = max(2, (os.cpu_count() or 4) - 1)
            primary_hw_label  = f"{real_cpu_name} ({system_ram_gb:.1f} GB RAM)"
        else:
            hardware_tier     = gpu_tier_from_vram(total_vram_gb)
            cooldown          = 0.0 if total_vram_gb > 8.0 else 1.5
            max_threads       = None if total_vram_gb > 8.0 else 4
            mode_desc         = f"Performance Profile ({real_gpu_name})"
            primary_hw_label  = f"{real_gpu_name} ({total_vram_gb:.1f} GB VRAM)"

        primary_lane_tag = "GPU" if primary_is_gpu else "CPU"

        dual_capable = (
            gpu_type != "cpu"
            and gpu_time is not None
            and cpu_time is not None
            and system_ram_gb >= DUAL_LANE_MIN_RAM_GB
            and total_vram_gb >= DUAL_LANE_MIN_VRAM_GB
        )

        session_event = {
            "event": "session_start", "user_id": user_id, "platform": PLATFORM,
            "gpu_type": gpu_type, "total_vram_gb": round(total_vram_gb, 2),
            "system_ram_gb": round(system_ram_gb, 2), "chosen_model": chosen_model,
            "hardware_tier": hardware_tier, "client_version": VERSION,
            "dual_lane": dual_capable, "primary_is_gpu": primary_is_gpu,
            "benchmark_gpu_time": gpu_time, "benchmark_cpu_time": cpu_time,
            "benchmark_gpu_error": gpu_error, "benchmark_cpu_error": cpu_error,
        }
        log_diagnostic(session_event)
        submit_diagnostic_to_server(session_event)

        board = TuiStatusBoard()
        board.set_label(primary_lane_tag, primary_hw_label)

        parallel_controller = ParallelWorkerPoolController(
            worker_kwargs=dict(
                hardware_tier=hardware_tier, chosen_model=chosen_model,
                max_threads=max_threads, cooldown=cooldown,
                mode_desc=mode_desc, hardware_label=primary_hw_label,
                force_cpu=not primary_is_gpu, fancy_ui=False,
            ),
            user_id=user_id, hardware_tier=hardware_tier,
            total_vram_gb=total_vram_gb, system_ram_gb=system_ram_gb,
            force_cpu=not primary_is_gpu, board=board,
        )
        _parallel_controller_ref = parallel_controller

        dual_controller = None
        if dual_capable:
            if primary_is_gpu:
                sec_tag       = "CPU"
                sec_model     = cpu_model
                sec_tier      = cpu_tier
                sec_threads   = max(2, (os.cpu_count() or 4) - 2)
                sec_cooldown  = 1.0
                sec_force_cpu = True
                sec_hw_label  = f"{real_cpu_name} ({system_ram_gb:.1f} GB RAM)"
                sec_desc      = f"Eco Profile ({real_cpu_name})"
            else:
                sec_tag       = "GPU"
                sec_model     = gpu_native_model
                sec_tier      = gpu_native_tier
                sec_threads   = None if total_vram_gb > 8.0 else 4
                sec_cooldown  = 0.0 if total_vram_gb > 8.0 else 1.5
                sec_force_cpu = False
                sec_hw_label  = f"{real_gpu_name} ({total_vram_gb:.1f} GB VRAM)"
                sec_desc      = f"Performance Profile ({real_gpu_name})"

            print(f"[96m[OK] Dual-lane: {primary_hw_label} + {sec_hw_label}[0m")
            board.set_label(sec_tag, sec_hw_label)
            secondary_user_id = user_id[:11] + ("c" if primary_is_gpu else "g")
            submit_diagnostic_to_server({
                "event": "session_start", "user_id": secondary_user_id, "platform": PLATFORM,
                "gpu_type": "cpu" if primary_is_gpu else gpu_type,
                "total_vram_gb": 0.0 if primary_is_gpu else round(total_vram_gb, 2),
                "system_ram_gb": round(system_ram_gb, 2),
                "chosen_model": sec_model, "hardware_tier": sec_tier,
                "client_version": VERSION, "dual_lane": True,
                "primary_is_gpu": not primary_is_gpu,
            })
            dual_controller = DualLaneController(board=board, cpu_lane_kwargs=dict(
                lane_tag=sec_tag, user_id=secondary_user_id, hardware_tier=sec_tier,
                chosen_model=sec_model, max_threads=sec_threads, cooldown=sec_cooldown,
                mode_desc=sec_desc, hardware_label=sec_hw_label,
                force_cpu=sec_force_cpu, fancy_ui=False,
                parallel_controller=parallel_controller,
            ))
            dual_controller.start()
            _dual_controller_ref = dual_controller

        print(f"[92m[OK] Starting crunching ({primary_lane_tag}, {chosen_model})...[0m")

        crunch_lane(
            lane_tag=primary_lane_tag, user_id=user_id, hardware_tier=hardware_tier,
            chosen_model=chosen_model, max_threads=max_threads, cooldown=cooldown,
            mode_desc=mode_desc, hardware_label=primary_hw_label,
            force_cpu=not primary_is_gpu, fancy_ui=True,
            pause_event=dual_controller.pause_event if dual_controller else None,
            board=board, stop_event=_primary_stop_event, dual_controller=dual_controller,
            parallel_controller=parallel_controller, has_gpu=_has_gpu,
        )

    def _startup_wrapper():
        try:
            _startup()
        except SystemExit as se:
            # _startup() and everything it calls (hardware checks, Ollama setup, the primary
            # crunch_lane) run on this background thread, not main -- a bare SystemExit here only
            # kills this thread, leaving app.run() on main spinning forever on a frozen screen with
            # nothing happening and no way out short of Ctrl+C. Log it and shut the whole app down
            # from the thread that's actually allowed to touch it (call_from_thread), so a fatal
            # startup/crunch error genuinely exits instead of silently hanging.
            _log_queue.append(f"\n{Colors.RED}[X] {se}{Colors.RESET}")
            try:
                app.call_from_thread(app.exit)
            except Exception:
                os._exit(1)

    startup_thread = threading.Thread(target=_startup_wrapper, daemon=True)
    startup_thread.start()
    app.run()


if __name__ == "__main__":
    main()

