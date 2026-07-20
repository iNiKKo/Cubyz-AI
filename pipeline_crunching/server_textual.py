import os
import re
import sys
import json
import time
import shutil
import hashlib
import asyncio
import threading
from collections import deque
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
# rich.text.Text is still used to hand the existing ANSI-colored content lines to textual without
# textual trying to reinterpret the raw escape codes -- see _ConnectionsPanel/_EventsPanel.
# `pip install rich textual` if missing.
from rich.text import Text
# The admin console's interactive terminal UI -- see the comment above CubyzAdminApp for why this
# replaced the rich.live.Live-only version (real keyboard-driven mode selection needs an actual
# application framework, not just a rendering library).
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Static, RadioSet, RadioButton, RichLog, Button, Collapsible

# ============================================================
# Console logging: every campaign event used to be a raw, differently-shaped print(f"...") scattered
# across every dispatch/submit branch -- no consistent column layout, no color, and the username
# was sometimes at the start of the line, sometimes buried mid-sentence, never in the same visual
# spot twice. Confirmed live: watching a multi-node campaign scroll by, it was genuinely hard to
# tell at a glance which volunteer a given line was even about. log_event() below gives every line
# the same shape (timestamp, mode badge, a fixed-width colored username field, a severity symbol,
# then the message), auto-disabled (no ANSI codes) when stdout isn't a real terminal.
# ============================================================
# Windows' legacy console host does NOT interpret ANSI cursor-movement escape codes (\033[nA,
# \033[J, \033[F, \033[2J\033[H, etc.) unless ENABLE_VIRTUAL_TERMINAL_PROCESSING is explicitly
# turned on via SetConsoleMode -- SGR color codes (\033[91m and friends) go through a completely
# separate, much older code path and render correctly regardless, which is exactly why colors
# always looked right here while THREE different admin-dashboard redraw strategies in a row
# (full-screen clear, then a per-line cursor-up erase, then a cursor-up + erase-to-end-of-screen)
# all failed identically: on an unpatched Windows console none of those are cursor-movement at
# all, they're inert bytes the console just doesn't act on, so every redraw landed as fresh
# scrolled-down text instead of overwriting in place -- confirmed live as the dashboard stacking a
# fresh full copy of itself every single 2-second cycle. Best-effort and silent on failure (e.g.
# stdout isn't a real Windows console handle, running inside some wrapper that doesn't expose
# one) -- this is a startup nicety, not something that should ever be able to crash the server.
if sys.platform == "win32":
    try:
        import ctypes
        _kernel32 = ctypes.windll.kernel32
        _STD_OUTPUT_HANDLE = -11
        _ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
        _stdout_handle = _kernel32.GetStdHandle(_STD_OUTPUT_HANDLE)
        _console_mode = ctypes.c_uint32()
        if _kernel32.GetConsoleMode(_stdout_handle, ctypes.byref(_console_mode)):
            _kernel32.SetConsoleMode(_stdout_handle, _console_mode.value | _ENABLE_VIRTUAL_TERMINAL_PROCESSING)
    except Exception:
        pass

_TTY = sys.stdout.isatty()

# Every attribute is a real escape code on a real terminal, or "" everywhere else -- defined
# conditionally here (not stripped later) specifically so any Colors.X reference embedded directly
# inside a log_event() message string (not just the timestamp/badge/user/symbol wrapper log_event
# itself controls) is automatically a no-op when stdout isn't a real terminal, without every call
# site needing its own _TTY check.
class Colors:
    RESET = "\033[0m" if _TTY else ""
    BOLD = "\033[1m" if _TTY else ""
    DIM = "\033[2m" if _TTY else ""
    RED = "\033[91m" if _TTY else ""
    GREEN = "\033[92m" if _TTY else ""
    YELLOW = "\033[93m" if _TTY else ""
    BLUE = "\033[94m" if _TTY else ""
    MAGENTA = "\033[95m" if _TTY else ""
    CYAN = "\033[96m" if _TTY else ""
    GRAY = "\033[90m" if _TTY else ""
    WHITE = "\033[97m" if _TTY else ""

# Per-client colors are deliberately a SEPARATE palette from Colors' basic 8 -- red/green/yellow
# are already "error/success/warning", blue/magenta/cyan are already the RAG/finetune/audit mode
# badges (_MODE_BADGES below), and white/gray are already "emphasis/dim". Reusing any of those for
# a client's name would make that client's lines look like a status color instead of an identity.
# These are 256-color ANSI codes (\033[38;5;Nm) instead, picked for visual distinctness from each
# other AND from the reserved basic-8 hues above (oranges, purples, teals, pinks -- not the
# straight red/green/yellow/blue/magenta/cyan points on the wheel).
_CLIENT_COLOR_PALETTE = [f"\033[38;5;{n}m" if _TTY else "" for n in (
    208,  # orange
    141,  # purple
    43,   # teal
    213,  # pink
    179,  # gold/tan
    75,   # sky blue
    204,  # rose
    112,  # lime green (distinct from Colors.GREEN's pure green)
    159,  # pale cyan-teal
    216,  # peach
    99,   # violet
    193,  # pale yellow-green
    203,  # coral
    80,   # aquamarine
    183,  # lavender
    173,  # copper
)]

# user_id (lowercased) -> assigned palette index, built lazily and never reassigned once set, so
# a volunteer's color is stable for the life of the process (and stable across restarts too, since
# it's derived from _user_first_seen's persisted join order, not process-local state). Colors are
# handed out in first-seen order rather than by hashing specifically so two simultaneously-online
# clients can never collide as long as there are fewer of them than palette entries -- a hash mod
# palette-length would let two unlucky usernames land on the same slot.
_user_color_assignment = {}

def _user_color(user_id: str) -> str:
    if not _TTY or not user_id:
        return ""
    key = user_id.lower()
    if key not in _user_color_assignment:
        # Assign the next unused slot, preferring first-seen order (falls back to insertion order
        # for a user not yet in _user_first_seen, e.g. mid-request before it's recorded).
        known_order = sorted(_user_first_seen.keys(), key=lambda k: _user_first_seen[k])
        for k in known_order:
            if k not in _user_color_assignment:
                _user_color_assignment[k] = len(_user_color_assignment) % len(_CLIENT_COLOR_PALETTE)
        if key not in _user_color_assignment:
            _user_color_assignment[key] = len(_user_color_assignment) % len(_CLIENT_COLOR_PALETTE)
    return _CLIENT_COLOR_PALETTE[_user_color_assignment[key]]

_MODE_BADGES = {  # (color, label) -- RAG/finetune colors match CUBYZ_FOLDING.py's client-side convention
    "rag": (Colors.CYAN, "RAG"),
    "finetune": (Colors.MAGENTA, "FINETUNE"),
    "audit": (Colors.BLUE, "AUDIT"),
    "admin": (Colors.GRAY, "ADMIN"),
}

# Persisted across restarts (unlike online_clients, which is a fresh in-memory dict every process
# start) so the admin dashboard's "joined" column reflects how long a volunteer has actually been
# part of the project, not just this particular server process's uptime. Computed independently of
# PIPELINE_ROOT (defined much later in this file, alongside the other campaign_state/* paths) since
# this needs to exist this early, before any of that.
USER_FIRST_SEEN_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "campaign_state", "user_first_seen.json")
_user_first_seen = {}  # user_id (lower) -> unix timestamp, persisted -- see USER_FIRST_SEEN_FILE

def _touch_first_seen(user_id: str):
    key = user_id.lower()
    if key in _user_first_seen:
        return
    _user_first_seen[key] = time.time()
    try:
        with open(USER_FIRST_SEEN_FILE, "w", encoding="utf-8") as f:
            json.dump(_user_first_seen, f, indent=2)
    except Exception:
        pass

if os.path.exists(USER_FIRST_SEEN_FILE):
    try:
        with open(USER_FIRST_SEEN_FILE, encoding="utf-8") as f:
            _user_first_seen.update(json.load(f))
    except Exception:
        pass

# ---- Live admin dashboard state (see render_dashboard()) --------------------------------------
_user_last_status = {}   # user_id (lower) -> {"mode","symbol","symbol_color","message","timestamp"}
_user_error_counts = {}  # user_id (lower) -> int, incremented for every RED-severity event
_recent_events = deque(maxlen=10)  # rolling tail of (ts, mode, user_id, symbol, symbol_color, message)

# user_id (lower) -> unix timestamp this ONLINE STREAK started -- unlike _user_first_seen (which
# only ever grows, tracking the volunteer's very first-ever connection), this resets to "now"
# whenever a lane comes back online after being stale/offline, so the connections panel's
# "Connected" field reflects how long THIS session has run, not lifetime history. Deliberately
# in-memory only (not persisted) -- a server restart is itself a disconnect from every client's
# point of view, so starting every streak fresh on restart is correct, not a bug. Not locked --
# same reasoning as _user_last_status/_user_hardware_info: a lost update here is, at worst, a
# streak's start time being off by one poll interval, never a correctness issue worth a lock.
_user_connected_since = {}

def _touch_connected_since(user_id: str) -> None:
    """Called from any endpoint that just marked a lane as online (see online_clients' own
    assignments) -- resets that lane's streak start if it was NOT already online a moment ago."""
    key = user_id.lower()
    prior = online_clients.get(key)
    was_online = prior is not None and (time.time() - prior.get("timestamp", 0) < DASHBOARD_ONLINE_STALE_SECONDS)
    if not was_online:
        _user_connected_since[key] = time.time()

# Persisted, same reasoning as USER_FIRST_SEEN_FILE above -- this used to be a bare in-memory dict,
# which meant every SERVER restart wiped it back to empty for every volunteer, even ones whose own
# client process never restarted at all: session_start is sent exactly once per client process
# lifetime (at that client's own startup), not resent on every poll, so there was no way for
# already-lost info to come back short of that specific client also restarting. Confirmed live --
# every panel showed "unknown" again after a routine server restart for an unrelated fix.
USER_HARDWARE_INFO_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "campaign_state", "user_hardware_info.json")
_user_hardware_info = {}  # user_id (lower) -> {"platform","gpu_type","total_vram_gb","system_ram_gb","dual_lane",...}, from /diagnostics' session_start event -- see submit_diagnostics()
if os.path.exists(USER_HARDWARE_INFO_FILE):
    try:
        with open(USER_HARDWARE_INFO_FILE, encoding="utf-8") as f:
            _user_hardware_info.update(json.load(f))
    except Exception:
        pass

def _save_user_hardware_info():
    try:
        with open(USER_HARDWARE_INFO_FILE, "w", encoding="utf-8") as f:
            json.dump(_user_hardware_info, f, indent=2)
    except Exception:
        pass

_DASHBOARD_ACTIVE = False  # flipped true once the background render thread actually starts

def log_event(mode: str, user_id: str, symbol: str, symbol_color: str, message: str, short: str = None):
    """The one place every campaign event flows through. Always updates the live dashboard state
    (last status per user, rolling recent-events tail, red-severity error counts) regardless of
    display mode. When the dashboard is actively rendering (_DASHBOARD_ACTIVE, a real terminal),
    this does NOT print a line itself -- the dashboard's own per-user panels are the display, and
    printing here too would just scroll them out of view. Falls back to plain sequential lines
    (original behavior) when there's no dashboard, e.g. output piped to a log file.

    `short` is an optional terse state label (e.g. "PROPOSED FIX", "DISPATCHED REVIEW") for the
    connections panel's one-line-per-client Status field -- that panel has no room for a full
    message with chunk_id/collection/reasons in it (confirmed live, Nick asked for it trimmed), but
    the Recent Events panel and any non-dashboard log output still want the FULL message, so both
    are kept: `message` is untouched everywhere it already went, `short` is purely additive."""
    now = time.time()
    if user_id:
        _user_last_status[user_id.lower()] = {"mode": mode, "symbol": symbol, "symbol_color": symbol_color, "message": message, "short": short or message, "timestamp": now}
        if symbol_color == Colors.RED:
            _user_error_counts[user_id.lower()] = _user_error_counts.get(user_id.lower(), 0) + 1
    _recent_events.append((now, mode, user_id, symbol, symbol_color, message))

    if _DASHBOARD_ACTIVE:
        return
    mode_color, mode_label = _MODE_BADGES.get(mode, (Colors.WHITE, mode.upper()))
    ts = f"{Colors.DIM}{datetime.now().strftime('%H:%M:%S')}{Colors.RESET}"
    u_color = _user_color(user_id)
    user_field = f"{u_color}{user_id:<10}{Colors.RESET}" if user_id else " " * 10
    print(f"{ts} {mode_color}[{mode_label:<8}]{Colors.RESET} {user_field} {symbol_color}{symbol}{Colors.RESET} {message}")

def _relative_time(ago_seconds: float) -> str:
    if ago_seconds < 60:
        return "just now"
    minutes = int(ago_seconds // 60)
    if minutes < 60:
        return f"{minutes}m ago"
    hours, minutes = divmod(minutes, 60)
    if hours < 24:
        return f"{hours}h {minutes}m ago"
    days, hours = divmod(hours, 24)
    return f"{days}d {hours}h ago"

def _mode_stats_file(mode: str):
    return {"rag": RAG_STATS_FILE, "finetune": FINETUNE_STATS_FILE, "audit": AUDIT_STATS_FILE}.get(mode)

def _gpu_tier_from_vram(total_vram_gb: float) -> str:
    """Mirrors CUBYZ_FOLDING.py's gpu_tier_from_vram() exactly -- same thresholds -- so the
    dashboard's explanation of a capability-based CPU-over-GPU choice (see
    _format_benchmark_note) reflects the client's actual real decision logic, not a guess."""
    return "easy" if total_vram_gb <= 4.5 else ("medium" if total_vram_gb <= 8.5 else "hard")

_PLATFORM_LABELS = {"win32": "Windows", "linux": "Linux", "darwin": "macOS"}
_GPU_TYPE_LABELS = {
    "nvidia": "NVIDIA GPU", "amd": "AMD GPU", "intel": "Intel GPU",
    "apple_silicon": "Apple Silicon GPU", "intel_dgpu": "Intel iGPU (Mac)", "cpu": "CPU only (no GPU)",
}

def _format_hardware_info(hw: dict, parallel_active: bool = False) -> str:
    """hw comes from the session_start diagnostic event (see submit_diagnostics()) -- None until
    that volunteer's client has actually reported it, which older (pre-1.1.25) clients never did
    at all, since it used to only ever get logged to that machine's own local file.

    `parallel_active` is determined structurally by the caller (via clusters/lane suffixes, not
    anything the client itself reports -- see _build_connections_lines()) and is purely additive
    to the existing DUAL-LANE flag, since it's the same physical machine running both at once."""
    if not hw:
        return f"{Colors.GRAY}(unknown -- pre-1.1.25 client, or hasn't reported yet){Colors.RESET}"
    os_label = _PLATFORM_LABELS.get(hw.get("platform"), hw.get("platform") or "?")
    # gpu_type "cpu" is ambiguous on its own -- it means either a genuinely GPU-less machine, OR
    # this specific panel is the secondary CPU lane of a dual-lane machine that DOES have a real
    # GPU, just in use by its sibling lane (see main()'s dual-lane session_start report). The
    # latter showing "CPU only (no GPU)" reads as if the whole machine has no GPU at all, which
    # is wrong and confusing -- confirmed live for a real dual-lane volunteer.
    if hw.get("gpu_type") == "cpu" and hw.get("dual_lane"):
        gpu_label = "CPU lane (GPU in use by dual-lane partner)"
    else:
        gpu_label = _GPU_TYPE_LABELS.get(hw.get("gpu_type"), hw.get("gpu_type") or "?")
    vram = hw.get("total_vram_gb")
    vram_text = f" ({vram:.1f} GB VRAM)" if isinstance(vram, (int, float)) and vram > 0 else ""
    ram = hw.get("system_ram_gb")
    ram_text = f"{ram:.1f} GB RAM" if isinstance(ram, (int, float)) else "? GB RAM"
    dual_text = ""
    if hw.get("dual_lane"):
        dual_text = f"  •  {Colors.CYAN}{Colors.BOLD}DUAL-LANE{Colors.RESET}"
        if parallel_active:
            dual_text += f" {Colors.CYAN}{Colors.BOLD}+ PARALLEL{Colors.RESET}"
    elif parallel_active:
        dual_text = f"  •  {Colors.CYAN}{Colors.BOLD}PARALLEL{Colors.RESET}"
    return f"{os_label}  •  {gpu_label}{vram_text}  •  {ram_text}{dual_text}"

def _format_benchmark_note(hw: dict):
    """A real, correctly-detected GPU sitting unused while the client runs on CPU looks like a
    dashboard bug until you know WHY -- benchmark_lane() (a real timed inference call, see its own
    comment) is what actually decides GPU vs CPU, not VRAM detection alone. Returns None when
    there's nothing surprising to explain (no GPU present at all, or the GPU IS the active lane)."""
    if not hw or hw.get("gpu_type") in (None, "cpu") or hw.get("primary_is_gpu"):
        return None
    gpu_time, cpu_time = hw.get("benchmark_gpu_time"), hw.get("benchmark_cpu_time")
    if gpu_time is None:
        gpu_error = hw.get("benchmark_gpu_error")
        # Truncated here (plain text, before any color wrapping) rather than left to run past a
        # narrow terminal -- the raw exception message is already capped at 200 chars client-side,
        # which can still be wider than a normal terminal once the panel's indent/label are added.
        reason = f" -- {_truncate(gpu_error, 90)}" if gpu_error else " (no error detail -- pre-1.1.28 client)"
        cpu_text = f" (CPU: {cpu_time:.1f}s)" if isinstance(cpu_time, (int, float)) else ""
        return f"{Colors.YELLOW}⚠ GPU benchmark FAILED{Colors.RESET}{reason}{cpu_text}"
    # GPU succeeded but CPU still ended up primary -- this used to ALWAYS say "CPU was faster",
    # even when it wasn't. main()'s real decision logic (see its own comment) picks CPU over a
    # faster GPU in one specific case: CPU can reach a more capable model tier than the GPU's low
    # VRAM allows ("capability beats speed"), NOT just raw speed -- confirmed live wrong for a
    # Threadripper (huge RAM, "medium" CPU tier) paired with a weak ~4GB GPU (capped at "easy"):
    # GPU benchmarked FASTER (42.9s vs 81.0s) but lost anyway because "medium" beats "easy", and
    # the old message claimed "CPU was faster", which was backwards.
    if isinstance(cpu_time, (int, float)) and cpu_time < gpu_time:
        return f"{Colors.YELLOW}⚠ GPU benchmark succeeded ({gpu_time:.1f}s) but CPU was genuinely faster ({cpu_time:.1f}s) -- CPU chosen{Colors.RESET}"
    total_vram = hw.get("total_vram_gb")
    gpu_tier = _gpu_tier_from_vram(total_vram) if isinstance(total_vram, (int, float)) else "?"
    winning_tier = hw.get("hardware_tier") or "?"
    cpu_text = f", CPU: {cpu_time:.1f}s" if isinstance(cpu_time, (int, float)) else ""
    return (f"{Colors.YELLOW}⚠ GPU was actually faster ({gpu_time:.1f}s{cpu_text}) but CPU chosen anyway{Colors.RESET} "
            f"-- CPU can reach a more capable tier ({winning_tier}) than the GPU's low VRAM allows ({gpu_tier}); capability beats raw speed")

def _format_progress_line(mode: str, stats: dict) -> str:
    if mode == "audit":
        return (f"{stats.get('chunks_audited', 0)} audited  •  {stats.get('issues_found', 0)} issues found  •  "
                f"{stats.get('reviews_done', 0)} reviewed  •  {stats.get('fixes_applied', 0)} fixes applied")
    if mode == "finetune":
        return f"{stats.get('chunks_completed', 0)} chunks  •  {stats.get('pairs_generated', 0)} pairs generated"
    return f"{stats.get('chunks_completed', 0)} chunks  •  {stats.get('lines_crunched', 0)} lines crunched"

_PROGRESS_SUM_KEYS = {
    "rag": ["chunks_completed", "lines_crunched"],
    "finetune": ["chunks_completed", "pairs_generated"],
    "audit": ["chunks_audited", "issues_found", "reviews_done", "fixes_applied"],
}

# c/g = a dual-lane secondary (see DualLaneController's secondary_user_id); p through z = a
# parallel worker (see ParallelWorkerPoolController's suffix pool). Both build their synthetic id
# the same way: user_id[:11] + one of these letters. Shared by _group_online_by_machine (this
# dashboard) and _merge_lane_children (the leaderboard) -- same underlying identities, two
# different views of them.
_LANE_CHILD_SUFFIXES = "cgpqrstuvwxyz"
_DUAL_SECONDARY_SUFFIXES = "cg"
_PARALLEL_WORKER_SUFFIXES = "pqrstuvwxyz"

def _group_online_by_machine(online: list) -> dict:
    """Clusters online lane identities (a dual-lane secondary, or a parallel worker) under their
    real physical-machine parent instead of each getting its own top-level dashboard panel --
    confirmed live as confusing: a machine running dual-lane or parallel workers showed up as 2-4
    separate boxes (e.g. "nickpc" and "nickpcc") that all describe the same physical hardware.
    Uses the exact same structural reconstruction _merge_lane_children uses for the leaderboard
    (child == parent[:11] + suffix) -- see that function's comment for why this is safe by
    construction. Returns {parent_id: [child_id, ...]} for every online identity that isn't
    itself a child (a genuine standalone machine gets an empty list).
    
    Hardened to handle server restarts: even if the parent lane has not polled yet (so it is not in
    the online list), we still group online children under the parent if the parent is a registered
    historical volunteer or multiple online siblings are present."""
    online_set = set(online)
    children_of = {}
    is_child = set()
    for user_id in online:
        if len(user_id) < 2 or user_id[-1] not in _LANE_CHILD_SUFFIXES:
            continue
        parent_id = user_id[:-1]
        siblings_online = [s for s in online if s.startswith(parent_id) and s != parent_id and len(s) == len(parent_id) + 1 and s[-1] in _LANE_CHILD_SUFFIXES]
        is_valid_parent = (
            parent_id in online_set or
            parent_id in _user_first_seen or
            len(siblings_online) > 1
        )
        if is_valid_parent and parent_id[:11] + user_id[-1] == user_id:
            children_of.setdefault(parent_id, []).append(user_id)
            is_child.add(user_id)
            
    result = {}
    for user_id in online:
        if user_id not in is_child:
            result[user_id] = sorted(children_of.get(user_id, []))
            
    # Include parent keys that are currently offline but have active online children
    for parent_id, children in children_of.items():
        if parent_id not in online_set:
            result[parent_id] = sorted(children)
            
    return result

def _fold_lane_children(ids) -> set:
    """Collapses a dual-lane secondary's/parallel worker's synthetic id into its real parent's,
    for COUNTING distinct physical machines/volunteers -- e.g. {"nickpc","nickpcc","nickpcp"}
    folds to just {"nickpc"}. Unlike _group_online_by_machine (which only ever looks at an
    already-online list and needs the child<->parent grouping itself, not just a count),
    this works on any set (online-only, or online+offline together) since it only needs to know
    whether each id's reconstructed parent is ALSO present in that same set -- confirmed live as
    the fix for the header's online/offline counts showing e.g. "6 online" for 3 actual
    volunteers, since a dual-lane+parallel machine's 3-4 lane identities were each being counted
    as a separate "online" entry.
    
    Hardened to handle server restarts: folds children to their parent even if the parent is offline,
    provided the parent exists in the registered history or multiple siblings are present in the set."""
    id_set = set(ids)
    result = set()
    for uid in id_set:
        if len(uid) >= 2 and uid[-1] in _LANE_CHILD_SUFFIXES:
            parent_id = uid[:-1]
            siblings_in_set = [s for s in id_set if s.startswith(parent_id) and s != parent_id and len(s) == len(parent_id) + 1 and s[-1] in _LANE_CHILD_SUFFIXES]
            is_valid_parent = (
                parent_id in id_set or
                parent_id in _user_first_seen or
                len(siblings_in_set) > 1
            )
            if is_valid_parent:
                result.add(parent_id)
                continue
        result.add(uid)
    return result

def _truncate(text: str, width: int) -> str:
    """Truncates PLAIN text (no ANSI codes inside it -- callers wrap the result in color AFTER
    calling this) to fit width, since counting an escape sequence's raw characters against a
    visible-width budget would truncate way too early or mid-sequence."""
    if width <= 1 or len(text) <= width:
        return text
    return text[:width - 1].rstrip() + "…"

# Dashboard-specific online threshold -- separate from ONLINE_STALE_SECONDS (used elsewhere, e.g.
# the leaderboard endpoint) because a single slow-hardware task cycle (dispatch -> generate ->
# submit -> next poll) can legitimately take several minutes on a weak "easy"-tier machine, and
# 60s was confirmed live to flip a genuinely-still-working node to OFFLINE and back repeatedly.
DASHBOARD_ONLINE_STALE_SECONDS = 300

def _build_header_line(term_width: int, mode_color: str, mode_label: str, online_n: int, offline_n: int) -> str:
    """The connections panel's top line: mode badge + online/offline counts on the left, clock
    right-aligned. Tries progressively shorter left-side content until one actually fits
    term_width -- confirmed live that at a realistic (not even especially narrow) sidebar+panel
    width, the full " CUBYZ DISTRIBUTED SERVER · X MODE · N online · N offline " text plus the
    clock is often already wider than the panel, silently cropping the clock (and, if it got bad
    enough, the online/offline counts too) off the right edge. Each tier is (plain, colored)
    segment pairs, same reasoning as before: padding for the right-aligned clock has to be
    computed from VISIBLE width, not raw string length, since ANSI codes cost zero display width."""
    clock = datetime.now().strftime('%H:%M:%S')
    # Two trailing spaces, not one -- confirmed live that with exactly one, the clock's last
    # digit(s) still got clipped no matter the panel width. RichLog's actual rendered width and
    # this function's computed term_width agree in every direct check done here, but something in
    # the render pipeline (a scrollbar reservation, a cell-width rounding) still eats the very
    # last column in practice; a 1-column safety margin costs nothing and makes that moot instead
    # of chasing the exact off-by-one.
    right_plain = f"{clock}  "
    right_colored = f"{Colors.DIM}{clock}{Colors.RESET}  "

    tiers = [
        [
            (" CUBYZ DISTRIBUTED SERVER ", " CUBYZ DISTRIBUTED SERVER "),
            ("· ", f"{Colors.DIM}·{Colors.RESET} "),
            (f"{mode_label} MODE ", f"{mode_color}{Colors.BOLD}{mode_label} MODE{Colors.RESET} "),
            ("· ", f"{Colors.DIM}·{Colors.RESET} "),
            (f"{online_n} online ", f"{Colors.GREEN}{online_n} online{Colors.RESET} "),
            ("· ", f"{Colors.DIM}·{Colors.RESET} "),
            (f"{offline_n} offline", f"{Colors.GRAY}{offline_n} offline{Colors.RESET}"),
        ],
        [
            (f" {mode_label} MODE ", f" {mode_color}{Colors.BOLD}{mode_label} MODE{Colors.RESET} "),
            ("· ", f"{Colors.DIM}·{Colors.RESET} "),
            (f"{online_n} online ", f"{Colors.GREEN}{online_n} online{Colors.RESET} "),
            ("· ", f"{Colors.DIM}·{Colors.RESET} "),
            (f"{offline_n} offline", f"{Colors.GRAY}{offline_n} offline{Colors.RESET}"),
        ],
        [
            (f" {mode_label} ", f" {mode_color}{Colors.BOLD}{mode_label}{Colors.RESET} "),
            (f"{online_n}↑{offline_n}↓", f"{Colors.GREEN}{online_n}{Colors.RESET}{Colors.DIM}↑{Colors.RESET}{Colors.GRAY}{offline_n}{Colors.RESET}{Colors.DIM}↓{Colors.RESET}"),
        ],
    ]

    for segments in tiers:
        left_plain = "".join(plain for plain, _ in segments)
        if len(left_plain) + len(right_plain) <= term_width:
            left_colored = "".join(colored for _, colored in segments)
            padding = term_width - len(left_plain) - len(right_plain)
            return left_colored + " " * padding + right_colored

    # Even the shortest tier plus the clock doesn't fit -- drop the clock rather than the mode/
    # counts (an operator can always check their own system clock; they can't see the mode/counts
    # anywhere else on this panel). RichLog's own overflow="crop" is still the final backstop if
    # the terminal is narrower than this can reasonably handle.
    left_plain, left_colored = tiers[-1][0][0], tiers[-1][0][1]
    for plain, colored in tiers[-1][1:]:
        left_plain += plain
        left_colored += colored
    return left_colored if len(left_plain) <= term_width else left_colored[:term_width] + Colors.RESET

def _format_eta(seconds: float) -> str:
    if seconds is None or seconds < 0:
        return "ETA: calculating..."
    if seconds == 0:
        return "ETA: complete"
    
    minutes = int(seconds // 60)
    if minutes < 1:
        return f"ETA: {int(seconds)}s remaining"
    
    hours, minutes = divmod(minutes, 60)
    if hours < 1:
        return f"ETA: {minutes}m remaining"
    
    days, hours = divmod(hours, 24)
    if days < 1:
        return f"ETA: {hours}h {minutes}m remaining"
    
    return f"ETA: {days}d {hours}h remaining"

def _build_global_progress_line(term_width: int, mode: str) -> str:
    """A campaign-wide progress bar for whatever mode is currently running -- there was no global
    view of "how far along is the whole campaign" anywhere in the console before (per-client
    Progress lines only show one volunteer's own share). total/completed reuse the exact same
    counters already computed elsewhere in this file for each mode (audit's own status endpoint:
    completed = audit_total_chunks - len(audit_chunk_queue), same shape for rag/finetune)."""
    if mode == "audit":
        state = load_lock_state(AUDIT_LOCK_FILE)
        completed = audit_total_chunks - len(audit_chunk_queue)
        completed_since_tracking = completed - state.get("actions_baseline_completed", completed)
        avg_actions = _audit_avg_actions_per_chunk(state.get("actions_count", 0), completed_since_tracking)
        totals = {
            "audit": (audit_total_chunks, completed, audit_completion_log, avg_actions),
        }
    else:
        totals = {
            "rag": (rag_total_chunks, rag_total_chunks - len(rag_chunk_queue), rag_completion_log, 1.0),
            "finetune": (finetune_total_chunks, finetune_total_chunks - len(finetune_chunk_queue), finetune_completion_log, 1.0),
        }
    if mode not in totals:
        return f"  {Colors.GRAY}(idle -- no active campaign){Colors.RESET}"
    total, completed, log, avg_actions = totals[mode]
    if total <= 0:
        return f"  {Colors.GRAY}(no chunks for this campaign yet){Colors.RESET}"
    completed = max(0, min(completed, total))
    pct = completed / total

    remaining = total - completed
    eta_val = _eta_seconds(log, remaining, avg_actions_per_unit=avg_actions)
    eta_text = _format_eta(eta_val)

    label = f" {completed}/{total} ({pct * 100:.1f}%)  •  {eta_text}"
    bar_width = max(10, term_width - len(label) - 5)  # "  [" + "]" + label
    filled = round(bar_width * pct)
    bar = f"{Colors.GREEN}{'█' * filled}{Colors.RESET}{Colors.DIM}{'░' * (bar_width - filled)}{Colors.RESET}"
    return f"  [{bar}]{label}"

def _build_top_header_lines(width: int = None) -> list:
    """Three lines: the mode/online/offline/clock banner, a blank separator line, and a global
    progress bar for the current campaign -- its own top-of-screen panel (_HeaderPanel), spanning
    the FULL app width above the sidebar+connections+events split. Modified to add the blank spacer
    line to prevent visual crowding of the progress bar, per Nick's ask."""
    term_width = width if width else max(60, min(shutil.get_terminal_size((100, 24)).columns, 160))
    term_width = max(20, term_width)
    mode = CURRENT_MODE
    stats_file = _mode_stats_file(mode)
    user_stats = read_json_file(stats_file, {}) if stats_file else {}
    now = time.time()
    known = set(online_clients.keys()) | set(user_stats.keys())
    online_ids = {u for u in known if u in online_clients and now - online_clients[u]["timestamp"] < DASHBOARD_ONLINE_STALE_SECONDS}
    # Folded to distinct MACHINES, not raw lane identities -- a dual-lane+parallel machine has
    # 3-4 separate online_clients entries (primary/secondary/P1/P2) that all describe ONE
    # volunteer, and counting each of those as its own "online" was overcounting (confirmed live:
    # "6 online" for 3 actual people). See _fold_lane_children()'s comment.
    online_n = len(_fold_lane_children(online_ids))
    offline_n = len(_fold_lane_children(known)) - online_n
    mode_color, mode_label = _MODE_BADGES.get(mode, (Colors.WHITE, mode.upper()))
    header = _build_header_line(term_width, mode_color, mode_label, online_n, offline_n)
    return [
        header,
        "",
        _build_global_progress_line(term_width, mode),
    ]

def _build_connections_lines(width: int = None) -> list:
    """Builds the connections half of the admin console -- a per-machine panel (status/hardware/
    lane/joined/progress/errors) for every online volunteer, instead of an ever-scrolling
    line-per-event log. The old format made it genuinely hard to answer "what is THIS specific
    user doing right now" at a glance on a live multi-node campaign, since their last line could
    be scrolled dozens of lines up by the time you looked. Only online volunteers get a panel --
    offline history is still reflected in the header count, but a wall of stale panels for
    everyone who's ever connected isn't what an admin watching a LIVE campaign wants to scroll
    past. The mode/online/offline/clock banner that used to open this panel now lives in its own
    _HeaderPanel/_build_top_header_lines() instead (see that function) -- this panel starts
    directly with the per-machine content. Split from the old combined _build_dashboard_lines()
    (rich version) into this half and _build_events_lines() specifically so the textual layout can
    put them in separate panels
    (connections top-right, recent events bottom-right, per Nick's s-tui-referenced layout) --
    the actual per-line content logic is otherwise unchanged from the rich version, which was
    itself unchanged from the original hand-rolled-ANSI version. This was never where any of the
    real redraw bugs lived; it's pure content generation."""
    mode = CURRENT_MODE
    stats_file = _mode_stats_file(mode)
    user_stats = read_json_file(stats_file, {}) if stats_file else {}

    # Real PANEL width, not a hardcoded guess and NOT the raw terminal width -- confirmed live
    # that using shutil.get_terminal_size() (the whole terminal) produced content wider than the
    # actual _ConnectionsPanel widget once the 32-column sidebar and borders were accounted for,
    # so anything near the right edge (the header's right-aligned clock, the "ONLINE" status badge
    # on each panel's border) got silently cropped by RichLog's overflow="crop" on a small window.
    # `width` is the caller's actual widget content width (see _ConnectionsPanel.refresh_content())
    # when known; the terminal-size fallback below only matters for a hypothetical caller with no
    # widget of its own (there isn't one right now, but this function predates the textual UI).
    term_width = width if width else max(60, min(shutil.get_terminal_size((100, 24)).columns, 160))
    # Floor is 20, not the old 60 -- that was sized for a whole terminal, but `width` here is
    # this ONE panel's content area next to the sidebar, which is legitimately much narrower than
    # the terminal. Content generation needs to track the real (possibly small) width rather than
    # inflate it, since _build_header_line() and the title-truncation above it already degrade
    # gracefully -- a hardcoded floor higher than the actual panel would just recreate the exact
    # cropping bug this was meant to fix.
    term_width = max(20, term_width)
    box_w = term_width - 2  # leaves room for the leading 2-space indent on content lines

    now = time.time()
    known = set(online_clients.keys()) | set(user_stats.keys())
    online = sorted(u for u in known if u in online_clients and now - online_clients[u]["timestamp"] < DASHBOARD_ONLINE_STALE_SECONDS)
    offline_count = len(known) - len(online)

    lines = []

    # A dual-lane secondary or parallel worker gets its own online_clients/user_stats entry (they
    # ARE independent identities server-side, e.g. for per-lane audit model diversity), but they're
    # the same physical machine as their parent -- see _group_online_by_machine's comment. Grouped
    clusters = _group_online_by_machine(online)
    # Calculate throughput and contribution % per machine
    machine_throughputs = {}
    for pid, c_list in clusters.items():
        m_tp = 0.0
        for uid in [pid] + c_list:
            if uid in online:
                sp = (online_clients.get(uid) or {}).get("speed")
                if sp and sp > 0:
                    m_tp += 1.0 / sp
        machine_throughputs[pid] = m_tp
    total_network_tp = sum(machine_throughputs.values())

    for parent_id in sorted(clusters):
        children = clusters[parent_id]
        lane_ids = [parent_id] + children  # every identity on this machine
        has_parallel = any(cid[-1] in _PARALLEL_WORKER_SUFFIXES for cid in children)
        has_dual = any(cid[-1] in _DUAL_SECONDARY_SUFFIXES for cid in children)

        # Show all online lanes on this machine (GPU/CPU primary + dual secondary + parallel workers)
        display_lane_ids = [lid for lid in lane_ids if lid in online]
        lane_count = len(display_lane_ids)
        u_color = _user_color(parent_id)
        lane_word = "lane" if lane_count == 1 else "lanes"

        m_tp = machine_throughputs.get(parent_id, 0.0)
        contrib_str = f" • {m_tp / total_network_tp * 100.0:.1f}% contrib" if total_network_tp > 0 else ""
        title = f"─ {parent_id} ({lane_count} {lane_word}{contrib_str})" + " "
        badge_w = len(" ") + len("ONLINE") + len(" ─┐") + 1  # +1 for the leading fill space
        title = _truncate(title, max(1, box_w - badge_w - 1))
        fill = max(1, box_w - len(title) - len("ONLINE ─") - 2)
        lines.append(f"{u_color}┌{title}{'─' * fill} {Colors.GREEN}ONLINE{Colors.RESET} {u_color}─┐{Colors.RESET}")

        multi_lane = lane_count > 1
        # Per-lane fields (Hardware/Status/Speed) indent one level deeper than a solo panel's --
        # "    " instead of "  " -- so they read as nested under their own "· lane_id" label
        # instead of sitting at the same indent as the shared System/Joined/Progress footer below,
        # which applies to the whole machine, not any one lane.
        field_indent = "    " if multi_lane else "  "
        for lane_id in display_lane_ids:
            if multi_lane:
                lines.append(f"  {Colors.DIM}{Colors.BOLD}· {lane_id}{Colors.RESET}")
            info = online_clients.get(lane_id, {})
            tier = info.get("tier", "?")
            # audit mode assigns each user a specific model from its diversity roster (see
            # _assign_audit_model), independent of whatever model the client itself locally
            # defaults to -- info["model"] (the client's own self-reported "model" query param)
            # reflects the LATTER, not what audit mode actually dispatched, so it was showing
            # e.g. "qwen2.5-coder:3b" for a lane whose real assigned model was something else
            # entirely (confirmed live). audit_model_assignments is the authoritative source here.
            if mode == "audit" and lane_id in audit_model_assignments:
                model = audit_model_assignments[lane_id].get("model") or "-"
            else:
                model = info.get("model") or "-"
            lane_tag = info.get("lane") or "-"
            lines.append(_truncate(f"{field_indent}Hardware : {tier} tier  •  {model}  •  lane: {lane_tag}", box_w))

            last = _user_last_status.get(lane_id)
            prefix = f"{field_indent}Status   : "
            if last:
                age_seconds = now - last["timestamp"]
                # No "(just now)" -- that's true for nearly every line on a live, fast-moving
                # campaign, so it was just noise repeated on almost every panel. The age is only
                # actually informative once a status has sat for a while.
                suffix = f"  ({_relative_time(age_seconds)})" if age_seconds >= 60 else ""
                # short, not message -- the connections panel shows one terse state per client
                # (e.g. "PROPOSED FIX", "DISPATCHED REVIEW"), not the full message with
                # chunk_id/collection/reasons baked in. The full message is untouched everywhere
                # else (Recent Events, non-dashboard log output) -- see log_event()'s comment.
                msg = _truncate(last.get("short") or last["message"], max(10, box_w - len(prefix) - 1 - len(suffix)))
                lines.append(f"{prefix}{last['symbol_color']}{last['symbol']}{Colors.RESET} {msg}{Colors.DIM}{suffix}{Colors.RESET}")
            else:
                lines.append(f"{prefix}{Colors.GRAY}(no activity yet this session){Colors.RESET}")

            speed = info.get("speed")
            speed_text = f"{speed:.1f}s/task avg" if isinstance(speed, (int, float)) else "calculating..."
            errors = _user_error_counts.get(lane_id, 0)
            errors_text = f"{errors} error{'s' if errors != 1 else ''}" if errors else "0 errors"
            errors_color = Colors.RED if errors else Colors.GRAY
            lines.append(f"{field_indent}Speed    : {speed_text}  •  Errors: {errors_color}{errors_text}{Colors.RESET}")
            if multi_lane:
                lines.append("")

        # One shared System/Joined/Progress for the whole cluster -- same physical machine, so
        # repeating it per lane would just be noise (and a non-primary lane doesn't always send
        # its own session_start at all). Uses whichever lane actually reported hardware info
        # (normally the parent, but falls through to a child if the parent hasn't reported yet).
        # A blank line already separates this from the last lane block when multi_lane (added
        # unconditionally above, including after the final lane -- keeps the shared footer visually
        # distinct from "belonging" to whichever lane happened to be listed last).
        hw = next((_user_hardware_info[lid] for lid in lane_ids if _user_hardware_info.get(lid)), None)
        # Not run through _truncate() -- unlike the other panel lines, this one has ANSI color
        # codes already embedded in it (see _format_hardware_info), and truncating by raw
        # character count risks cutting a line off mid-escape-sequence, corrupting the terminal's
        # color state for everything printed after it. Its content is short and bounded enough
        # (OS + GPU label + VRAM + RAM + an optional DUAL-LANE flag) that overflow in practice
        # would only happen on an extremely narrow terminal, where it just wraps instead.
        lines.append(f"  System   : {_format_hardware_info(hw, parallel_active=has_parallel)}")
        benchmark_note = _format_benchmark_note(hw)
        if benchmark_note:
            lines.append(f"             {benchmark_note}")

        # "Connected", not "Joined" -- _user_first_seen never resets (it's truly "first ever seen",
        # which stays useful for _user_color()'s stable assignment order, so it's kept for that),
        # but showing it here as a duration was misleading: it just grew forever and never
        # reflected the CURRENT online streak (Nick's ask -- "it never resets"). _user_connected_since
        # is the same min-across-lanes pattern, but tracks each streak's own start (reset in
        # /get_work and /submit_work whenever a lane was previously offline -- see those handlers).
        connected_since = min((_user_connected_since[lid] for lid in lane_ids if lid in _user_connected_since), default=None)
        connected_text = _relative_time(now - connected_since) if connected_since else "unknown"
        lines.append(f"  Connected: {connected_text}")

        combined_stats = {}
        for lid in lane_ids:
            lane_stats = user_stats.get(lid, {})
            for k in _PROGRESS_SUM_KEYS.get(mode, []):
                combined_stats[k] = combined_stats.get(k, 0) + lane_stats.get(k, 0)
        lines.append(_truncate(f"  Progress : {_format_progress_line(mode, combined_stats)}", box_w))

        lines.append(f"{u_color}└{'─' * box_w}┘{Colors.RESET}")
        lines.append("")

    if not online:
        msg = "No volunteers online right now." if known else "No volunteers have connected yet."
        lines.append(f"  {Colors.GRAY}{msg}{Colors.RESET}")
        lines.append("")

    return lines

def _build_events_lines(width: int = None) -> list:
    """The recent-events tail -- split out from _build_connections_lines() (see that function's
    comment) so it can be its own panel (bottom-right in the textual layout) instead of trailing
    off the bottom of a long connections list where it used to get scrolled out of view on a busy
    campaign. `width` is the caller's actual widget content width -- see the matching comment in
    _build_connections_lines() for why this can't just be the raw terminal width."""
    term_width = width if width else max(60, min(shutil.get_terminal_size((100, 24)).columns, 160))
    term_width = max(20, term_width)  # see the matching comment in _build_connections_lines()
    box_w = term_width - 2
    lines = []
    if not _recent_events:
        lines.append(f"  {Colors.GRAY}(none yet){Colors.RESET}")
    event_prefix_len = len("  HH:MM:SS ") + 11  # timestamp + fixed-width user field
    for ts, ev_mode, ev_user, symbol, symbol_color, message in list(_recent_events)[::-1]:
        u_color = _user_color(ev_user)
        user_field = f"{u_color}{ev_user:<10}{Colors.RESET}" if ev_user else " " * 10
        ts_text = f"{Colors.DIM}{datetime.fromtimestamp(ts).strftime('%H:%M:%S')}{Colors.RESET}"
        msg = _truncate(message, max(10, box_w - event_prefix_len - 2))
        lines.append(f"  {ts_text} {user_field} {symbol_color}{symbol}{Colors.RESET} {msg}")
    return lines

# Everything below replaces the rich.live.Live-based dashboard (which itself replaced four
# hand-rolled ANSI redraw attempts -- a full-screen clear, a per-line cursor-up erase, a
# cursor-up + erase-to-end-of-screen, and a manual alternate-screen-buffer switch). rich alone
# only ever solved the REDRAW problem -- it has no concept of keyboard-driven navigation,
# selection, or focus. Nick asked for a real interactive layout (mode selection as a genuine
# selectable list, not just a display, referencing s-tui's UX) -- that needs an actual
# application framework, not a rendering library. `textual` (rich's own sibling project) is that
# framework: real widgets, real keyboard/mouse events, a proper App/Screen model.

# RichLog, NOT Static -- confirmed live that Static.update() in this textual version (8.2.8)
# can't correctly host a Rich Text/Group carrying pre-existing ANSI styling ("AttributeError:
# 'Text'/'Group' object has no attribute 'render_strips'"), since Static's content pipeline goes
# through textual's own newer "Visual" protocol, which doesn't cleanly round-trip an
# already-ANSI-styled Rich renderable the way it does plain textual markup strings. RichLog is
# the widget textual itself documents for hosting arbitrary Rich renderables robustly (it's built
# for exactly this -- writing pre-rendered rich content into a pane) -- clear() + write() fresh
# content each cycle instead of Static's update(), since this is a periodic full replace, not an
# appending log.
class _HeaderPanel(RichLog):
    """Full-width top bar (see _build_top_header_lines()): mode + online/offline counts + clock,
    plus a global campaign progress bar. Its own panel, spanning the whole app width above the
    sidebar/connections/events split -- previously this content opened the connections panel and
    was constrained to that panel's narrower width, per Nick's ask. Always exactly 3 content
    lines (including a blank separating line), so no scrollbar."""

    def __init__(self, **kwargs):
        super().__init__(wrap=False, markup=False, auto_scroll=False, max_lines=3, **kwargs)

    def on_mount(self) -> None:
        self.refresh_content()
        self.set_interval(1, self.refresh_content)

    def refresh_content(self) -> None:
        try:
            lines = _build_top_header_lines(width=self.content_size.width or None)
        except Exception as e:
            lines = [f"Header panel render error: {e}"]
        self.clear()
        for line in lines:
            self.write(Text.from_ansi(line, no_wrap=True, overflow="crop"))

class _ConnectionsPanel(RichLog):
    """Right side, top: the per-machine panels (see _build_connections_lines()) -- unchanged
    content logic from the rich version, just living in its own textual widget now instead of
    being concatenated with the recent-events tail into one combined region."""

    def __init__(self, **kwargs):
        super().__init__(wrap=False, markup=False, auto_scroll=False, **kwargs)

    def on_mount(self) -> None:
        self.refresh_content()
        self.set_interval(1, self.refresh_content)

    def refresh_content(self) -> None:
        try:
            # content_size, not the raw terminal size -- this panel is only PART of the screen
            # (right of the 32-column sidebar, inside its own border), so building content at the
            # full terminal width overflowed the widget and got cropped on a small window
            # (confirmed live: the header's right-aligned clock and each panel's "ONLINE" badge
            # were invisible). 0 during the very first refresh_content() call in on_mount() (before
            # the widget has been laid out at all) falls back to _build_connections_lines()'s own
            # terminal-size default rather than collapsing to the width-1 floor.
            lines = _build_connections_lines(width=self.content_size.width or None)
        except Exception as e:
            lines = [f"Connections panel render error: {e}"]
        self.clear()
        for line in lines:
            # Text.from_ansi so the existing Colors.*-embedded escape codes render as real color
            # instead of literal escape bytes -- RichLog (unlike Static here) handles this fine.
            self.write(Text.from_ansi(line, no_wrap=True, overflow="crop"))

class _EventsPanel(RichLog):
    """Right side, bottom: the recent-events tail (see _build_events_lines()). Content is always
    capped at _recent_events' own maxlen (10), so this panel is sized to fit exactly that many
    lines with no scrollbar -- there's never more content than fits, so a scrollbar here was just
    wasted space plus a misleading affordance (nothing to scroll TO)."""

    def __init__(self, **kwargs):
        super().__init__(wrap=False, markup=False, auto_scroll=False, max_lines=_recent_events.maxlen, **kwargs)

    def on_mount(self) -> None:
        self.refresh_content()
        self.set_interval(1, self.refresh_content)

    def refresh_content(self) -> None:
        try:
            lines = _build_events_lines(width=self.content_size.width or None)
        except Exception as e:
            lines = [f"Events panel render error: {e}"]
        self.clear()
        for line in lines:
            self.write(Text.from_ansi(line, no_wrap=True, overflow="crop"))

def _seed_startup_events(captured_text: str) -> None:
    """Feeds captured stdout (the RAG/finetune/audit chunk-scan summaries normally printed by
    *_initialize_chunks() before anything else exists) into _recent_events directly, instead of
    letting log_event() print them -- there's no console up yet to print them TO. This is what
    lets the textual console open already showing "what happened at startup" in its Events panel
    instead of the operator seeing a burst of plain scrolling text and then a hard cut to the
    panel UI (confirmed live -- Nick saw that flash and asked for it to land in the panel)."""
    for line in captured_text.splitlines():
        line = line.strip()
        if not line:
            continue
        _recent_events.append((time.time(), "admin", "", "•", Colors.GRAY, line))

_MODE_ORDER = ["idle", "rag", "finetune", "audit"]

# Advanced Settings (Collapsible, collapsed by default -- these are destructive campaign-data
# wipes, not everyday actions, so they live tucked away rather than in the main sidebar flow
# where the old CLI startup menu used to put them alongside ordinary mode selection).
_RESET_LABELS = {
    "reset_rag": "Reset RAG campaign",
    "reset_finetune": "Reset Finetune campaign",
    "reset_both": "Reset BOTH campaigns",
}

class CubyzAdminApp(App):
    """The interactive admin console -- left: mode selection (a real selectable RadioSet, not
    just a display, per Nick's s-tui reference) + control options, spanning the FULL height top to
    bottom; right: the mode/online/offline/clock bar, connections, and recent events stacked in
    their own column, sized to match that column's width rather than the whole screen. Runs in its
    own background thread with its own asyncio event loop (see run_textual_console_if_tty()) so it
    can coexist with uvicorn's event loop in the same process while still reading the server's live
    in-memory state directly."""

    CSS = """
    Screen { layout: horizontal; }
    #sidebar { width: 32; border: solid $accent; padding: 1; }
    #main { layout: vertical; }
    #topbar { height: 5; border: solid $accent; scrollbar-size: 0 0; }
    #connections { height: 1fr; border: solid $accent; overflow-y: auto; }
    #events { height: 12; border: solid $accent; scrollbar-size: 0 0; }
    RadioSet { margin-bottom: 1; }
    #advanced { margin-top: 1; }
    #advanced Button { margin-bottom: 1; width: 100%; }
    """
    BINDINGS = [("q", "quit", "Quit"), ("r", "refresh_now", "Refresh now")]

    def __init__(self):
        super().__init__()
        # Guards against the mode RadioSet's own on_radio_set_changed handler firing again (and
        # re-calling set_mode()) when THIS app is the one that just programmatically set the
        # selection to reflect a mode change made elsewhere (the HTTP /admin/mode endpoint, or
        # the startup menu) -- without this, syncing the display would loop back into itself.
        self._syncing_mode_display = False
        # Reset buttons are two-step (arm, then confirm) instead of a plain click, since these
        # wipe campaign data -- see on_button_pressed(). _armed_reset is the button id currently
        # waiting on a confirm click; _armed_timer auto-disarms it if that confirm doesn't come.
        self._armed_reset = None
        self._armed_timer = None

    def compose(self) -> ComposeResult:
        with Vertical(id="sidebar"):
            yield Static("[b]Campaign Mode[/b]")
            with RadioSet(id="mode_select"):
                for m in _MODE_ORDER:
                    yield RadioButton(m.upper(), value=(m == CURRENT_MODE), id=f"mode_{m}")
            yield Static("\n[b]Control Options[/b]\n[dim]q[/dim] Quit\n[dim]r[/dim] Refresh now")
            with Collapsible(title="Advanced Settings", collapsed=True, id="advanced"):
                yield Button(_RESET_LABELS["reset_rag"], id="reset_rag", variant="warning")
                yield Button(_RESET_LABELS["reset_finetune"], id="reset_finetune", variant="warning")
                yield Button(_RESET_LABELS["reset_both"], id="reset_both", variant="error")
            yield Static(id="hint", markup=True)
        with Vertical(id="main"):
            yield _HeaderPanel(id="topbar")
            yield _ConnectionsPanel(id="connections")
            yield _EventsPanel(id="events")

    def on_mount(self) -> None:
        self.set_interval(2, self._sync_mode_display)

    def _sync_mode_display(self) -> None:
        """Keeps the RadioSet in sync with CURRENT_MODE when it changes from somewhere OTHER
        than this panel -- the existing POST /admin/mode HTTP endpoint, or another admin's own
        console -- so this console never shows a stale selection."""
        radio_set = self.query_one("#mode_select", RadioSet)
        wanted_id = f"mode_{CURRENT_MODE}"
        pressed = radio_set.pressed_button
        if pressed is not None and pressed.id == wanted_id:
            return
        self._syncing_mode_display = True
        try:
            for button in radio_set.query(RadioButton):
                button.value = (button.id == wanted_id)
        finally:
            self._syncing_mode_display = False

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        if self._syncing_mode_display:
            return
        new_mode = event.pressed.id.removeprefix("mode_")
        if new_mode == CURRENT_MODE:
            return
        try:
            # Reuses the exact same validated, logged mode-switch path the HTTP /admin/mode
            # endpoint uses -- set_mode() is a plain function underneath the @app.post
            # decorator, callable directly, so there's no reason to duplicate its RAG-completion
            # guard or its logging/persistence side effects here.
            set_mode(new_mode)
        except HTTPException as e:
            self.query_one("#hint", Static).update(f"[red]{e.detail}[/red]")
            self._sync_mode_display()  # revert the visible selection -- the switch was refused

    def action_refresh_now(self) -> None:
        self.query_one(_HeaderPanel).refresh_content()
        self.query_one(_ConnectionsPanel).refresh_content()
        self.query_one(_EventsPanel).refresh_content()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn_id = event.button.id
        if btn_id not in _RESET_LABELS:
            return
        if self._armed_reset == btn_id:
            # Second click on the already-armed button -- this IS the confirmation.
            if self._armed_timer is not None:
                self._armed_timer.stop()
            self._armed_reset = None
            self._armed_timer = None
            event.button.label = _RESET_LABELS[btn_id]
            self._execute_reset(btn_id)
            return
        # First click on this button -- arm it, and disarm whichever other one (if any) was
        # already armed, so only one reset can ever be mid-confirmation at a time.
        if self._armed_reset is not None:
            if self._armed_timer is not None:
                self._armed_timer.stop()
            try:
                self.query_one(f"#{self._armed_reset}", Button).label = _RESET_LABELS[self._armed_reset]
            except Exception:
                pass
        self._armed_reset = btn_id
        event.button.label = "Click again to CONFIRM"
        self._armed_timer = self.set_timer(5, lambda: self._disarm_reset(btn_id))

    def _disarm_reset(self, btn_id: str) -> None:
        if self._armed_reset != btn_id:
            return
        self._armed_reset = None
        self._armed_timer = None
        try:
            self.query_one(f"#{btn_id}", Button).label = _RESET_LABELS[btn_id]
        except Exception:
            pass

    def _execute_reset(self, btn_id: str) -> None:
        try:
            if btn_id == "reset_rag":
                rag_execute_hard_reset()
            elif btn_id == "reset_finetune":
                finetune_execute_hard_reset()
            elif btn_id == "reset_both":
                rag_execute_hard_reset()
                finetune_execute_hard_reset()
            self.query_one("#hint", Static).update(f"[green]{_RESET_LABELS[btn_id]} complete.[/green]")
        except Exception as e:
            self.query_one("#hint", Static).update(f"[red]Reset failed: {e}[/red]")
        self.query_one(_ConnectionsPanel).refresh_content()
        self.query_one(_EventsPanel).refresh_content()

# NOTE ON THREADING (learned the hard way -- confirmed live, not theorized): the ORIGINAL plan
# here was "run textual's App in a background thread with its own event loop, same shape as the
# rich Live loop it replaced." That's broken: textual's Linux/Mac driver calls signal.signal()
# during startup (to support Ctrl+Z suspend/resume), and Python's signal module hard-requires
# that only ever happen on the MAIN thread of the MAIN interpreter -- calling it from a
# background thread raises "ValueError: signal only works in main thread of the main
# interpreter" unconditionally, not something catchable/configurable away. So the whole
# threading model is INVERTED from every previous version of this dashboard: textual now owns
# the MAIN thread (via App.run(), the synchronous blocking entry point), and uvicorn moves to a
# background thread instead.
#
# This is safe on uvicorn's side specifically because uvicorn.Server.serve() (unlike the
# uvicorn.run() convenience wrapper) checks `threading.current_thread() is not
# threading.main_thread()` inside its own capture_signals() context manager and silently skips
# registering signal handlers when that's true, rather than erroring the same way textual does --
# confirmed by reading uvicorn's own source before relying on this, not assumed to be safe.

def _run_uvicorn_in_background():
    config = uvicorn.Config(app, host="0.0.0.0", port=7000, access_log=False)
    server = uvicorn.Server(config)
    asyncio.run(server.serve())

app = FastAPI(title="Cubyz Distributed Dataset Coordinator")

# FastAPI/Starlette runs synchronous "def" route handlers (every route in this file) in a thread
# pool, so two requests genuinely can execute concurrently -- e.g. two lanes on the same dual-lane
# client (see CUBYZ_FOLDING.py's crunch_lane()), or just two different volunteers, both hitting
# /get_work or /submit_work at close to the same instant. Every one of those handlers does a
# read-JSON -> mutate -> write-JSON cycle on lock_state.json; without serializing that whole
# cycle, two concurrent requests can interleave their writes and either silently lose one
# request's update or -- confirmed live under a synthetic concurrent-load test -- corrupt the
# JSON file itself into something no longer parseable at all. One coarse global lock is
# deliberately simple here: campaign state I/O is not a throughput bottleneck at this scale (a
# handful of concurrent volunteers), so there's no reason to risk a more fine-grained scheme's
# deadlock potential for a performance win nothing here needs.
campaign_state_lock = threading.Lock()

# ============================================================
# This server used to be two separate processes (this file, RAG-only, and
# finetune/server_finetune.py) that happened to both bind port 7000 -- meaning only one could
# ever run at a time anyway. Merged into one process that runs BOTH campaigns' state side by
# side and switches which one is being served via CURRENT_MODE, matching what
# CUBYZ_FOLDING.py (the unified client) expects: a "mode" field on /get_work telling it whether
# to do RAG extraction, fine-tune pair generation, or nothing (idle).
#
# RAG and fine-tune chunk_ids are NOT interchangeable even though they can be equal as strings
# -- a fine-tune chunk_id is literally copied from an already-completed RAG chunk_id, so treating
# them as the same lock/completion namespace would be wrong. Their queues, lock files, stats
# files, and hash databases stay fully separate; only the HTTP surface and the online-clients
# roster are unified.
# ============================================================

PIPELINE_ROOT = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(PIPELINE_ROOT)
FINETUNE_ROOT = os.path.join(REPO_ROOT, "finetune")

# --- RAG campaign paths (unchanged from this file's pre-merge state) ---
RAG_SOURCE_DIR = os.path.join(PIPELINE_ROOT, "organized_cubyz_dataset") + os.sep
USERS_DIR = os.path.join(REPO_ROOT, "users")
RAG_LOCK_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "lock_state.json")
RAG_STATS_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "user_stats.json")
RAG_HASH_DB_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "file_hashes.json")
RAG_BACKUP_DIR = os.path.join(REPO_ROOT, "archive", "rag_crunching_campaign_backups")

# --- Fine-tune campaign paths ---
FINETUNE_OUTPUT_DIR = os.path.join(FINETUNE_ROOT, "pairs")
FINETUNE_LOCK_FILE = os.path.join(FINETUNE_ROOT, "campaign_state", "lock_state.json")
FINETUNE_STATS_FILE = os.path.join(FINETUNE_ROOT, "campaign_state", "user_stats.json")
FINETUNE_HASH_DB_FILE = os.path.join(FINETUNE_ROOT, "campaign_state", "file_hashes.json")
FINETUNE_BACKUP_DIR = os.path.join(REPO_ROOT, "archive", "finetune_campaign_backups")

# --- Audit campaign paths (finds and fixes "fact dropped during crunching" bugs in ALREADY
# crunched knowledge_base/*.md content -- the manual work done by hand throughout the 2026-07-18
# RAG debugging session, turned into an ongoing distributed job instead of a one-off pass) ---
KNOWLEDGE_DIR = os.path.join(REPO_ROOT, "knowledge_base")
AUDIT_LOCK_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "audit_lock_state.json")
AUDIT_STATS_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "audit_user_stats.json")
AUDIT_HASH_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "audit_hash_state.json")
AUDIT_PENDING_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "audit_pending_fixes.json")
AUDIT_APPLIED_LOG = os.path.join(PIPELINE_ROOT, "campaign_state", "audit_applied_log.jsonl")
AUDIT_NEEDS_HUMAN_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "audit_needs_human_review.jsonl")
AUDIT_MODEL_ASSIGNMENTS_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "audit_model_assignments.json")

# Model roster for audit mode, split by hardware tier so a weak machine only ever gets assigned a
# model it can actually run and a strong machine gets real capability out of its hardware.
#
# Used to deliberately span multiple vendors/architectures (Qwen, Llama, Gemma, Mistral/Mixtral,
# DeepSeek) so a "different reviewer" meant a genuinely different model's blind spots, not just a
# different size of the same family -- and WITHIN a tier, every concurrently-online volunteer got a
# distinct model from the list, cycling back to the top once every model in the tier was in use.
# Simplified to qwen2.5-coder only, on explicit request, trading that cross-model blind-spot
# diversity away for a single, predictable, code-tuned family -- also more consistent with the rest
# of this project, which already uses qwen2.5-coder (not plain qwen2.5, what this roster used
# before) for RAG/finetune's own hardware-based model picks. One real, immediate side effect: since
# there's only one model per tier now, every online volunteer in the same tier gets the SAME model
# -- the round-robin "distinct model per volunteer" logic in _assign_audit_model still runs, it just
# has nothing left to diversify across. Operators should have these pulled in Ollama ahead of time;
# the client will attempt to pull an assigned model on demand if it isn't present locally.
AUDIT_MODEL_ROSTER = {
    "easy":   ["qwen2.5-coder:3b"],
    "medium": ["qwen2.5-coder:7b"],
    "hard":   ["qwen2.5-coder:14b"],
}
# A brief gap between polls (network hiccup, a slow Ollama call) shouldn't free up a model that's
# genuinely still in use and hand it to someone else -- this is deliberately looser than the 60s
# "online" window used elsewhere for display purposes, since reassigning someone's model out from
# under them mid-session is more disruptive than a leaderboard briefly showing them as offline.
AUDIT_ASSIGNMENT_STALE_SECONDS = 120

audit_model_assignments = {}  # user_id (lowercase) -> {"model": ..., "tier": ..., "last_seen": ...}

# The review/revise role -- judging whether a proposed fix is correct AND whether it silently
# regresses something already-correct -- is a harder task than the "easy" tier's 3B-class models
# reliably handle. Confirmed live during the first real 3-machine test: an "easy"-tier reviewer
# rejected/re-requested-revision on genuinely correct fixes, at one point giving literally
# self-contradictory feedback across rounds on the same chunk (first said a value shouldn't be
# added because it was already present, then two rounds later said the same value was missing and
# must be added) -- 56% of that reviewer's review actions ended up on chunks that never converged
# and had to be escalated to a human, versus a small fraction for the other three volunteers
# combined. "easy" tier can still PROPOSE (simple pattern-matching against source); it just isn't
# offered review/revise work.
HARDWARE_TIER_RANK = {"easy": 1, "medium": 2, "hard": 3}
REVIEW_MIN_TIER = "medium"

# Fixes to "docs" chunks are the highest-consequence in the whole knowledge base -- wiki/FAQ-style
# content that gets quoted close to verbatim in real chat answers, and literally every severe bug
# found during the 2026-07-18 session (healing, multiplayer port/UDP, an entire missing "Great Zig
# Rewrite" section, etc.) lived there. Everything else (codebase config, addon_creator, reviews)
# stays at a single approval to keep the common case fast; "docs" requires a second, independent
# approval before a fix is actually written. A dict (not a hardcoded branch) so this can be
# extended later if evidence from other collections warrants it.
AUDIT_REQUIRED_APPROVALS = {"docs": 2}
AUDIT_DEFAULT_REQUIRED_APPROVALS = 1

def _required_approvals(collection: str) -> int:
    return AUDIT_REQUIRED_APPROVALS.get(collection, AUDIT_DEFAULT_REQUIRED_APPROVALS)

TASK_TIMEOUT = 300

# How many separate nodes must independently give up on the same RAG chunk (each after their own
# internal 3-attempt retry loop) before the server stops handing it back out. See submit_diagnostics()
# -- unlike finetune mode (which always submits a real, if empty, result and so always reaches a
# terminal "completed" state), RAG mode's give-up path makes no submission at all, so without this
# a structurally hard chunk (e.g. code_example content the model can never shape correctly, or a
# fragment from the oversized-unit chunking fallback that's missing its own declaration) gets
# handed to every node in the swarm forever, once every TASK_TIMEOUT, and the campaign can never
# reach 100%. Confirmed live: 'graphics.zig_chunk_20' failed identically 5 times over ~25 minutes.
RAG_GIVE_UP_THRESHOLD = 3

# A chunk this short (same threshold the client uses to cap synthetic_queries) doesn't carry
# enough genuine content for small local models to extract from without fabricating -- verified live
# against qwen2.5-coder:3b/7b/14b: only the 14b tier stayed fully grounded on chunks this thin.
THIN_CONTENT_CHAR_THRESHOLD = 400
MODEL_TIER_RANK = {
    "qwen2.5-coder:3b": 1,
    "qwen2.5-coder:7b": 2,
    "qwen2.5-coder:14b": 3,
    "qwen3-coder:30b": 4,
}
THIN_CHUNK_MIN_TIER = 3  # requires a qwen2.5-coder:14b-or-better client

# ============================================================
# CLIENT VERSIONING -- old clients (the archived per-OS scripts, RAG_FOLDING.py,
# FINETUNE_FOLDING.py) don't send a client_version at all and don't understand the "mode"
# field this server now returns; letting them through would silently misdispatch work to them.
# get_work/submit_work reject anything below MIN_CLIENT_VERSION with HTTP 426 and a message
# telling the operator to update, rather than accepting and mishandling it.
# ============================================================
MIN_CLIENT_VERSION = "1.3.0"
LATEST_CLIENT_VERSION = "1.3.0"
CLIENT_DOWNLOAD_URL = "https://raw.githubusercontent.com/iNiKKo/Cubyz-AI/main/CUBYZ_FOLDING.py"

def _parse_version(v: str) -> tuple:
    try:
        return tuple(int(p) for p in v.strip().split("."))
    except Exception:
        return (0,)

def _version_rejection_message(client_version: str) -> str:
    return (
        f"Your client is out of date (sent version '{client_version or 'none'}', server requires "
        f">= {MIN_CLIENT_VERSION}). You must update to the new version. Download: {CLIENT_DOWNLOAD_URL}"
    )

# "idle": server up, no campaign handing out work. Set at startup via server_startup_gate() and
# switchable afterward without restarting via POST /admin/mode?mode=idle|rag|finetune.
CURRENT_MODE = "idle"
SERVER_STATE_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "server_mode_state.json")
# Central collection point for client-side diagnostics (task_gave_up / task_cancelled events only
# -- see CUBYZ_FOLDING.py's log_diagnostic()/submit_diagnostic_to_server()). Every volunteer's
# local ~/.cubyz_node_diagnostics.jsonl stays on their own machine; this is the aggregated view
# across all of them, since the operator otherwise has no way to see any machine's data but their
# own.
CLIENT_DIAGNOSTICS_FILE = os.path.join(PIPELINE_ROOT, "campaign_state", "client_diagnostics.jsonl")

# Audit mode is a genuine two-role conversation, not blind independent voting: one volunteer's LLM
# PROPOSES a fix, a DIFFERENT volunteer's LLM (never the same one) REVIEWS that specific proposal --
# sees the proposer's stated reasoning, checks it's real against raw_content, and explicitly checks
# the fix doesn't drop/contradict anything the ORIGINAL content already had right (the regression
# check). The reviewer can approve (fix gets applied), reject (proposer's diagnosis itself was
# wrong -- goes back for a completely fresh, independent proposal), or request revision (the
# diagnosis is right but the fix itself needs work -- goes out with the reviewer's specific
# feedback attached for someone else to take another pass at). Capped at MAX_REVIEW_ROUNDS
# propose/reject/revise cycles per chunk before giving up and flagging it for an actual human
# instead of ping-ponging between LLMs forever on a chunk they can't agree on.
MAX_REVIEW_ROUNDS = 3

rag_chunk_queue = []
finetune_chunk_queue = []
audit_chunk_queue = []
audit_total_chunks = 0
audit_completion_log = []
# True campaign size, including chunks skipped from the queues above because they're already
# fully completed and unchanged (see rag_initialize_chunks()/finetune_initialize_chunks()) --
# *_chunk_queue only holds chunks still available to hand out, so once enough of a campaign is
# done that some source files become fully-skippable on a restart, len(*_chunk_queue) alone
# undercounts the real total and the reported percentage can exceed 100%.
rag_total_chunks = 0
finetune_total_chunks = 0
online_clients = {}  # unified roster -- one client identity now, regardless of which mode it's working in
ONLINE_STALE_SECONDS = 60  # a client not heard from in this long is treated as offline everywhere

# ETA estimation: a rolling log of completion timestamps per campaign, used to derive the
# aggregate throughput of ALL currently-active nodes combined (chunks/sec), not any single
# node's solo rate. Averaging individual clients' own "time remaining" estimates would be wrong
# -- it ignores parallelism (N nodes working together finish in ~1/N the time a lone node's
# estimate implies) and is noisy for a node that just joined. Computing one aggregate rate
# server-side from real completion events avoids both problems and needs no client-side timing.
#
# This window-based method is now the FALLBACK -- see _capacity_based_eta() below for the
# preferred path, used whenever at least one online client has reported a real measured speed.
# The window method stayed noisy in practice: multi-round audit conversations resolve in bursts,
# so a lucky cluster of completions landing inside ETA_WINDOW_SECONDS swung the estimate wildly,
# and a fast node joining didn't move the number until enough of ITS completions accumulated in
# the window -- confirmed live when adding a fast "easy"-tier node barely moved a ~6h estimate.
ETA_WINDOW_SECONDS = 600  # only the last 10 minutes of completions count toward the current rate
ETA_MIN_SAMPLES = 3       # below this many recent completions, the rate is too noisy to trust
rag_completion_log = []
finetune_completion_log = []


class RAGNode(BaseModel):
    chunk_id: str
    summary: str
    comprehensive_explanation: str
    symbols: List[str] = []
    concepts: List[str] = []
    keywords: List[str] = []
    chunk_type: Optional[str] = None
    code_example: Optional[str] = None
    synthetic_queries: List[str]
    title: str
    user_id: str = Field(..., min_length=3, max_length=12, pattern="^[a-zA-Z]+$")
    lines_crunched: Optional[int] = 0


class FinetunePairsSubmission(BaseModel):
    chunk_id: str
    source_type: str  # docs | codebase | reviews
    pairs: List[dict]  # [{"instruction": ..., "response": ...}, ...]
    user_id: str = Field(..., min_length=3, max_length=12, pattern="^[a-zA-Z]+$")
    lines_crunched: Optional[int] = 0


class UnifiedSubmission(BaseModel):
    # "mode" defaults to "rag" so an old, not-yet-updated RAG-only client (which never sends this
    # field) still submits correctly as long as the server happens to be in RAG mode -- the same
    # spirit as CUBYZ_FOLDING.py defaulting an absent /get_work "mode" to "rag".
    mode: Literal["rag", "finetune", "audit"] = "rag"
    client_version: str = ""  # absent (old client) is treated the same as "0.0.0" -- see _parse_version
    chunk_id: str
    user_id: str = Field(..., min_length=3, max_length=12, pattern="^[a-zA-Z]+$")
    lines_crunched: Optional[int] = 0
    # RAG-mode fields
    summary: Optional[str] = None
    comprehensive_explanation: Optional[str] = None
    symbols: List[str] = []
    concepts: List[str] = []
    keywords: List[str] = []
    chunk_type: Optional[str] = None
    code_example: Optional[str] = None
    synthetic_queries: List[str] = []
    title: Optional[str] = None
    # Fine-tune-mode fields
    source_type: Optional[str] = None
    pairs: List[dict] = []
    # Audit-mode fields -- see _submit_audit_work(). task_type tracks which of the three roles
    # this submission is responding as; verdict/reason/corrected_* are the PROPOSER's (or
    # REVISER's) fields, review_verdict/review_feedback are the REVIEWER's.
    task_type: Optional[Literal["propose", "review", "revise"]] = None
    verdict: Optional[Literal["ok", "needs_fix"]] = None
    reason: str = ""
    corrected_summary: Optional[str] = None
    corrected_explanation: Optional[str] = None
    corrected_related_questions: List[str] = []
    review_verdict: Optional[Literal["approve", "reject", "revise"]] = None
    review_feedback: str = ""


def read_json_file(path: str, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default

def write_json_file(path: str, data, label: str = "file"):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"[X] Failed to write {label} to disk: {e}")

def append_jsonl(path: str, record: dict, label: str = "record"):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")
    except Exception as e:
        print(f"[X] Failed to append {label} to disk: {e}")

def load_lock_state(path: str) -> dict:
    return read_json_file(path, {"locked": {}, "completed": []})

def save_lock_state(path: str, state: dict):
    write_json_file(path, state, "lock state")

def load_user_stats(path: str) -> dict:
    return read_json_file(path, {})

def save_user_stats(path: str, stats: dict):
    write_json_file(path, stats, "user stats")

def load_server_mode_state() -> dict:
    return read_json_file(SERVER_STATE_FILE, {"mode": "idle", "clean_shutdown": True})

def save_server_mode_state(mode: str, clean_shutdown: bool):
    write_json_file(SERVER_STATE_FILE, {"mode": mode, "clean_shutdown": clean_shutdown}, "server mode state")

def prune_stale_locks(state: dict) -> bool:
    now = time.time()
    stale_keys = [
        chunk_id for chunk_id, info in state["locked"].items()
        if now - info["timestamp"] > TASK_TIMEOUT
    ]
    for key in stale_keys:
        stale_info = state["locked"].pop(key)
        print(f"[!] Task '{key}' timed out from user '{stale_info['user_id']}'. Released back to queue.")
    return bool(stale_keys)

def _record_completion(completion_log: list):
    """Appends a completion event (now) to a campaign's rolling log and drops anything older than
    ETA_WINDOW_SECONDS, so the log stays bounded and every reading reflects only recent activity."""
    now = time.time()
    completion_log.append(now)
    cutoff = now - ETA_WINDOW_SECONDS
    while completion_log and completion_log[0] < cutoff:
        completion_log.pop(0)

def _estimate_eta_seconds(completion_log: list, remaining_chunks: int):
    """Aggregate throughput across every node that has completed a chunk in the last
    ETA_WINDOW_SECONDS, applied to however many chunks are left. Returns None when there isn't
    enough recent data yet to trust a rate (campaign just started/resumed, or gone quiet)."""
    if remaining_chunks <= 0:
        return 0.0
    now = time.time()
    cutoff = now - ETA_WINDOW_SECONDS
    recent = [t for t in completion_log if t >= cutoff]
    if len(recent) < ETA_MIN_SAMPLES:
        return None
    span = max(now - min(recent), 1.0)
    rate = len(recent) / span  # combined chunks/sec across all active nodes
    return remaining_chunks / rate

def _capacity_based_eta(remaining_units: float, avg_actions_per_unit: float = 1.0):
    """Preferred ETA path: sum 1/speed across every currently-online client that has reported a
    real measured speed (seconds/task, from that client's own recent dispatch->submit timings --
    see CUBYZ_FOLDING.py's task_durations), for a combined actions/sec capacity. Unlike the
    window-based _estimate_eta_seconds, this reacts the instant a node joins or leaves (its speed
    is known immediately, not inferred from waiting for enough of its completions to land in a
    rolling window) and doesn't swing on how bursty recent completion timing happened to be.
    avg_actions_per_unit converts actions/sec into units/sec for campaigns (audit) where one
    resolved unit costs more than one submission. Returns None if no online client has reported a
    speed yet (e.g. right after a restart, before any client's first get_work poll lands) -- the
    caller should fall back to _estimate_eta_seconds in that case."""
    if remaining_units <= 0:
        return 0.0
    now = time.time()
    capacity = 0.0  # actions/sec, summed across every online node with a known speed
    for info in online_clients.values():
        speed = info.get("speed")
        if speed and speed > 0 and now - info["timestamp"] < ONLINE_STALE_SECONDS:
            capacity += 1.0 / speed
    if capacity <= 0:
        return None
    return (remaining_units * avg_actions_per_unit) / capacity

def _eta_seconds(completion_log: list, remaining_units: float, avg_actions_per_unit: float = 1.0):
    """Tries the capacity-based estimate first (see _capacity_based_eta), falling back to the
    older completion-window method when no online client has reported a speed yet."""
    capacity_eta = _capacity_based_eta(remaining_units, avg_actions_per_unit)
    if capacity_eta is not None:
        return capacity_eta
    return _estimate_eta_seconds(completion_log, remaining_units)

def _audit_avg_actions_per_chunk(actions_count: int, completed_since_tracking: int) -> float:
    """A resolved audit chunk usually costs more than one submission (a propose plus at least one
    independent review, sometimes a revise round or a second docs approval), so a raw actions/sec
    capacity overstates how fast chunks actually resolve unless converted through this ratio.

    Both arguments are measured from the SAME starting point -- see "actions_count" and
    "actions_baseline_completed" in AUDIT_LOCK_FILE's schema, both persisted (not bare in-memory
    globals) so this survives a restart. actions_baseline_completed snapshots how many chunks were
    already completed the moment tracking started, so completed_since_tracking is a delta measured
    from that same zero point as actions_count -- NOT the campaign's full historical completed
    count. Dividing actions_count by the full historical total instead (either mismatch -- a fresh
    in-memory counter against a persisted historical total, or a fresh persisted counter still
    divided by the un-baselined total) collapses the ratio toward the 1.0 floor for a long time
    after every restart or deploy, since the numerator starts at/near 0 while the denominator is
    already large -- confirmed live, this made a freshly-restarted server's ETA come out 2.5-3x too
    optimistic (looked like every chunk only ever needed one action). 2.0 (propose + one review,
    the most common real shape) is used as a prior until enough real samples exist to trust the
    observed ratio."""
    if actions_count < 10 or completed_since_tracking <= 0:
        return 2.0
    return max(1.0, actions_count / completed_since_tracking)

# ============================================================
# RAG CAMPAIGN -- chunk ingestion, hard reset (unchanged logic from the pre-merge server.py,
# except execute_hard_reset's backup copy now uses os.path.basename()/a literal "users" name
# when joining onto session_backup -- the original passed the source's own ABSOLUTE path as the
# second os.path.join() argument, which Python discards all prior components for, so every
# "backup" copy was actually just the file copied onto itself and never actually landed in
# session_backup at all. finetune/server_finetune.py's equivalent code already used the correct
# pattern; this merge adopts that version for both campaigns.
# ============================================================

def rag_initialize_empty_state():
    # RAG_STATS_FILE (per-user chunks_completed/lines_crunched -- the leaderboard) is deliberately
    # left untouched here: a hard reset clears the campaign so chunks can be redone (e.g. after a
    # crunching-prompt fix), but a volunteer's lifetime contribution total should never drop back
    # to 0 just because the campaign queue was rebuilt.
    for f in (RAG_LOCK_FILE, RAG_HASH_DB_FILE):
        if os.path.exists(f):
            os.remove(f)
    if os.path.exists(USERS_DIR):
        shutil.rmtree(USERS_DIR)
    os.makedirs(USERS_DIR, exist_ok=True)

    save_lock_state(RAG_LOCK_FILE, {"locked": {}, "completed": []})
    write_json_file(RAG_HASH_DB_FILE, {}, "hash db")
    print("\n[✓] RAG campaign structures initialized back to 0 (contribution stats preserved).")

def rag_execute_hard_reset():
    print("\n[!] Initializing RAG System Hard Reset & Backup Sequence...")
    os.makedirs(RAG_BACKUP_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_backup = os.path.join(RAG_BACKUP_DIR, f"backup_{timestamp}")
    os.makedirs(session_backup, exist_ok=True)

    files_backed_up = 0
    for f in (RAG_LOCK_FILE, RAG_STATS_FILE, RAG_HASH_DB_FILE):
        if os.path.exists(f):
            shutil.copy2(f, os.path.join(session_backup, os.path.basename(f)))
            files_backed_up += 1

    if os.path.exists(USERS_DIR) and os.listdir(USERS_DIR):
        shutil.copytree(USERS_DIR, os.path.join(session_backup, "users"), dirs_exist_ok=True)
        files_backed_up += 1

    if files_backed_up > 0:
        print(f"[✓] Successfully archived RAG session data to: {session_backup}")
    else:
        print("[~] No historical RAG operational data found to archive.")

    rag_initialize_empty_state()

def calculate_file_hash(file_path: str) -> str:
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while block := f.read(8192):
                sha256.update(block)
        return sha256.hexdigest()
    except Exception:
        return ""

def _is_chunk_set_unchanged(file_chunks: list, file: str, f_hash: str, old_hashes: dict, completed_chunks: set) -> bool:
    all_completed = len(file_chunks) > 0 and all(c["chunk_id"] in completed_chunks for c in file_chunks)
    return file in old_hashes and old_hashes[file] == f_hash and all_completed

def _classify_role_context(file_lower: str, tier_path: str) -> str:
    if file_lower.startswith("docs"):
        return "DEFINITIVE_WIKI_DOCUMENTATION"
    elif file_lower.startswith("codebase"):
        return "FUNCTIONAL_CODEBASE_LOGIC"
    elif file_lower.startswith("addon_creator") or "addon" in tier_path.lower():
        return "ADDON_STUDIO_BLUEPRINTS"
    else:
        is_wiki_ext = file_lower.endswith(('.md', '.txt', '.html'))
        return "DEFINITIVE_WIKI_DOCUMENTATION" if is_wiki_ext else "FUNCTIONAL_CODEBASE_LOGIC"

def _structural_chunks(lines: list, target: int = 150, max_size: int = 300, overlap: int = 30) -> list:
    """Splits a file's lines into chunks that respect logical boundaries instead of blindly
    slicing every `target` lines regardless of what's in the middle. A fixed-size sliding window
    doesn't know where a function or doc section ends, so a chunk boundary could fall in the
    middle of one, handing the crunching LLM two structurally incoherent halves -- directly
    feeding "vague/incomplete explanation" bugs (see the stub-page-hallucination and
    gameplay_controls.md under-generation bugs documented in finetune/README.md, and this
    project's repeated live-verification findings that source coherence drives crunch quality).

    Boundary detection is language-agnostic on purpose (one heuristic instead of separate Zig/JS/
    markdown parsers, each with its own edge cases to get wrong): a new logical unit starts at any
    unindented (column-0) non-blank line that is either the first line of the file or immediately
    preceded by a blank line. This matches how top-level functions/structs are conventionally
    separated by a blank line in Zig/JS, and how markdown headers work too, without needing a
    per-language keyword list.

    Consecutive small units are greedily merged up to `target` lines (matching the previous flat
    chunk size, so typical output stays similarly sized). A single unit larger than `target` but
    not larger than `max_size` becomes its own chunk rather than being split (a complete large
    function beats an arbitrarily-cut one). Only a single unit that's *itself* bigger than
    `max_size` falls back to the old sliding-window slicing, scoped to just that unit, so no chunk
    is ever unbounded.
    """
    if not lines:
        return []

    boundaries = []
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        if line == line.lstrip():
            if i == 0 or not lines[i - 1].strip():
                boundaries.append(i)
    if not boundaries or boundaries[0] != 0:
        boundaries.insert(0, 0)

    spans = [(boundaries[k], boundaries[k + 1]) for k in range(len(boundaries) - 1)]
    spans.append((boundaries[-1], len(lines)))

    chunk_spans = []
    current_start = spans[0][0]
    current_end = spans[0][0]
    step = max(target - overlap, 1)

    for start, end in spans:
        if end - start > max_size:
            if current_end > current_start:
                chunk_spans.append((current_start, current_end))
            for i in range(start, end, step):
                chunk_spans.append((i, min(i + target, end)))
                if i + target >= end:
                    break
            current_start = current_end = end
            continue

        if end - current_start > target and current_end > current_start:
            chunk_spans.append((current_start, current_end))
            current_start = start

        current_end = end

    if current_end > current_start:
        chunk_spans.append((current_start, current_end))

    return ["".join(lines[s:e]) for s, e in chunk_spans]

def rag_initialize_chunks(verbose: bool = True):
    global rag_total_chunks
    chunk_size, overlap = 150, 30
    step = chunk_size - overlap
    rag_total_chunks = 0

    if not os.path.exists(RAG_SOURCE_DIR):
        print(f"[X] Error: Organized source workspace not found at '{RAG_SOURCE_DIR}'!")
        sys.exit(1)

    lock_state = load_lock_state(RAG_LOCK_FILE)
    completed_chunks = set(lock_state.get("completed", []))
    old_hashes = read_json_file(RAG_HASH_DB_FILE, {})

    current_hashes = {}
    skipped_unchanged_count = 0
    total_scanned_files = 0

    for tier in ["easy", "medium", "hard"]:
        tier_path = os.path.join(RAG_SOURCE_DIR, tier)
        if not os.path.exists(tier_path):
            continue

        for file in os.listdir(tier_path):
            file_path = os.path.join(tier_path, file)
            if not os.path.isfile(file_path):
                continue

            total_scanned_files += 1
            f_hash = calculate_file_hash(file_path)
            current_hashes[file] = f_hash

            try:
                if file.lower().endswith('.json') or file.lower().startswith('reviews'):
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        review_array = json.load(f)

                    file_chunks = []
                    for review_item in review_array:
                        review_raw_content = review_item.get("raw_content", "")
                        file_chunks.append({
                            "chunk_id": review_item.get("chunk_id"),
                            "file_name": review_item.get("file_name", "unknown.zig"),
                            "relative_path": review_item.get("relative_path", "unknown_path"),
                            "directory_context": f"{tier} | GITHUB_REVIEWS",
                            "chunk_index": review_item.get("chunk_index", 0),
                            "difficulty": tier,
                            "raw_content": review_raw_content,
                            "requires_strong_model": len(review_raw_content) < THIN_CONTENT_CHAR_THRESHOLD
                        })

                    rag_total_chunks += len(file_chunks)
                    if _is_chunk_set_unchanged(file_chunks, file, f_hash, old_hashes, completed_chunks):
                        skipped_unchanged_count += 1
                        continue

                    rag_chunk_queue.extend(file_chunks)

                else:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()

                    isolated_role_context = _classify_role_context(file.lower(), tier_path)

                    file_chunks = []
                    for idx, chunk_raw_content in enumerate(_structural_chunks(lines, chunk_size, chunk_size * 2, overlap)):
                        file_chunks.append({
                            "chunk_id": f"{file}_chunk_{idx}",
                            "file_name": file,
                            "relative_path": f"{tier}/{file}",
                            "directory_context": f"{tier} | {isolated_role_context}",
                            "chunk_index": idx,
                            "difficulty": tier,
                            "raw_content": chunk_raw_content,
                            "requires_strong_model": len(chunk_raw_content) < THIN_CONTENT_CHAR_THRESHOLD
                        })

                    rag_total_chunks += len(file_chunks)
                    if _is_chunk_set_unchanged(file_chunks, file, f_hash, old_hashes, completed_chunks):
                        skipped_unchanged_count += 1
                        continue

                    rag_chunk_queue.extend(file_chunks)

            except Exception as e:
                print(f"[!] Error parsing file entry {file}: {e}")

    write_json_file(RAG_HASH_DB_FILE, current_hashes, "hash db")
    os.makedirs(USERS_DIR, exist_ok=True)

    if verbose:
        print("\n" + "─"*55)
        print("               RAG PIPELINE METRICS                   ")
        print("─"*55)
        print(f" 📂 Total Workspace Files Found:  {total_scanned_files}")
        print(f" ⏭️ Bypassed (Fully Completed):   {skipped_unchanged_count}")
        print(f" 🔥 Active Task Targets Queued:   {len(rag_chunk_queue)}")
        print(f" 🎯 True Campaign Total:          {rag_total_chunks}")
        print("─"*55 + "\n")

# ============================================================
# FINE-TUNE CAMPAIGN -- chunk ingestion, hard reset (unchanged logic from the pre-merge
# finetune/server_finetune.py).
# ============================================================

def finetune_initialize_empty_state():
    # FINETUNE_STATS_FILE (per-user chunks_completed/pairs_generated -- the leaderboard) is
    # deliberately left untouched here, same reasoning as rag_initialize_empty_state(): the
    # campaign queue resets, but lifetime contribution totals never should.
    for f in (FINETUNE_LOCK_FILE, FINETUNE_HASH_DB_FILE):
        if os.path.exists(f):
            os.remove(f)
    if os.path.exists(FINETUNE_OUTPUT_DIR):
        shutil.rmtree(FINETUNE_OUTPUT_DIR)
    os.makedirs(FINETUNE_OUTPUT_DIR, exist_ok=True)

    save_lock_state(FINETUNE_LOCK_FILE, {"locked": {}, "completed": []})
    write_json_file(FINETUNE_HASH_DB_FILE, {}, "hash db")
    print("\n[OK] Fine-tune campaign structures initialized back to 0 (contribution stats preserved).")

def finetune_execute_hard_reset():
    print("\n[!] Initializing Fine-Tune System Hard Reset & Backup Sequence...")
    os.makedirs(FINETUNE_BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_backup = os.path.join(FINETUNE_BACKUP_DIR, f"backup_{timestamp}")
    os.makedirs(session_backup, exist_ok=True)

    files_backed_up = 0
    for f in (FINETUNE_LOCK_FILE, FINETUNE_STATS_FILE, FINETUNE_HASH_DB_FILE):
        if os.path.exists(f):
            shutil.copy2(f, os.path.join(session_backup, os.path.basename(f)))
            files_backed_up += 1
    if os.path.exists(FINETUNE_OUTPUT_DIR) and os.listdir(FINETUNE_OUTPUT_DIR):
        shutil.copytree(FINETUNE_OUTPUT_DIR, os.path.join(session_backup, "pairs"), dirs_exist_ok=True)
        files_backed_up += 1

    if files_backed_up > 0:
        print(f"[OK] Archived fine-tune session data to: {session_backup}")
    else:
        print("[~] No historical fine-tune operational data found to archive.")
    finetune_initialize_empty_state()

def calculate_content_hash(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode("utf-8")).hexdigest()

# Reproduces filter_codebase_subset.py's qualifies() filter (architectural/conceptual chunks
# only, not per-asset stat blocks or narrow utility code) against knowledge_base-derived records
# instead of the raw users/*/codebase.jsonl crunch it was originally written against -- see
# _parse_kb_md_record's comment for why finetune reads from knowledge_base/ at all now. Keep in
# sync with finetune/scripts/filter_codebase_subset.py's ALWAYS_INCLUDE_TYPES/CONDITIONAL_TYPES/
# CONDITIONAL_MIN_TIER if that script's own filter logic ever changes -- that script is still the
# right place to go inspect/tune the filter by hand, this is just its rule re-applied live.
FINETUNE_CODEBASE_ALWAYS_INCLUDE_TYPES = {"world_generation", "algorithm", "gameplay", "networking"}
FINETUNE_CODEBASE_CONDITIONAL_TYPES = {"implementation", "api", "serialization"}
FINETUNE_CODEBASE_CONDITIONAL_MIN_TIER = {"medium", "hard"}
_FINETUNE_TIER_RE = re.compile(r"\[(easy|medium|hard)/")

def _finetune_codebase_qualifies(record: dict) -> bool:
    chunk_type = record.get("chunk_type")
    if chunk_type in FINETUNE_CODEBASE_ALWAYS_INCLUDE_TYPES:
        return True
    if chunk_type in FINETUNE_CODEBASE_CONDITIONAL_TYPES:
        m = _FINETUNE_TIER_RE.search(record.get("title") or "")
        return bool(m) and m.group(1) in FINETUNE_CODEBASE_CONDITIONAL_MIN_TIER
    return False

def _parse_kb_md_record(collection: str, chunk_id: str) -> dict:
    """Reconstructs the same record shape rag_submit_work() originally wrote to
    users/*/{wiki,codebase,github_reviews}.jsonl, but read back from the published
    knowledge_base/*.md file instead -- so finetune trains on whatever audit mode has already
    fixed (or will fix in the future), not on the original, possibly-since-corrected crunch output
    that sits frozen in users/*.jsonl forever (that file is never touched again after the initial
    crunch submission -- confirmed while investigating why audit's fixes weren't reaching
    finetune). Returns None if this chunk_id was never published (e.g. mid-crunch, or a different
    campaign's in-progress chunk)."""
    kb_path = os.path.join(KNOWLEDGE_DIR, collection, f"{chunk_id}.md")
    if not os.path.exists(kb_path):
        return None
    with open(kb_path, encoding="utf-8") as f:
        text = f.read()

    title_m = re.match(r"^#\s+(.+)$", text, re.M)
    type_m = re.search(r"^\*\*Type:\*\*\s*(.+)$", text, re.M)
    keywords_m = re.search(r"^\*\*Keywords:\*\*\s*(.+)$", text, re.M)
    symbols_m = re.search(r"^\*\*Symbols:\*\*\s*(.+)$", text, re.M)
    concepts_m = re.search(r"^\*\*Concepts:\*\*\s*(.+)$", text, re.M)

    code_example = _extract_kb_section(text, "Code Example")
    if code_example:
        code_example = re.sub(r"^```\w*\n|\n```$", "", code_example).strip() or None

    related = _extract_kb_section(text, "Related Questions")
    synthetic_queries = [re.sub(r"^-\s*", "", ln).strip() for ln in related.splitlines() if ln.strip()] if related else []

    return {
        "chunk_id": chunk_id,
        "title": title_m.group(1).strip() if title_m else chunk_id,
        "chunk_type": type_m.group(1).strip() if type_m else None,
        "keywords": [k.strip() for k in keywords_m.group(1).split(",")] if keywords_m else [],
        "symbols": [s.strip() for s in symbols_m.group(1).split(",")] if symbols_m else [],
        "concepts": [c.strip() for c in concepts_m.group(1).split(",")] if concepts_m else [],
        "summary": _extract_kb_section(text, "Summary"),
        "comprehensive_explanation": _extract_kb_section(text, "Explanation"),
        "code_example": code_example,
        "synthetic_queries": synthetic_queries,
    }

def _load_kb_records_for_finetune(collection: str) -> list:
    d = os.path.join(KNOWLEDGE_DIR, collection)
    if not os.path.exists(d):
        return []
    out = []
    for fname in sorted(os.listdir(d)):
        if not fname.endswith(".md"):
            continue
        record = _parse_kb_md_record(collection, fname[:-3])
        if record:
            out.append(record)
    return out

def finetune_initialize_chunks(verbose: bool = True):
    global finetune_total_chunks
    finetune_total_chunks = 0
    if not os.path.exists(KNOWLEDGE_DIR):
        print(f"[X] {KNOWLEDGE_DIR} not found. Run pipeline_crunching/build_knowledge_base.py first.")
        sys.exit(1)

    lock_state = load_lock_state(FINETUNE_LOCK_FILE)
    completed_chunks = set(lock_state.get("completed", []))
    old_hashes = read_json_file(FINETUNE_HASH_DB_FILE, {})
    current_hashes = {}

    docs_entries = _load_kb_records_for_finetune("docs")
    review_entries = _load_kb_records_for_finetune("reviews")
    codebase_entries = [r for r in _load_kb_records_for_finetune("codebase") if _finetune_codebase_qualifies(r)]

    skipped_unchanged = 0
    for source_type, entries in (("docs", docs_entries), ("codebase", codebase_entries), ("reviews", review_entries)):
        for entry in entries:
            content_hash = calculate_content_hash(entry)
            current_hashes[entry["chunk_id"]] = content_hash
            finetune_total_chunks += 1

            if (entry["chunk_id"] in completed_chunks and
                    old_hashes.get(entry["chunk_id"]) == content_hash):
                skipped_unchanged += 1
                continue

            finetune_chunk_queue.append({
                "chunk_id": entry["chunk_id"],
                "source_type": source_type,
                "record": entry,
            })

    write_json_file(FINETUNE_HASH_DB_FILE, current_hashes, "hash db")
    os.makedirs(FINETUNE_OUTPUT_DIR, exist_ok=True)

    if verbose:
        print("\n" + "─"*55)
        print("            FINE-TUNE PIPELINE METRICS                ")
        print("─"*55)
        print(f" Docs candidates:       {len(docs_entries)}")
        print(f" Codebase candidates:   {len(codebase_entries)}")
        print(f" Review candidates:     {len(review_entries)}")
        print(f" Bypassed (unchanged):  {skipped_unchanged}")
        print(f" Active task targets:   {len(finetune_chunk_queue)}")
        print("─"*55 + "\n")

# ============================================================
# AUDIT CAMPAIGN -- finds and fixes the "fact dropped during crunching" bug class in ALREADY
# published knowledge_base/*.md content. This is the automated, ongoing version of the manual
# audit-and-rewrite work done by hand throughout the 2026-07-18 RAG debugging session (see
# README.md's Prototype 5 section): every bug found that day had the same shape -- a chunk's
# Explanation mentioned a topic without stating the actual value/fact the raw source gives for it.
#
# Deliberately separate campaign state from RAG/finetune (own lock file, own stats, own hash
# tracking) since chunk_ids can collide as strings across campaigns without meaning the same
# chunk -- same reasoning already documented at the top of this file for RAG vs finetune.
# ============================================================

def _enumerate_source_chunks_for_audit() -> list:
    """Every (chunk_id, raw_content, collection) triple currently derivable from local source
    data, re-chunked with the exact same chunk_size/overlap/boundaries rag_initialize_chunks()
    uses for docs/codebase/addon_creator, so chunk_id and raw_content match exactly what the
    original crunch saw -- deliberately NOT reusing rag_chunk_queue directly, since that only
    holds chunks still *incomplete* for the RAG campaign, while auditing needs raw_content for
    already-completed chunks too (the ones with an existing knowledge_base entry to check).
    Reviews are handled differently: raw_content is read directly from organized_cubyz_dataset's
    reviews json, which -- unlike the crunched output stored in users/*/github_reviews.jsonl --
    still carries the original PR diff/comment text (confirmed present live, 2026-07-18)."""
    chunk_size, overlap = 150, 30
    results = []

    for tier in ["easy", "medium", "hard"]:
        tier_path = os.path.join(RAG_SOURCE_DIR, tier)
        if not os.path.exists(tier_path):
            continue
        for file in os.listdir(tier_path):
            file_path = os.path.join(tier_path, file)
            if not os.path.isfile(file_path):
                continue

            if file.lower().endswith('.json') or file.lower().startswith('reviews'):
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        review_array = json.load(f)
                except Exception:
                    continue
                for review_item in review_array:
                    chunk_id = review_item.get("chunk_id")
                    raw_content = review_item.get("raw_content", "")
                    if chunk_id and raw_content:
                        results.append({"chunk_id": chunk_id, "raw_content": raw_content, "collection": "reviews"})
            else:
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                except Exception:
                    continue
                file_lower = file.lower()
                if file_lower.startswith("codebase_"):
                    collection = "codebase"
                elif file_lower.startswith("addon_creator_"):
                    collection = "addon_creator"
                else:
                    collection = "docs"
                for idx, chunk_raw_content in enumerate(_structural_chunks(lines, chunk_size, chunk_size * 2, overlap)):
                    results.append({
                        "chunk_id": f"{file}_chunk_{idx}",
                        "raw_content": chunk_raw_content,
                        "collection": collection,
                    })
    return results

def _combined_audit_hash(raw_content: str, kb_content: str) -> str:
    """One hash covering both sides of what an audit checks -- if EITHER the raw source or the
    published knowledge_base chunk changes, the combined hash changes, and the chunk is due for
    re-audit. Hashing only one side would miss e.g. a hand-edit to the knowledge_base chunk (like
    every fix made by hand this session) that never touched the raw source."""
    h = hashlib.sha256()
    h.update(raw_content.encode("utf-8", errors="ignore"))
    h.update(b"\x00")
    h.update(kb_content.encode("utf-8", errors="ignore"))
    return h.hexdigest()

def _prune_stale_audit_assignments():
    now = time.time()
    stale = [u for u, info in audit_model_assignments.items() if now - info["last_seen"] > AUDIT_ASSIGNMENT_STALE_SECONDS]
    for u in stale:
        audit_model_assignments.pop(u, None)
    if stale:
        write_json_file(AUDIT_MODEL_ASSIGNMENTS_FILE, audit_model_assignments, "audit model assignments")

def _assign_audit_model(user_id: str, hardware_tier: str, client_local_models: set = None) -> str:
    """Gives this volunteer one specific model from their hardware tier's roster, distinct from
    every other model currently in use by someone else online in that same tier -- see
    AUDIT_MODEL_ROSTER's comment for why. Stable for as long as they stay online (no reason to make
    Ollama reload a different model every single poll); reassigned fresh once they've been away
    long enough to be pruned."""
    _prune_stale_audit_assignments()
    tier = hardware_tier if hardware_tier in AUDIT_MODEL_ROSTER else "medium"
    roster = AUDIT_MODEL_ROSTER[tier]
    user_key = user_id.lower()
    client_local_models = client_local_models or set()

    # Also checks the existing model is still actually IN the current roster, not just that the
    # tier matches -- without this, editing AUDIT_MODEL_ROSTER (e.g. removing a model that turned
    # out too large for its tier's low end) would never actually take effect for anyone already
    # holding that now-removed model: this stayed sticky purely on tier match, so a volunteer
    # assigned a model that got deleted from the roster would keep being handed that same
    # unpullable/oversized model forever, confirmed live right after gemma2:27b was removed here.
    existing = audit_model_assignments.get(user_key)
    if existing and existing.get("tier") == tier and existing.get("model") in roster:
        existing["last_seen"] = time.time()
        write_json_file(AUDIT_MODEL_ASSIGNMENTS_FILE, audit_model_assignments, "audit model assignments")
        return existing["model"]

    # Whichever roster model the fewest OTHER currently-active same-tier volunteers are using gets
    # picked, ties broken by roster order. The 1st joiner gets roster[0] (everything at 0 usage,
    # first tie-break wins); the 2nd gets roster[1] (roster[0] now has 1 user, everything else 0);
    # once every model has exactly 1 user, the next joiner ties everything again and lands back on
    # roster[0] -- a genuine repeat of the list, the same behavior whether 3 or 30 people join.
    usage = {m: 0 for m in roster}
    for u, info in audit_model_assignments.items():
        if u != user_key and info.get("tier") == tier and info.get("model") in usage:
            usage[info["model"]] += 1

    # Prefer a model this specific client already has pulled -- avoids an unnecessary download
    # entirely when there's a diversity-valid choice available for free. Only fall through to the
    # full roster (accepting a pull may be needed) when none of what they already have is a viable,
    # least-used option in this tier.
    already_have = [m for m in roster if m in client_local_models]
    if already_have:
        min_usage_overall = min(usage.values())
        # Only prefer "already have" if it doesn't force a strictly worse (more duplicated) model
        # than the true least-used one -- otherwise two clients who both already have roster[0]
        # would keep piling onto it forever instead of ever spreading out.
        candidates = [m for m in already_have if usage[m] == min_usage_overall]
        if candidates:
            chosen = min(candidates, key=lambda m: roster.index(m))
            audit_model_assignments[user_key] = {"model": chosen, "tier": tier, "last_seen": time.time()}
            write_json_file(AUDIT_MODEL_ASSIGNMENTS_FILE, audit_model_assignments, "audit model assignments")
            log_event("audit", user_id, "i", Colors.GRAY, f"assigned model {Colors.BOLD}{chosen}{Colors.RESET} (tier: {tier}, already local)", short="MODEL ASSIGNED")
            return chosen

    chosen = min(roster, key=lambda m: (usage[m], roster.index(m)))
    audit_model_assignments[user_key] = {"model": chosen, "tier": tier, "last_seen": time.time()}
    write_json_file(AUDIT_MODEL_ASSIGNMENTS_FILE, audit_model_assignments, "audit model assignments")
    pull_note = "" if chosen in client_local_models else " -- will need to be pulled"
    log_event("audit", user_id, "i", Colors.GRAY, f"assigned model {Colors.BOLD}{chosen}{Colors.RESET} (tier: {tier}){pull_note}", short="MODEL ASSIGNED")
    return chosen

def audit_initialize_chunks(verbose: bool = True):
    global audit_total_chunks
    audit_chunk_queue.clear()
    audit_total_chunks = 0
    audit_model_assignments.clear()
    audit_model_assignments.update(read_json_file(AUDIT_MODEL_ASSIGNMENTS_FILE, {}))

    if not os.path.exists(RAG_SOURCE_DIR) or not os.path.exists(KNOWLEDGE_DIR):
        print("[X] Audit campaign: source dataset or knowledge_base/ not found -- skipping.")
        return

    lock_state = load_lock_state(AUDIT_LOCK_FILE)
    completed_chunks = set(lock_state.get("completed", []))
    audit_hashes = read_json_file(AUDIT_HASH_FILE, {})

    skipped_no_kb_entry = 0
    skipped_unchanged = 0
    for entry in _enumerate_source_chunks_for_audit():
        chunk_id, collection = entry["chunk_id"], entry["collection"]
        kb_path = os.path.join(KNOWLEDGE_DIR, collection, f"{chunk_id}.md")
        if not os.path.exists(kb_path):
            skipped_no_kb_entry += 1
            continue  # never crunched yet (or a different campaign's in-progress chunk) -- nothing to audit

        try:
            with open(kb_path, encoding="utf-8") as f:
                kb_content = f.read()
        except Exception:
            continue

        # Counted toward the true campaign size here, BEFORE the unchanged-skip check below --
        # same pattern as rag_total_chunks/finetune_total_chunks (see their shared comment). Audit
        # mode had regressed to the bug that pattern already fixed: only incrementing the total
        # for chunks that make it into audit_chunk_queue undercounts it, since every chunk already
        # resolved with a matching cached hash (a real "no issue found" or "escalated to human"
        # verdict from a prior pass) drops out of the queue but was never actually removed from the
        # campaign -- confirmed live, this made "total_chunks_due" visibly shrink after every
        # restart (3,247 -> 3,171 -> 2,972 over three restarts) even though no chunks left the
        # campaign, which also meant global_percentage was computed against a moving denominator.
        audit_total_chunks += 1

        current_hash = _combined_audit_hash(entry["raw_content"], kb_content)
        if chunk_id in completed_chunks and audit_hashes.get(chunk_id) == current_hash:
            skipped_unchanged += 1
            continue  # already audited, and neither side has changed since

        audit_chunk_queue.append({
            "chunk_id": chunk_id,
            "collection": collection,
            "raw_content": entry["raw_content"],
            "kb_content": kb_content,
            "content_hash": current_hash,
        })

    if verbose:
        print("\n" + "─"*55)
        print("              AUDIT PIPELINE METRICS                  ")
        print("─"*55)
        print(f" Not yet crunched (skipped):     {skipped_no_kb_entry}")
        print(f" Already audited, unchanged:     {skipped_unchanged}")
        print(f" Due for (re-)audit:             {len(audit_chunk_queue)}")
        print("─"*55 + "\n")

def _extract_kb_section(text: str, heading: str) -> str:
    match = re.search(rf"## {re.escape(heading)}\n(.*?)(?=\n\n## |\n\n\*Source)", text, re.S)
    return match.group(1).strip() if match else ""

def _text_similarity(a: str, b: str) -> float:
    import difflib
    norm = lambda s: re.sub(r"\s+", " ", s.strip().lower())
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()

def _replace_kb_section(text: str, heading: str, new_body: str) -> str:
    """Replaces just one section's body (e.g. everything after '## Explanation') in a
    knowledge_base/*.md chunk, leaving the header/Type/Keywords/Symbols/Concepts and the trailing
    '## Related Questions'/Source footer exactly as they are -- an audit fix corrects the
    generated content, it never touches structural metadata a human or the original crunch
    already got right. Matches up to the next '## ' heading or the '*Source:' footer, whichever
    comes first, since which section follows varies (a Code Example section is only present on
    some chunk types)."""
    pattern = re.compile(rf"(## {re.escape(heading)}\n).*?(?=\n\n## |\n\n\*Source)", re.S)
    if not pattern.search(text):
        return text
    return pattern.sub(lambda m: m.group(1) + new_body.strip(), text, count=1)

def _apply_audit_fix(chunk_id: str, collection: str, corrected_summary, corrected_explanation, corrected_related_questions) -> bool:
    kb_path = os.path.join(KNOWLEDGE_DIR, collection, f"{chunk_id}.md")
    if not os.path.exists(kb_path):
        return False

    # A model occasionally writes an entire replacement document (header/Type/Keywords/Concepts,
    # then its OWN "## Summary"/"## Explanation"/"## Related Questions") into a single field
    # instead of just that field's prose -- confirmed live, this produced 9 real applied fixes with
    # visibly duplicated/nested section headings (e.g. a "## Summary" section whose body contained
    # an entire second copy of the chunk, including a second "## Explanation"). _replace_kb_section
    # has no way to tell a legitimate multi-paragraph explanation from an accidentally-embedded
    # whole document, so this is caught here instead: refuse to apply and let the chunk go back
    # into the pool for another attempt, rather than writing structurally corrupted content.
    for field in (corrected_summary, corrected_explanation):
        if field and re.search(r"^##\s+(Summary|Explanation|Related Questions)\s*$", field, re.M):
            log_event("audit", "", "✗", Colors.RED, f"{Colors.BOLD}{chunk_id}{Colors.RESET}: corrected field contains an embedded '## ' heading (whole replacement document, not one section) -- refusing to apply, chunk stays open", short="FIX REJECTED (malformed)")
            return False

    with open(kb_path, encoding="utf-8") as f:
        text = f.read()

    if corrected_summary:
        text = _replace_kb_section(text, "Summary", corrected_summary)
    if corrected_explanation:
        text = _replace_kb_section(text, "Explanation", corrected_explanation)
    if corrected_related_questions:
        # Strip any leading "- " the model already included (it sometimes echoes questions back
        # with the bullet marker still attached, e.g. after reading them out of kb_content's own
        # markdown) before adding our own -- otherwise this produces a literal "- - question"
        # double bullet. Confirmed live: 34 of 35 knowledge_base chunks with this exact glitch
        # were audit-mode applied fixes, none from the original crunching campaign.
        rq_body = "\n".join(f"- {re.sub(r'^[\\s-]+', '', q)}" for q in corrected_related_questions)
        text = _replace_kb_section(text, "Related Questions", rq_body)

    with open(kb_path, "w", encoding="utf-8") as f:
        f.write(text)
    return True

def _new_user_stats_entry() -> dict:
    return {"chunks_audited": 0, "issues_found": 0, "fixes_applied": 0, "reviews_done": 0}

def _get_audit_work(user_id: str, hardware_tier: str, client_local_models: set = None) -> dict:
    state = load_lock_state(AUDIT_LOCK_FILE)
    state_modified = prune_stale_locks(state)
    pending = read_json_file(AUDIT_PENDING_FILE, {})
    assigned_model = _assign_audit_model(user_id, hardware_tier, client_local_models)

    total_chunks = audit_total_chunks  # true campaign size -- see audit_initialize_chunks's comment
    # NOT len(state["completed"]) -- that's a LIFETIME count of unique chunks ever resolved, which
    # doesn't move during a re-audit pass over already-completed chunks (they're already in that
    # list from their first pass) even while real work is actively happening. audit_chunk_queue
    # now correctly SHRINKS as chunks resolve (see _mark_done's comment), so total minus whatever's
    # still queued is a live, honest "how much of the CURRENT pass is actually done" -- confirmed
    # live as the fix for a real, confusing symptom: the progress bar sat frozen at 3247/3247
    # (100%) for an entire re-audit pass while every volunteer was visibly still working.
    completed_chunks = total_chunks - len(audit_chunk_queue)

    # Three kinds of work can exist for a given chunk right now: a fresh chunk nobody's looked at
    # yet (propose), a chunk sitting with an unreviewed (or not-yet-fully-approved) proposal
    # (review -- but never handed to the proposer, nor to anyone who already approved this same
    # proposal, since re-approving with yourself isn't independent of anything), or a chunk whose
    # reviewer asked for a better fix (revise -- never handed back to that same reviewer, so a
    # fresh attempt gets made rather than the same person just overriding their own feedback).
    # Review/revise are gated to medium+ hardware tier -- see REVIEW_MIN_TIER's comment.
    can_review = HARDWARE_TIER_RANK.get(hardware_tier, 2) >= HARDWARE_TIER_RANK[REVIEW_MIN_TIER]
    candidates = []
    for t in audit_chunk_queue:
        cid = t["chunk_id"]
        # NOT also skipped for "cid in state['completed']" -- audit_chunk_queue only ever contains
        # a chunk that's either never been audited, or WAS audited but the combined raw+kb hash
        # changed since (see audit_initialize_chunks()'s skip-unchanged logic, and _mark_done's
        # comment on deliberately not caching a hash for LLM-only-approved fixes so they get a
        # second independent pass later). state["completed"] never has entries removed from it, so
        # a completed-list check here would make that whole "eligible for re-audit" design
        # permanently unreachable: confirmed live -- a second full audit run over ~2,255
        # previously-applied fixes produced zero new activity and reported "complete" instantly,
        # because every one of them was silently filtered out right here despite
        # audit_initialize_chunks() correctly re-queuing all of them every restart.
        if cid in state["locked"]:
            continue
        p = pending.get(cid)
        if not p or not p.get("stage"):
            candidates.append(("propose", t, p))
        elif not can_review:
            continue
        elif p["stage"] == "proposed" and p["proposer"].lower() != user_id.lower() \
                and user_id.lower() not in [a.lower() for a in p.get("approvals", [])]:
            candidates.append(("review", t, p))
        elif p["stage"] == "revise_requested" and (p.get("last_reviewer") or "").lower() != user_id.lower():
            candidates.append(("revise", t, p))
        # else: nothing this user_id can do for this chunk right now (e.g. they're the proposer
        # waiting on someone else's review, or they already approved it once and it's waiting on a
        # second approver) -- it just isn't offered to them this call.

    # Global remaining count (matches /leaderboard's definition), not len(candidates) -- the
    # candidate list is just what THIS caller can currently pick from, not the campaign's real
    # remaining size, so it made the live status ETA inconsistent with the leaderboard's.
    completed_since_tracking = completed_chunks - state.get("actions_baseline_completed", completed_chunks)
    eta_seconds = _eta_seconds(audit_completion_log, total_chunks - completed_chunks,
                                _audit_avg_actions_per_chunk(state.get("actions_count", 0), completed_since_tracking))

    if not candidates:
        if state_modified:
            save_lock_state(AUDIT_LOCK_FILE, state)
        status = "waiting" if (state["locked"] or pending) else "done"
        return {"mode": "audit", "status": status, "total_chunks": total_chunks,
                "completed_chunks": completed_chunks, "eta_seconds": eta_seconds, "audit_model": assigned_model}

    # Review/revise work clears an in-flight chunk all the way to a decision; fresh proposals just
    # add more in-flight chunks. Prioritizing the former keeps the pending backlog from growing
    # unbounded when there are more volunteers proposing than reviewing.
    priority = {"review": 0, "revise": 1, "propose": 2}
    candidates.sort(key=lambda c: priority[c[0]])
    task_type, assigned_task, p = candidates[0]

    state["locked"][assigned_task["chunk_id"]] = {"user_id": user_id, "timestamp": time.time()}
    save_lock_state(AUDIT_LOCK_FILE, state)
    log_event("audit", user_id, "→", Colors.BLUE, f"dispatched {Colors.BOLD}{task_type}{Colors.RESET} · {assigned_task['chunk_id']} {Colors.GRAY}({assigned_task['collection']}){Colors.RESET}", short=f"DISPATCHED {task_type.upper()}")

    task = {
        "chunk_id": assigned_task["chunk_id"],
        "collection": assigned_task["collection"],
        "raw_content": assigned_task["raw_content"],
        "kb_content": assigned_task["kb_content"],
        "task_type": task_type,
    }
    if task_type in ("review", "revise"):
        task["proposed_summary"] = p.get("corrected_summary")
        task["proposed_explanation"] = p.get("corrected_explanation")
        task["proposed_related_questions"] = p.get("corrected_related_questions")
        task["proposal_reason"] = p.get("reason")
    if task_type == "revise":
        task["review_feedback"] = p.get("review_feedback")

    return {"mode": "audit", "status": "active", "task": task, "total_chunks": total_chunks,
            "completed_chunks": completed_chunks, "eta_seconds": eta_seconds, "audit_model": assigned_model}

def _submit_audit_work(submission: UnifiedSubmission) -> dict:
    state = load_lock_state(AUDIT_LOCK_FILE)
    state["locked"].pop(submission.chunk_id, None)

    original_task = next((t for t in audit_chunk_queue if t["chunk_id"] == submission.chunk_id), None)

    # A chunk_id already in state["completed"] is normally a late/duplicate submission for
    # already-resolved work and should be ignored -- EXCEPT when it's still in audit_chunk_queue
    # (original_task is not None), meaning its combined raw+kb hash changed since that earlier
    # completion and audit_initialize_chunks() legitimately re-queued it for a fresh pass (see
    # _get_audit_work's comment for the full story -- this is the submit-side half of the same
    # bug: without this exception, ~2,255 previously-applied fixes could never be resubmitted even
    # after the dispatch-side fix, since every one of them was already in state["completed"]).
    if submission.chunk_id in state["completed"] and original_task is None:
        save_lock_state(AUDIT_LOCK_FILE, state)
        return {"status": "ignored"}

    # Counts every real propose/review/revise submission accepted past this point, regardless of
    # whether it ends up resolving the chunk -- see _audit_avg_actions_per_chunk's comment. Stored
    # in the same persisted file as "completed" (not a bare in-memory global) specifically so it
    # survives a server restart instead of resetting to 0 while "completed" stays at its full
    # campaign total. actions_baseline_completed snapshots "completed" the first time this ever
    # runs, so the ratio is always measured from a matching zero point for both numerator and
    # denominator -- see _audit_avg_actions_per_chunk's comment.
    if "actions_baseline_completed" not in state:
        state["actions_baseline_completed"] = len(state["completed"])
    state["actions_count"] = state.get("actions_count", 0) + 1

    collection = (original_task or {}).get("collection", "docs")
    content_hash = (original_task or {}).get("content_hash")
    kb_content = (original_task or {}).get("kb_content", "")

    user_stats = load_user_stats(AUDIT_STATS_FILE)
    user_key = submission.user_id.lower()
    user_stats.setdefault(user_key, _new_user_stats_entry())

    pending = read_json_file(AUDIT_PENDING_FILE, {})

    def _mark_done(result_label, cache_hash=True):
        # Idempotent -- see _submit_rag_work's comment on why appending unconditionally would let
        # len(state["completed"]) exceed total_chunks once a chunk can legitimately complete more
        # than once (a re-audit cycle re-resolving a chunk that was already in this list).
        if submission.chunk_id not in state["completed"]:
            state["completed"].append(submission.chunk_id)
        save_lock_state(AUDIT_LOCK_FILE, state)
        if cache_hash and content_hash:
            audit_hashes = read_json_file(AUDIT_HASH_FILE, {})
            audit_hashes[submission.chunk_id] = content_hash
            write_json_file(AUDIT_HASH_FILE, audit_hashes, "audit hash state")
        # audit_chunk_queue is built once at startup/mode-switch and NEVER otherwise pruned as
        # chunks resolve -- removing the "chunk_id in state['completed']" dispatch check (see
        # _get_audit_work's comment, needed so a hash-changed chunk becomes reachable again at
        # all) meant a chunk that just resolved was immediately offered right back out as a fresh
        # "propose" candidate on the very next poll, forever, since pending.pop() below already
        # cleared its in-flight state and nothing else excluded it. Confirmed live with a direct
        # dispatch->resolve->dispatch-again test: without this line the SAME already-settled
        # chunk_id kept coming back every single time. This is what "100%/3247 complete but every
        # client is still working" actually was -- clients weren't doing new re-audit work, they
        # were stuck looping on chunks that had already resolved moments earlier. Removing it here
        # (not from state["completed"], which stays permanent) only affects THIS session's live
        # queue; whether it's offered again in a FUTURE session is decided fresh by
        # audit_initialize_chunks()'s own hash comparison at next restart, same as always.
        audit_chunk_queue[:] = [t for t in audit_chunk_queue if t["chunk_id"] != submission.chunk_id]
        pending.pop(submission.chunk_id, None)
        write_json_file(AUDIT_PENDING_FILE, pending, "audit pending fixes")
        save_user_stats(AUDIT_STATS_FILE, user_stats)
        _record_completion(audit_completion_log)
        return {"status": "success", "result": result_label}

    # --- Stage 1: a fresh proposal ---
    if submission.task_type == "propose":
        user_stats[user_key]["chunks_audited"] += 1
        if submission.verdict != "needs_fix":
            save_user_stats(AUDIT_STATS_FILE, user_stats)
            log_event("audit", submission.user_id, "✓", Colors.GREEN, f"{submission.chunk_id} -- no issue found", short="NO ISSUE FOUND")
            return _mark_done("ok")

        # Same false-positive guard confirmed necessary live during testing: the model can flag
        # needs_fix against content that's already correct while its own "fix" restates the same
        # facts near-verbatim. If the proposal isn't actually different from what's published,
        # there's nothing for a reviewer to usefully review -- skip straight to done.
        existing_explanation = _extract_kb_section(kb_content, "Explanation")
        proposed_explanation = submission.corrected_explanation or ""
        if existing_explanation and proposed_explanation and _text_similarity(existing_explanation, proposed_explanation) > 0.95:
            save_user_stats(AUDIT_STATS_FILE, user_stats)
            log_event("audit", submission.user_id, "~", Colors.YELLOW, f"{submission.chunk_id} -- flagged needs_fix but near-identical to what's published, treating as no-op", short="NO-OP (near-identical)")
            return _mark_done("false_positive_no_op")

        user_stats[user_key]["issues_found"] += 1
        prior = pending.get(submission.chunk_id, {})
        pending[submission.chunk_id] = {
            "stage": "proposed", "collection": collection, "proposer": submission.user_id,
            "reason": submission.reason,
            "corrected_summary": submission.corrected_summary,
            "corrected_explanation": submission.corrected_explanation,
            "corrected_related_questions": submission.corrected_related_questions,
            "attempts": prior.get("attempts", 0) + 1,
            "last_reviewer": None,
            "approvals": [],
            "history": prior.get("history", []) + [{
                "stage": "proposed", "user_id": submission.user_id, "timestamp": time.time(),
                "reason": submission.reason,
                "corrected_summary": submission.corrected_summary,
                "corrected_explanation": submission.corrected_explanation,
                "corrected_related_questions": submission.corrected_related_questions,
            }],
        }
        write_json_file(AUDIT_PENDING_FILE, pending, "audit pending fixes")
        save_lock_state(AUDIT_LOCK_FILE, state)
        save_user_stats(AUDIT_STATS_FILE, user_stats)
        log_event("audit", submission.user_id, "⚠", Colors.YELLOW, f"proposed fix for {Colors.BOLD}{submission.chunk_id}{Colors.RESET}: {submission.reason[:100]} -- awaiting review", short="PROPOSED FIX")
        return {"status": "success", "result": "proposed_awaiting_review"}

    # --- Stage 2: an independent review of someone else's proposal ---
    if submission.task_type == "review":
        entry = pending.get(submission.chunk_id)
        if entry is None or entry.get("stage") != "proposed":
            save_lock_state(AUDIT_LOCK_FILE, state)
            return {"status": "ignored", "result": "no_matching_proposal"}

        user_stats[user_key]["reviews_done"] += 1
        entry["history"].append({
            "stage": "reviewed", "user_id": submission.user_id, "verdict": submission.review_verdict,
            "feedback": submission.review_feedback, "timestamp": time.time(),
        })

        if submission.review_verdict == "approve":
            required = _required_approvals(collection)
            approvals = entry.setdefault("approvals", [])
            if submission.user_id not in approvals:
                approvals.append(submission.user_id)

            if len(approvals) < required:
                # Not enough independent approvals yet for a chunk this consequential -- see
                # AUDIT_REQUIRED_APPROVALS's comment. Stays in "proposed" (still reviewable, just
                # not by anyone already in `approvals` -- see _get_audit_work's filter) rather than
                # applying on a single approval.
                pending[submission.chunk_id] = entry
                write_json_file(AUDIT_PENDING_FILE, pending, "audit pending fixes")
                save_lock_state(AUDIT_LOCK_FILE, state)
                save_user_stats(AUDIT_STATS_FILE, user_stats)
                log_event("audit", submission.user_id, "✓", Colors.YELLOW, f"approved {submission.chunk_id} ({len(approvals)}/{required} approvals) -- awaiting one more", short="APPROVED")
                return {"status": "success", "result": "approved_awaiting_more"}

            applied = _apply_audit_fix(
                submission.chunk_id, collection,
                entry.get("corrected_summary"), entry.get("corrected_explanation"),
                entry.get("corrected_related_questions"),
            )
            if not applied:
                # This used to just bail out here without touching `pending` or `entry` at all --
                # neither persisted to disk (this reviewer's approval silently vanished) nor
                # advanced the conversation state, so the exact same malformed proposal (most
                # commonly the embedded-whole-document guard in _apply_audit_fix) kept getting
                # re-offered for review forever, with every reviewer hitting the identical
                # rejection on repeat -- confirmed live as a real infinite loop. Treated the same
                # as an explicit "revise" verdict instead: send it back for a fresh attempt (still
                # counting toward MAX_REVIEW_ROUNDS, so a proposer that can't produce anything
                # clean after repeated tries still eventually escalates to a human) rather than
                # leaving it stuck in "proposed" with unpersisted state.
                attempts = entry.get("attempts", 1)
                log_event("audit", submission.user_id, "✗", Colors.RED, f"{submission.chunk_id}: approved fix failed to apply (malformed content) -- requesting a fresh attempt", short="FIX FAILED (retry)")
                if attempts >= MAX_REVIEW_ROUNDS:
                    append_jsonl(AUDIT_NEEDS_HUMAN_FILE, {
                        "chunk_id": submission.chunk_id, "collection": collection,
                        "reason": "approved fix repeatedly failed to apply (malformed content)",
                        "history": entry["history"], "flagged_at": time.time(),
                    }, "audit needs human review")
                    save_user_stats(AUDIT_STATS_FILE, user_stats)
                    return _mark_done("needs_human_review")
                entry["stage"] = "revise_requested"
                entry["review_feedback"] = ("The approved fix could not be applied -- it likely contains "
                    "a whole replacement document (its own '## Summary'/'## Explanation'/'## Related "
                    "Questions' headings) instead of clean text for just one section. Write a corrected "
                    "field containing ONLY that section's prose, with no '## ' headings inside it.")
                entry["last_reviewer"] = submission.user_id
                entry["attempts"] = attempts + 1
                entry["approvals"] = []  # this content never actually landed -- needs fresh approval too
                pending[submission.chunk_id] = entry
                write_json_file(AUDIT_PENDING_FILE, pending, "audit pending fixes")
                save_lock_state(AUDIT_LOCK_FILE, state)
                save_user_stats(AUDIT_STATS_FILE, user_stats)
                return {"status": "success", "result": "fix_failed_to_apply_requeued"}
            append_jsonl(AUDIT_APPLIED_LOG, {
                "chunk_id": submission.chunk_id, "collection": collection,
                "reason": entry.get("reason"), "proposer": entry.get("proposer"),
                "reviewers": approvals, "required_approvals": required,
                "attempts": entry.get("attempts", 1), "applied_at": time.time(),
            }, "audit applied fix")
            pkey = entry["proposer"].lower()
            user_stats.setdefault(pkey, _new_user_stats_entry())
            user_stats[pkey]["fixes_applied"] += 1
            log_event("audit", entry['proposer'], "✓✓", Colors.GREEN + Colors.BOLD, f"fix APPLIED for {submission.chunk_id} -- approved by {', '.join(approvals)}", short="FIX APPLIED")
            # Don't cache a hash for content only ever checked by LLMs, never a human -- leave it
            # eligible for a future re-audit rather than treating it as permanently settled.
            return _mark_done("fix_applied", cache_hash=False)

        if submission.review_verdict == "reject":
            # The reviewer says there was never a real issue -- the proposer's DIAGNOSIS itself was
            # wrong, not just the wording of the fix. Don't just re-ask the same proposer -- clear
            # the proposal and send the chunk back for a completely fresh, independent pass, so a
            # single reviewer's opinion isn't the last word either.
            attempts = entry.get("attempts", 1)
            log_event("audit", submission.user_id, "✗", Colors.RED, f"rejected {Colors.BOLD}{entry['proposer']}{Colors.RESET}'s proposal for {submission.chunk_id}: {submission.review_feedback[:100]}", short="REJECTED FIX")
            if attempts >= MAX_REVIEW_ROUNDS:
                append_jsonl(AUDIT_NEEDS_HUMAN_FILE, {
                    "chunk_id": submission.chunk_id, "collection": collection,
                    "reason": "proposer and reviewer disagreed repeatedly without resolving",
                    "history": entry["history"], "flagged_at": time.time(),
                }, "audit needs human review")
                save_user_stats(AUDIT_STATS_FILE, user_stats)
                return _mark_done("needs_human_review")
            pending[submission.chunk_id] = {"attempts": attempts, "history": entry["history"]}
            write_json_file(AUDIT_PENDING_FILE, pending, "audit pending fixes")
            save_lock_state(AUDIT_LOCK_FILE, state)
            save_user_stats(AUDIT_STATS_FILE, user_stats)
            return {"status": "success", "result": "rejected_requeued"}

        # review_verdict == "revise": the reviewer agrees something's genuinely wrong, but the
        # proposed fix itself needs work -- keep the diagnosis, attach specific feedback, and route
        # it out for a fresh attempt at the fix (see _get_audit_work's last_reviewer exclusion).
        attempts = entry.get("attempts", 1)
        if attempts >= MAX_REVIEW_ROUNDS:
            append_jsonl(AUDIT_NEEDS_HUMAN_FILE, {
                "chunk_id": submission.chunk_id, "collection": collection,
                "reason": "revision requested repeatedly without landing on an approved fix",
                "history": entry["history"], "flagged_at": time.time(),
            }, "audit needs human review")
            save_user_stats(AUDIT_STATS_FILE, user_stats)
            return _mark_done("needs_human_review")

        entry["stage"] = "revise_requested"
        entry["review_feedback"] = submission.review_feedback
        entry["last_reviewer"] = submission.user_id
        entry["attempts"] = attempts + 1
        pending[submission.chunk_id] = entry
        write_json_file(AUDIT_PENDING_FILE, pending, "audit pending fixes")
        save_lock_state(AUDIT_LOCK_FILE, state)
        save_user_stats(AUDIT_STATS_FILE, user_stats)
        log_event("audit", submission.user_id, "↺", Colors.YELLOW, f"requested revision for {submission.chunk_id}: {submission.review_feedback[:100]}", short="REVISION REQUESTED")
        return {"status": "success", "result": "revision_requested"}

    # --- Stage 3: a revised fix, in response to a reviewer's specific feedback ---
    if submission.task_type == "revise":
        entry = pending.get(submission.chunk_id)
        if entry is None or entry.get("stage") != "revise_requested":
            save_lock_state(AUDIT_LOCK_FILE, state)
            return {"status": "ignored", "result": "no_matching_revision_request"}

        entry["stage"] = "proposed"
        entry["proposer"] = submission.user_id  # the reviser's fix is what gets reviewed next
        entry["corrected_summary"] = submission.corrected_summary
        entry["corrected_explanation"] = submission.corrected_explanation
        entry["corrected_related_questions"] = submission.corrected_related_questions
        entry["approvals"] = []  # this is different content from whatever was approved (if anything) before -- needs fresh approval
        entry["history"].append({
            "stage": "revised", "user_id": submission.user_id, "timestamp": time.time(),
            "corrected_summary": submission.corrected_summary,
            "corrected_explanation": submission.corrected_explanation,
            "corrected_related_questions": submission.corrected_related_questions,
        })
        pending[submission.chunk_id] = entry
        write_json_file(AUDIT_PENDING_FILE, pending, "audit pending fixes")
        save_lock_state(AUDIT_LOCK_FILE, state)
        log_event("audit", submission.user_id, "↺", Colors.YELLOW, f"submitted revised fix for {submission.chunk_id} -- awaiting review", short="REVISED FIX SUBMITTED")
        return {"status": "success", "result": "revised_awaiting_review"}

    save_lock_state(AUDIT_LOCK_FILE, state)
    return {"status": "ignored", "result": "unknown_task_type"}

def _rag_campaign_complete() -> bool:
    # An empty total (RAG source not configured/scanned) counts as "complete" -- nothing to
    # block on. Real incompleteness is completed < total with a nonzero total. Uses
    # rag_total_chunks (true campaign size), not len(rag_chunk_queue) -- the queue only holds
    # chunks still available to hand out, so once enough of the campaign is done that some source
    # files become fully-skippable on a restart, the queue length alone would make this return
    # True (campaign "complete") well before the real total is actually reached.
    total = rag_total_chunks
    if total == 0:
        return True
    state = load_lock_state(RAG_LOCK_FILE)
    return len(state["completed"]) >= total

# ============================================================
# STARTUP GATE -- picks the initial CURRENT_MODE. Both campaigns' chunk queues are always built
# regardless of which mode is chosen, so /admin/mode can switch live without a restart.
# ============================================================

def server_startup_gate():
    global CURRENT_MODE

    # If the last run's mode change was never followed by a clean shutdown (crash, kill -9,
    # power loss -- anything that skipped the finally block in __main__), flag it here instead
    # of silently forgetting what was running. Doesn't auto-resume -- the operator still has to
    # pick it -- just makes it obvious that campaign was mid-run when the server last stopped.
    persisted = load_server_mode_state()
    unfinished_mode = persisted.get("mode") if not persisted.get("clean_shutdown", True) and persisted.get("mode") in ("rag", "finetune", "audit") else None
    rag_flag = "  ⚠ was still running when the server last stopped -- resume?" if unfinished_mode == "rag" else ""
    finetune_flag = "  ⚠ was still running when the server last stopped -- resume?" if unfinished_mode == "finetune" else ""

    rag_total = len(rag_chunk_queue)
    rag_done = len(load_lock_state(RAG_LOCK_FILE)["completed"])
    rag_progress = f"  [{rag_done}/{rag_total} chunks]" if rag_total else ""
    finetune_not_ready = "  ⚠ RAG campaign not finished yet -- see note below" if not _rag_campaign_complete() else ""

    audit_flag = "  ⚠ was still running when the server last stopped -- resume?" if unfinished_mode == "audit" else ""
    audit_progress = f"  [{len(load_lock_state(AUDIT_LOCK_FILE)['completed'])}/{len(audit_chunk_queue)} chunks]" if audit_chunk_queue else ""

    print("\n" + "═"*55)
    print("        CUBYZ DISTRIBUTED DATASET ENGINE COORDINATOR      ")
    print("═"*55)
    print(f"  [1] 🟢 LAUNCH IN RAG MODE           (knowledge extraction){rag_flag}{rag_progress}")
    print(f"  [2] 🟢 LAUNCH IN FINETUNE MODE      (training-pair generation){finetune_flag}{finetune_not_ready}")
    print("  [3] 🟢 LAUNCH IN IDLE MODE          (server up, no tasks handed out)")
    print(f"  [4] 🔍 LAUNCH IN AUDIT MODE         (find/fix dropped facts in existing knowledge_base){audit_flag}{audit_progress}")
    print("  [5] ⚠️ HARD RESET RAG CAMPAIGN       (wipe queue & database to 0 -- contribution stats kept)")
    print("  [6] ⚠️ HARD RESET FINETUNE CAMPAIGN  (wipe queue & pairs to 0 -- contribution stats kept)")
    print("  [7] ⚠️ HARD RESET BOTH CAMPAIGNS     (wipe both queues to 0 -- contribution stats kept)")
    print("  [8] 🛑 SHUTDOWN ENGINE")
    print("═"*55)
    print("  Mode can be switched later without restarting: POST /admin/mode?mode=idle|rag|finetune|audit")
    print("═"*55)

    while True:
        try:
            choice = input("Select command index (1-8): ").strip()
            if choice == "1":
                CURRENT_MODE = "rag"
                print("\n[➔] Access Authorized. Launching in RAG mode...")
                break
            elif choice == "2":
                if not _rag_campaign_complete():
                    confirm = input(
                        f"\n⚠️ RAG campaign is not finished yet ({rag_done}/{rag_total} chunks). "
                        f"Fine-tune pair generation is meant to run after RAG extraction is done -- "
                        f"pair quality depends on the RAG knowledge base being complete. Launch in "
                        f"FINETUNE mode anyway? (y/n): "
                    ).strip().lower()
                    if confirm != 'y':
                        print("[~] Staying at menu -- finish the RAG campaign first, or confirm to override.")
                        continue
                CURRENT_MODE = "finetune"
                print("\n[➔] Access Authorized. Launching in FINETUNE mode...")
                break
            elif choice == "3":
                CURRENT_MODE = "idle"
                print("\n[➔] Access Authorized. Launching in IDLE mode...")
                break
            elif choice == "4":
                if not audit_chunk_queue:
                    print("\n[~] Nothing currently due for audit (either everything's already been audited "
                          "and unchanged since, or knowledge_base/ is empty). Launching anyway is harmless -- "
                          "the queue is rechecked live as chunks/source files change.")
                CURRENT_MODE = "audit"
                print("\n[➔] Access Authorized. Launching in AUDIT mode...")
                break
            elif choice == "5":
                confirm = input("\n⚠️ CRITICAL WARNING: Confirm wiping the RAG queue/database to 0? (leaderboard stats are kept) (y/n): ").strip().lower()
                if confirm == 'y':
                    rag_execute_hard_reset()
                else:
                    print("[~] Reset routine aborted.")
            elif choice == "6":
                confirm = input("\n⚠️ CRITICAL WARNING: Confirm wiping all fine-tune generated pairs? (leaderboard stats are kept) (y/n): ").strip().lower()
                if confirm == 'y':
                    finetune_execute_hard_reset()
                else:
                    print("[~] Reset routine aborted.")
            elif choice == "7":
                confirm = input("\n⚠️ CRITICAL WARNING: Confirm wiping BOTH campaigns' queues/data to 0? (leaderboard stats are kept) (y/n): ").strip().lower()
                if confirm == 'y':
                    rag_execute_hard_reset()
                    finetune_execute_hard_reset()
                else:
                    print("[~] Reset routine aborted.")
            elif choice == "8":
                print("[X] Terminating environment.")
                sys.exit(0)
            else:
                print("[!] Parameter outside boundary bounds. Select 1-8.")
        except KeyboardInterrupt:
            print("\n[X] Forced Close.")
            sys.exit(0)

# ============================================================
# API ENDPOINTS
# ============================================================

def _get_rag_work(user_id: str, hardware_tier: str, model: str) -> dict:
    state = load_lock_state(RAG_LOCK_FILE)
    state_modified = prune_stale_locks(state)

    if hardware_tier == "easy":
        allowed = ["easy"]
    elif hardware_tier == "medium":
        allowed = ["easy", "medium"]
    else:
        allowed = ["easy", "medium", "hard"]

    # Unrecognized/unset model names default to the lowest rank -- they still get every normal
    # chunk, just not the ones flagged as needing a stronger model to avoid fabricated content on
    # thin chunks.
    client_model_rank = MODEL_TIER_RANK.get(model, 1)

    # NOT also filtered on "chunk_id not in state['completed']" -- rag_chunk_queue only ever
    # contains a chunk that's either never been completed, or WAS completed but whose source file
    # hash changed since (see rag_initialize_chunks()'s skip-unchanged logic). A completed-list
    # check here would silently exclude that second case forever: state["completed"] never has
    # entries removed from it, so a hash-changed chunk that rag_initialize_chunks() correctly
    # re-queued on every restart could never actually be re-dispatched to anyone. Confirmed live
    # as the exact same bug in audit mode (see _get_audit_work's comment) -- fixed here too since
    # it's the identical pattern, not something specific to audit.
    available_tasks = [
        t for t in rag_chunk_queue
        if t["chunk_id"] not in state["locked"]
        and t["difficulty"] in allowed
        and (not t.get("requires_strong_model") or client_model_rank >= THIN_CHUNK_MIN_TIER)
    ]

    # rag_total_chunks (the true campaign size), not len(rag_chunk_queue) (only chunks still
    # available to hand out) -- using the queue length here undercounts once enough of the
    # campaign is done that some source files become fully-skippable on a restart, which doesn't
    # just make the reported percentage wrong: completed_chunks < total_chunks below could go
    # false prematurely, reporting "done" while real unprocessed work still remains queued.
    total_chunks = rag_total_chunks
    completed_chunks = len(state["completed"])
    eta_seconds = _eta_seconds(rag_completion_log, total_chunks - completed_chunks)

    if not available_tasks:
        if state_modified:
            save_lock_state(RAG_LOCK_FILE, state)
        # "done" must mean the whole campaign is finished, not just "nothing available for me
        # right now" -- otherwise a swarm of only-3B clients would see thin chunks (which they're
        # deliberately excluded from) as a false "complete!" the moment their eligible work runs
        # dry, while those chunks sit unprocessed forever waiting for a 14B+ client to show up.
        if state["locked"] or completed_chunks < total_chunks:
            return {"mode": "rag", "status": "waiting", "total_chunks": total_chunks, "completed_chunks": completed_chunks, "eta_seconds": eta_seconds}
        return {"mode": "rag", "status": "done", "total_chunks": total_chunks, "completed_chunks": completed_chunks, "eta_seconds": eta_seconds}

    if "hard" in allowed:
        priority_map = {"hard": 0, "medium": 1, "easy": 2}
        available_tasks.sort(key=lambda t: priority_map.get(t["difficulty"], 3))

    assigned_task = available_tasks[0]
    state["locked"][assigned_task["chunk_id"]] = {"user_id": user_id, "timestamp": time.time()}
    save_lock_state(RAG_LOCK_FILE, state)
    log_event("rag", user_id, "→", Colors.BLUE, f"dispatched {Colors.BOLD}{assigned_task['difficulty'].upper()}{Colors.RESET} · {assigned_task['chunk_id']}", short=f"DISPATCHED {assigned_task['difficulty'].upper()}")

    return {"mode": "rag", "status": "active", "task": assigned_task, "total_chunks": total_chunks, "completed_chunks": completed_chunks, "eta_seconds": eta_seconds}

def _get_finetune_work(user_id: str, hardware_tier: str) -> dict:
    state = load_lock_state(FINETUNE_LOCK_FILE)
    state_modified = prune_stale_locks(state)

    total_chunks = finetune_total_chunks  # true campaign size -- see _get_rag_work's comment
    completed_chunks = len(state["completed"])
    eta_seconds = _eta_seconds(finetune_completion_log, total_chunks - completed_chunks)

    # Fine-tune generation needs stronger instruction-following than RAG extraction (natural
    # prose + judging debugging-vs-review shape for reviews) -- "easy" tier clients are capped at
    # qwen2.5-coder:3b, which isn't reliable enough for this task, so they never get fine-tune
    # work even while the campaign has plenty left to do. See CUBYZ_FOLDING.py's protocol notes.
    if hardware_tier == "easy":
        available_tasks = []
    else:
        # NOT filtered on "chunk_id not in state['completed']" -- see _get_rag_work's comment for
        # why. finetune_chunk_queue already excludes anything genuinely settled (unchanged since
        # its last completion); a completed-list check on top of that would silently exclude any
        # chunk finetune_initialize_chunks() re-queued because its knowledge_base source changed
        # since the earlier pass -- state["completed"] never has entries removed from it, so that
        # exclusion would be permanent, not just until the next restart.
        available_tasks = [
            t for t in finetune_chunk_queue
            if t["chunk_id"] not in state["locked"]
        ]

    if not available_tasks:
        if state_modified:
            save_lock_state(FINETUNE_LOCK_FILE, state)
        if state["locked"] or completed_chunks < total_chunks:
            return {"mode": "finetune", "status": "waiting", "total_chunks": total_chunks, "completed_chunks": completed_chunks, "eta_seconds": eta_seconds}
        return {"mode": "finetune", "status": "done", "total_chunks": total_chunks, "completed_chunks": completed_chunks, "eta_seconds": eta_seconds}

    assigned_task = available_tasks[0]
    state["locked"][assigned_task["chunk_id"]] = {"user_id": user_id, "timestamp": time.time()}
    save_lock_state(FINETUNE_LOCK_FILE, state)
    log_event("finetune", user_id, "→", Colors.BLUE, f"dispatched {Colors.BOLD}{assigned_task['source_type']}{Colors.RESET} · {assigned_task['chunk_id']}", short=f"DISPATCHED {assigned_task['source_type'].upper()}")

    return {"mode": "finetune", "status": "active", "task": assigned_task, "total_chunks": total_chunks, "completed_chunks": completed_chunks, "eta_seconds": eta_seconds}

@app.get("/get_work")
def get_work(user_id: str, hardware_tier: str = "medium", model: str = "", client_version: str = "", available_models: str = "", avg_task_seconds: float = None, lane: str = ""):
    if not user_id.isalpha() or not (3 <= len(user_id) <= 12):
        raise HTTPException(status_code=400, detail="Invalid ID layout.")

    if _parse_version(client_version) < _parse_version(MIN_CLIENT_VERSION):
        raise HTTPException(status_code=426, detail=_version_rejection_message(client_version))

    # avg_task_seconds/lane are omitted by a client with nothing to report yet (no completed tasks,
    # or a pre-1.1.23 client that doesn't send lane at all) -- keep whatever we last heard from this
    # user_id rather than blanking it out on every single poll.
    _touch_first_seen(user_id)
    _touch_connected_since(user_id)
    prior = online_clients.get(user_id.lower(), {})
    online_clients[user_id.lower()] = {
        "timestamp": time.time(), "tier": hardware_tier, "model": model or prior.get("model"),
        "lane": lane or prior.get("lane"),
        "speed": avg_task_seconds if avg_task_seconds is not None else prior.get("speed"),
    }
    client_local_models = {m for m in available_models.split(",") if m}

    # The whole read-lock_state -> pick a task -> write-lock_state cycle inside _get_rag_work/
    # _get_finetune_work has to be one atomic unit -- see campaign_state_lock's comment. Without
    # this, two concurrent requests (e.g. a dual-lane client's two lanes, or two different
    # volunteers) can both read the state before either writes, and then both dispatch the exact
    # same chunk_id, or worse, interleave their writes and corrupt lock_state.json outright
    # (confirmed live under a concurrent-load test).
    with campaign_state_lock:
        if CURRENT_MODE == "rag":
            return _get_rag_work(user_id, hardware_tier, model)
        if CURRENT_MODE == "finetune":
            return _get_finetune_work(user_id, hardware_tier)
        if CURRENT_MODE == "audit":
            return _get_audit_work(user_id, hardware_tier, client_local_models)
        return {"mode": "idle", "status": "idle"}

def _submit_rag_work(submission: UnifiedSubmission) -> dict:
    state = load_lock_state(RAG_LOCK_FILE)

    # A chunk_id already in state["completed"] is normally a late/duplicate submission for
    # already-resolved work and should be ignored -- EXCEPT when it's also still in
    # rag_chunk_queue, meaning its source changed since that earlier completion and
    # rag_initialize_chunks() legitimately re-queued it (see _get_rag_work's comment). Checking
    # queue membership, not just completed-list membership, is what makes that re-crunch actually
    # reachable instead of silently unrecoverable forever.
    still_queued = any(t["chunk_id"] == submission.chunk_id for t in rag_chunk_queue)
    if submission.chunk_id in state["completed"] and not still_queued:
        state["locked"].pop(submission.chunk_id, None)
        save_lock_state(RAG_LOCK_FILE, state)
        return {"status": "ignored"}

    state["locked"].pop(submission.chunk_id, None)
    # Idempotent -- a re-crunched chunk (still_queued case above) may already be in
    # state["completed"] from its earlier pass; appending it again would let len(state["completed"])
    # exceed total_chunks and break every percentage/"done" calculation that assumes it's a count
    # of unique chunks, not completion events.
    if submission.chunk_id not in state["completed"]:
        state["completed"].append(submission.chunk_id)
    save_lock_state(RAG_LOCK_FILE, state)
    # rag_chunk_queue is built once at startup and never otherwise pruned as chunks complete --
    # removing the completed-list dispatch check above (needed so a hash-changed re-queued chunk
    # is reachable at all) means a chunk that just finished would be immediately offered right
    # back out on the very next poll if it weren't also dropped from the live queue here.
    # Confirmed as a real, live infinite-loop bug for the identical pattern in audit mode (see
    # _mark_done's comment) -- fixed here too before it was ever actually hit for RAG, since RAG
    # rarely re-queues a chunk mid-session, but it's the exact same latent bug either way.
    rag_chunk_queue[:] = [t for t in rag_chunk_queue if t["chunk_id"] != submission.chunk_id]
    _record_completion(rag_completion_log)

    user_stats = load_user_stats(RAG_STATS_FILE)
    user_key = submission.user_id.lower()
    if user_key not in user_stats:
        user_stats[user_key] = {"chunks_completed": 0, "lines_crunched": 0}
    user_stats[user_key]["chunks_completed"] += 1
    user_stats[user_key]["lines_crunched"] += submission.lines_crunched or 0
    save_user_stats(RAG_STATS_FILE, user_stats)

    user_folder = os.path.join(USERS_DIR, submission.user_id.lower())
    os.makedirs(user_folder, exist_ok=True)

    # Route by the chunk's own recorded directory_context (set once, authoritatively, at ingestion
    # time in rag_initialize_chunks()) rather than pattern-matching the submitted title. Title is
    # built client-side from the chunk's relative_path -- for GitHub review chunks that's the path
    # of the file *being reviewed*, which never contains the word "review", so title-based
    # matching would silently misfile every review chunk into codebase.jsonl.
    original_task = next((t for t in rag_chunk_queue if t["chunk_id"] == submission.chunk_id), None)
    directory_context = (original_task or {}).get("directory_context", "").upper()

    if "GITHUB_REVIEWS" in directory_context:
        target_file = "github_reviews.jsonl"
    elif "DEFINITIVE_WIKI_DOCUMENTATION" in directory_context:
        target_file = "wiki.jsonl"
    elif "ADDON_STUDIO" in directory_context:
        target_file = "addon_studio.jsonl"
    else:
        target_file = "codebase.jsonl"

    user_file = os.path.join(user_folder, target_file)
    # Only the RAG-relevant subset of UnifiedSubmission's fields -- not a raw dump of the whole
    # model, which would otherwise pollute this output with always-empty finetune-only fields
    # (source_type, pairs) that downstream consumers of codebase.jsonl/wiki.jsonl don't expect.
    output_record = {
        "chunk_id": submission.chunk_id,
        "summary": submission.summary,
        "comprehensive_explanation": submission.comprehensive_explanation,
        "symbols": submission.symbols,
        "concepts": submission.concepts,
        "keywords": submission.keywords,
        "chunk_type": submission.chunk_type,
        "code_example": submission.code_example,
        "synthetic_queries": submission.synthetic_queries,
        "title": submission.title,
        "user_id": submission.user_id,
        "lines_crunched": submission.lines_crunched,
    }
    with open(user_file, "a", encoding="utf-8") as out_f:
        out_f.write(json.dumps(output_record) + "\n")

    log_event("rag", submission.user_id, "✓", Colors.GREEN, f"{submission.title} → {target_file} ({submission.lines_crunched} LOC)", short="SUBMITTED")
    return {"status": "success"}

def _submit_finetune_work(submission: UnifiedSubmission) -> dict:
    state = load_lock_state(FINETUNE_LOCK_FILE)
    # See _submit_rag_work's comment -- same reasoning, same fix: only ignore this as a stale/
    # duplicate submission if it's ALSO no longer in the active queue. Still in the queue means
    # finetune_initialize_chunks() re-queued it (its knowledge_base source changed since the
    # earlier completion), and this submission is the legitimate redo, not a duplicate.
    still_queued = any(t["chunk_id"] == submission.chunk_id for t in finetune_chunk_queue)
    if submission.chunk_id in state["completed"] and not still_queued:
        state["locked"].pop(submission.chunk_id, None)
        save_lock_state(FINETUNE_LOCK_FILE, state)
        return {"status": "ignored"}

    state["locked"].pop(submission.chunk_id, None)
    # Idempotent -- see _submit_rag_work's comment on why appending unconditionally would let
    # len(state["completed"]) exceed total_chunks once a chunk can legitimately complete twice.
    if submission.chunk_id not in state["completed"]:
        state["completed"].append(submission.chunk_id)
    save_lock_state(FINETUNE_LOCK_FILE, state)
    # finetune_chunk_queue is built once at startup and never otherwise pruned as chunks
    # complete -- see _mark_done's comment (the identical bug, confirmed live there) for why a
    # chunk that just resolved needs to be dropped from the live queue too, not just left to the
    # completed-list check that was removed above to make re-queued chunks reachable at all.
    finetune_chunk_queue[:] = [t for t in finetune_chunk_queue if t["chunk_id"] != submission.chunk_id]
    _record_completion(finetune_completion_log)

    user_stats = load_user_stats(FINETUNE_STATS_FILE)
    user_key = submission.user_id.lower()
    if user_key not in user_stats:
        user_stats[user_key] = {"chunks_completed": 0, "pairs_generated": 0}
    user_stats[user_key]["chunks_completed"] += 1
    user_stats[user_key]["pairs_generated"] += len(submission.pairs)
    save_user_stats(FINETUNE_STATS_FILE, user_stats)

    user_folder = os.path.join(FINETUNE_OUTPUT_DIR, submission.user_id.lower())
    os.makedirs(user_folder, exist_ok=True)
    target_file = os.path.join(user_folder, f"{submission.source_type}_pairs.jsonl")
    with open(target_file, "a", encoding="utf-8") as out_f:
        out_f.write(json.dumps({
            "chunk_id": submission.chunk_id,
            "source_type": submission.source_type,
            "pairs": submission.pairs,
            "user_id": submission.user_id,
        }) + "\n")

    log_event("finetune", submission.user_id, "✓", Colors.GREEN, f"{submission.chunk_id} → {len(submission.pairs)} pairs", short="SUBMITTED")
    return {"status": "success"}

@app.post("/submit_work")
def submit_work(submission: UnifiedSubmission):
    if _parse_version(submission.client_version) < _parse_version(MIN_CLIENT_VERSION):
        raise HTTPException(status_code=426, detail=_version_rejection_message(submission.client_version))

    # Preserve whatever tier/model/lane/speed the last /get_work poll reported instead of
    # clobbering it -- this endpoint doesn't receive any of them, and online_clients is the shared
    # roster both /get_work and the capacity-based ETA (_capacity_based_eta) read from.
    _touch_first_seen(submission.user_id)
    _touch_connected_since(submission.user_id)
    prior = online_clients.get(submission.user_id.lower(), {})
    online_clients[submission.user_id.lower()] = {
        "timestamp": time.time(), "tier": prior.get("tier", "reporting"),
        "model": prior.get("model"), "lane": prior.get("lane"), "speed": prior.get("speed"),
    }

    # Same reasoning as /get_work's campaign_state_lock use -- _submit_rag_work/
    # _submit_finetune_work each do a read-modify-write on lock_state.json AND user_stats.json,
    # both shared across every volunteer (and, for a dual-lane client, both lanes of the same
    # machine too).
    with campaign_state_lock:
        if submission.mode == "finetune":
            return _submit_finetune_work(submission)
        if submission.mode == "audit":
            return _submit_audit_work(submission)
        return _submit_rag_work(submission)

def _merge_lane_children(rankings: list, sum_keys: list) -> list:
    """Folds a dual-lane secondary's or parallel worker's synthetic identity into its real
    owner's entry before the leaderboard is ranked or shown -- those synthetic ids exist purely
    so the ADMIN dashboard can show distinct per-lane hardware/status panels (see
    render_dashboard()); they were never meant to look like separate volunteers to anyone else.
    Confirmed live as confusing: a dual-lane or parallel-workers volunteer showed up split across
    2-4 tiny leaderboard rows (e.g. "nickc", "nicksrvrc", "nickpcc") instead of their real
    combined contribution under one name.

    Reconstructs parent from child structurally (child == parent[:11] + suffix) rather than
    needing the relationship recorded anywhere explicitly -- the exact inverse of how
    DualLaneController/ParallelWorkerPoolController build the child id. Only merges when the
    reconstructed parent is ALSO a real entry already in this same rankings list (so a
    coincidentally suffix-ending real name can never be misattributed to a non-existent parent),
    and only when the reconstruction is provably exact -- see the truncation-ambiguity note below.
    """
    by_id = {r["user_id"]: r for r in rankings}
    merged_away = set()
    for user_id in list(by_id.keys()):
        if user_id in merged_away or len(user_id) < 2 or user_id[-1] not in _LANE_CHILD_SUFFIXES:
            continue
        parent_id = user_id[:-1]
        if parent_id not in by_id or parent_id in merged_away:
            continue
        # A parent longer than 11 chars gets truncated before the suffix is appended, so its
        # child can't always be inverted back to the exact original parent id from the child
        # alone -- this check only accepts the reconstruction when it's provably exact (parent is
        # <=11 chars, or the truncated-and-resuffixed form matches the child exactly either way),
        # so an unprovable case is left as a separate row rather than risked as a wrong merge.
        if parent_id[:11] + user_id[-1] != user_id:
            continue
        entry, parent = by_id[user_id], by_id[parent_id]
        for k in sum_keys:
            if k in parent and k in entry:
                parent[k] = parent[k] + entry[k]
        if "ONLINE" in entry.get("status", "") and "ONLINE" not in parent.get("status", ""):
            parent["status"] = entry["status"]
        merged_away.add(user_id)
    return [r for uid, r in by_id.items() if uid not in merged_away]

def _rag_leaderboard() -> dict:
    state = load_lock_state(RAG_LOCK_FILE)
    user_stats = load_user_stats(RAG_STATS_FILE)

    total_chunks = rag_total_chunks  # true campaign size -- see _get_rag_work's comment
    completed_chunks = len(state["completed"])
    global_pct = (completed_chunks / total_chunks * 100) if total_chunks > 0 else 0.0

    # Union with online_clients, not just user_stats -- a node that has connected but not yet
    # completed a chunk (in this campaign specifically) has no stats entry yet, but should still
    # show up as an active user.
    known_users = set(user_stats.keys()) | set(online_clients.keys())

    # Denominator must be the same lifetime total the numerator is drawn from (sum of every
    # user's own chunks_completed), not completed_chunks -- that's the CURRENT campaign's
    # completed count, which resets to 0 on every hard reset while user_stats.chunks_completed
    # (deliberately) does not. Dividing a never-reset numerator by a just-reset denominator let
    # shares exceed 100% and stop summing to 100 across users.
    lifetime_total = sum(data.get("chunks_completed", 0) for data in user_stats.values())

    rankings = []
    for u_id in known_users:
        data = user_stats.get(u_id, {"chunks_completed": 0, "lines_crunched": 0})
        contribution = (data["chunks_completed"] / lifetime_total * 100) if lifetime_total > 0 else 0.0
        is_online = u_id in online_clients and (time.time() - online_clients[u_id]["timestamp"] < 60)

        rankings.append({
            "user_id": u_id,
            "chunks_completed": data["chunks_completed"],
            "lines_crunched": data["lines_crunched"],
            "contribution_percentage": round(contribution, 2),
            "status": "ONLINE 🟢" if is_online else "OFFLINE 🔴"
        })

    # Merged BEFORE contribution_percentage is recomputed -- that field is derived from
    # chunks_completed, not itself additive, so it has to be recalculated against each entry's
    # now-merged chunks_completed rather than summed like a raw count would be.
    rankings = _merge_lane_children(rankings, sum_keys=["chunks_completed", "lines_crunched"])
    for entry in rankings:
        entry["contribution_percentage"] = round((entry["chunks_completed"] / lifetime_total * 100) if lifetime_total > 0 else 0.0, 2)

    rankings.sort(key=lambda x: (x["chunks_completed"], x["lines_crunched"]), reverse=True)
    for index, entry in enumerate(rankings, 1):
        entry["rank"] = index

    return {
        "total_chunks_in_codebase": total_chunks,
        "total_chunks_completed": completed_chunks,
        "global_percentage": round(global_pct, 2),
        "eta_seconds": _eta_seconds(rag_completion_log, total_chunks - completed_chunks),
        "rankings": rankings
    }

def _finetune_leaderboard() -> dict:
    state = load_lock_state(FINETUNE_LOCK_FILE)
    user_stats = load_user_stats(FINETUNE_STATS_FILE)
    total_chunks = finetune_total_chunks  # true campaign size -- see _get_rag_work's comment
    completed_chunks = len(state["completed"])
    global_pct = (completed_chunks / total_chunks * 100) if total_chunks > 0 else 0.0

    known_users = set(user_stats.keys()) | set(online_clients.keys())
    rankings = []
    for u_id in known_users:
        data = user_stats.get(u_id, {"chunks_completed": 0, "pairs_generated": 0})
        is_online = u_id in online_clients and (time.time() - online_clients[u_id]["timestamp"] < 60)
        rankings.append({
            "user_id": u_id,
            "chunks_completed": data["chunks_completed"],
            "pairs_generated": data["pairs_generated"],
            "status": "ONLINE" if is_online else "OFFLINE",
        })
    rankings = _merge_lane_children(rankings, sum_keys=["chunks_completed", "pairs_generated"])
    rankings.sort(key=lambda x: (x["chunks_completed"], x["pairs_generated"]), reverse=True)
    for i, entry in enumerate(rankings, 1):
        entry["rank"] = i

    return {
        "total_chunks_in_campaign": total_chunks,
        "total_chunks_completed": completed_chunks,
        "global_percentage": round(global_pct, 2),
        "eta_seconds": _eta_seconds(finetune_completion_log, total_chunks - completed_chunks),
        "rankings": rankings,
    }

def _audit_leaderboard() -> dict:
    state = load_lock_state(AUDIT_LOCK_FILE)
    user_stats = load_user_stats(AUDIT_STATS_FILE)
    total_chunks = audit_total_chunks  # true campaign size -- see audit_initialize_chunks's comment
    # See _get_audit_work's comment -- same fix, same reasoning: a live "how much of THIS pass is
    # done" number, not a lifetime count that sits frozen during a re-audit pass.
    completed_chunks = total_chunks - len(audit_chunk_queue)
    global_pct = (completed_chunks / total_chunks * 100) if total_chunks > 0 else 0.0

    known_users = set(user_stats.keys()) | set(online_clients.keys())
    rankings = []
    for u_id in known_users:
        data = user_stats.get(u_id, _new_user_stats_entry())
        is_online = u_id in online_clients and (time.time() - online_clients[u_id]["timestamp"] < 60)
        rankings.append({
            "user_id": u_id,
            "chunks_audited": data.get("chunks_audited", 0),
            "issues_found": data.get("issues_found", 0),
            "reviews_done": data.get("reviews_done", 0),
            "fixes_applied": data.get("fixes_applied", 0),
            "status": "ONLINE" if is_online else "OFFLINE",
        })
    rankings = _merge_lane_children(rankings, sum_keys=["chunks_audited", "issues_found", "reviews_done", "fixes_applied"])
    rankings.sort(key=lambda x: (x["fixes_applied"], x["chunks_audited"]), reverse=True)
    for i, entry in enumerate(rankings, 1):
        entry["rank"] = i

    pending = read_json_file(AUDIT_PENDING_FILE, {})
    completed_since_tracking = completed_chunks - state.get("actions_baseline_completed", completed_chunks)
    return {
        "total_chunks_due": total_chunks,
        "total_chunks_completed": completed_chunks,
        "global_percentage": round(global_pct, 2),
        "in_flight_conversations": len(pending),
        "eta_seconds": _eta_seconds(audit_completion_log, total_chunks - completed_chunks,
                                     _audit_avg_actions_per_chunk(state.get("actions_count", 0), completed_since_tracking)),
        "rankings": rankings,
    }

@app.post("/delete_user")
def delete_user(user_id: str):
    """Purges every trace of one volunteer identity from the server -- raised by a volunteer's
    own request (see the pause menu's [X] option), e.g. after renaming, or just wanting to stop
    appearing on the leaderboard/dashboard under an old id. Deliberately thorough rather than
    just clearing user_stats: a half-deleted identity (still showing hardware info or "joined"
    time, or holding a stale chunk lock forever) would be a worse, more confusing state than
    either "fully present" or "fully gone."""
    if not user_id.isalpha() or not (3 <= len(user_id) <= 12):
        raise HTTPException(status_code=400, detail="Invalid user_id.")
    user_key = user_id.lower()

    with campaign_state_lock:
        # Release any chunk currently locked to this user across every campaign, rather than
        # leaving it to sit locked until TASK_TIMEOUT expires on its own -- someone else should be
        # able to pick it up immediately, not wait out a timeout for a user who no longer exists.
        for lock_file in (RAG_LOCK_FILE, FINETUNE_LOCK_FILE, AUDIT_LOCK_FILE):
            state = load_lock_state(lock_file)
            released = [cid for cid, info in state["locked"].items() if info.get("user_id", "").lower() == user_key]
            for cid in released:
                state["locked"].pop(cid, None)
            if released:
                save_lock_state(lock_file, state)

        # Per-campaign stats/leaderboard entries.
        for stats_file in (RAG_STATS_FILE, FINETUNE_STATS_FILE, AUDIT_STATS_FILE):
            stats = load_user_stats(stats_file)
            if user_key in stats:
                del stats[user_key]
                save_user_stats(stats_file, stats)

        # Live dashboard / identity state -- both the in-memory copy AND the persisted file for
        # first-seen/hardware-info, which otherwise survive a server restart forever (see
        # USER_FIRST_SEEN_FILE's and USER_HARDWARE_INFO_FILE's own comments on why they're
        # persisted at all).
        online_clients.pop(user_key, None)
        _user_first_seen.pop(user_key, None)
        try:
            with open(USER_FIRST_SEEN_FILE, "w", encoding="utf-8") as f:
                json.dump(_user_first_seen, f, indent=2)
        except Exception:
            pass
        _user_hardware_info.pop(user_key, None)
        _save_user_hardware_info()
        audit_model_assignments.pop(user_key, None)
        write_json_file(AUDIT_MODEL_ASSIGNMENTS_FILE, audit_model_assignments, "audit model assignments")

        # log_event() itself writes into _user_last_status (and, since this is RED-severity, into
        # _user_error_counts) as a side effect of recording the announcement -- called deliberately
        # INSIDE the lock and BEFORE the two lines below, so those two pops are what actually have
        # the last word. Popping first and logging after (the original order here) silently
        # resurrected both entries for a user that otherwise no longer exists anywhere -- confirmed
        # by a real before/after test against live state, not just read from the code.
        log_event("admin", user_id, "✗", Colors.RED, f"'{user_id}' deleted their identity from the server")
        _user_last_status.pop(user_key, None)
        _user_error_counts.pop(user_key, None)

    return {"status": "deleted", "user_id": user_id}

@app.api_route("/disconnect", methods=["GET", "POST"])
def disconnect(user_id: str, lane: str = ""):
    """Called by the client on clean exit to immediately mark this lane as offline, rather than
    waiting for the 60-second ONLINE_STALE_SECONDS timeout to expire naturally.  Removes the
    lane from online_clients immediately so the dashboard sees it as offline on the very next frame."""
    user_key = user_id.lower()
    with campaign_state_lock:
        online_clients.pop(user_key, None)
        _user_connected_since.pop(user_key, None)
        label = f" [{lane}]" if lane else ""
        log_event("info", user_id, "↓", Colors.GRAY, f"'{user_id}'{label} disconnected cleanly")
    return {"status": "ok"}


@app.post("/rename_user")
def rename_user(old_user_id: str, new_user_id: str):
    """Migrates every trace of one volunteer identity to a new name, instead of the old_user_id's
    entire history just sitting orphaned while new_user_id starts over at zero. Confirmed live as
    a real gap: the pause menu's [N] option originally only changed what the CLIENT saves
    locally -- the server had no idea the new name was the same person, so it looked exactly like
    a brand-new volunteer with no history, and the old name's stats/leaderboard entry/hardware
    info were never touched at all. Mirrors delete_user's list of what counts as "every trace,"
    just moving each piece to the new key instead of discarding it."""
    for uid in (old_user_id, new_user_id):
        if not uid.isalpha() or not (3 <= len(uid) <= 12):
            raise HTTPException(status_code=400, detail=f"Invalid user_id: '{uid}'.")
    old_key, new_key = old_user_id.lower(), new_user_id.lower()
    if old_key == new_key:
        raise HTTPException(status_code=400, detail="New name is the same as the old one.")

    with campaign_state_lock:
        # Refuse if new_user_id is already a real, distinct identity with its own history --
        # renaming INTO it would silently merge two different volunteers' stats together, which
        # is a much worse outcome than just asking for a different name.
        stats_snapshots = {f: load_user_stats(f) for f in (RAG_STATS_FILE, FINETUNE_STATS_FILE, AUDIT_STATS_FILE)}
        if new_key != old_key and (new_key in _user_first_seen or any(new_key in s for s in stats_snapshots.values())):
            raise HTTPException(status_code=409, detail=f"'{new_user_id}' already exists on the server -- pick a different name.")

        # Reassign (not release) any chunk currently locked to the old name, so in-flight work
        # this exact rename request interrupted isn't lost or handed to someone else mid-task.
        for lock_file in (RAG_LOCK_FILE, FINETUNE_LOCK_FILE, AUDIT_LOCK_FILE):
            state = load_lock_state(lock_file)
            changed = False
            for info in state["locked"].values():
                if info.get("user_id", "").lower() == old_key:
                    info["user_id"] = new_user_id
                    changed = True
            if changed:
                save_lock_state(lock_file, state)

        # Per-campaign stats/leaderboard entries.
        for stats_file, stats in stats_snapshots.items():
            if old_key in stats:
                stats[new_key] = stats.pop(old_key)
                save_user_stats(stats_file, stats)

        # Live dashboard / identity state.
        if old_key in online_clients:
            online_clients[new_key] = online_clients.pop(old_key)
        if old_key in _user_connected_since:
            _user_connected_since[new_key] = _user_connected_since.pop(old_key)
        if old_key in _user_first_seen:
            _user_first_seen[new_key] = _user_first_seen.pop(old_key)
            try:
                with open(USER_FIRST_SEEN_FILE, "w", encoding="utf-8") as f:
                    json.dump(_user_first_seen, f, indent=2)
            except Exception:
                pass
        if old_key in _user_hardware_info:
            _user_hardware_info[new_key] = _user_hardware_info.pop(old_key)
            _save_user_hardware_info()
        if old_key in audit_model_assignments:
            audit_model_assignments[new_key] = audit_model_assignments.pop(old_key)
            write_json_file(AUDIT_MODEL_ASSIGNMENTS_FILE, audit_model_assignments, "audit model assignments")

        log_event("admin", new_user_id, "→", Colors.CYAN, f"'{old_user_id}' renamed to '{new_user_id}'")
        _user_last_status.pop(old_key, None)
        _user_error_counts[new_key] = _user_error_counts.pop(old_key, 0)

    return {"status": "renamed", "old_user_id": old_user_id, "new_user_id": new_user_id}

@app.post("/merge_user")
def merge_user(absorbed_user_id: str, into_user_id: str):
    """Combines two REAL, independent identities that turned out to be the same volunteer (e.g.
    a rename that happened before rename_user's server-side migration existed, so the old name's
    history was left orphaned instead of moved) -- unlike rename_user, this is explicitly for the
    case where into_user_id already has its own real history too, and both should be summed
    together rather than one refusing to overwrite the other. Stats are additive across every
    campaign; first_seen keeps whichever is EARLIER (the absorbed identity may well be the older
    one, e.g. a volunteer's original name from early in the project); hardware_info keeps
    into_user_id's (the current name is the one still actively reporting real specs)."""
    for uid in (absorbed_user_id, into_user_id):
        if not uid.isalpha() or not (3 <= len(uid) <= 12):
            raise HTTPException(status_code=400, detail=f"Invalid user_id: '{uid}'.")
    absorbed_key, into_key = absorbed_user_id.lower(), into_user_id.lower()
    if absorbed_key == into_key:
        raise HTTPException(status_code=400, detail="Both names are the same identity already.")

    with campaign_state_lock:
        for lock_file in (RAG_LOCK_FILE, FINETUNE_LOCK_FILE, AUDIT_LOCK_FILE):
            state = load_lock_state(lock_file)
            changed = False
            for info in state["locked"].values():
                if info.get("user_id", "").lower() == absorbed_key:
                    info["user_id"] = into_user_id
                    changed = True
            if changed:
                save_lock_state(lock_file, state)

        # Per-campaign stats -- summed field by field (not a blind dict overwrite), since either
        # side might be missing fields the other has (different campaign shapes, or a fresh
        # identity that's never submitted to this particular campaign yet).
        for stats_file in (RAG_STATS_FILE, FINETUNE_STATS_FILE, AUDIT_STATS_FILE):
            stats = load_user_stats(stats_file)
            if absorbed_key in stats:
                absorbed_data = stats.pop(absorbed_key)
                into_data = stats.setdefault(into_key, {})
                for k, v in absorbed_data.items():
                    if isinstance(v, (int, float)):
                        into_data[k] = into_data.get(k, 0) + v
                    elif k not in into_data:
                        into_data[k] = v
                save_user_stats(stats_file, stats)

        online_clients.pop(absorbed_key, None)
        if absorbed_key in _user_first_seen:
            absorbed_seen = _user_first_seen.pop(absorbed_key)
            if into_key not in _user_first_seen or absorbed_seen < _user_first_seen[into_key]:
                _user_first_seen[into_key] = absorbed_seen
            try:
                with open(USER_FIRST_SEEN_FILE, "w", encoding="utf-8") as f:
                    json.dump(_user_first_seen, f, indent=2)
            except Exception:
                pass
        _user_hardware_info.pop(absorbed_key, None)
        _save_user_hardware_info()
        audit_model_assignments.pop(absorbed_key, None)
        write_json_file(AUDIT_MODEL_ASSIGNMENTS_FILE, audit_model_assignments, "audit model assignments")

        log_event("admin", into_user_id, "→", Colors.CYAN, f"'{absorbed_user_id}' merged into '{into_user_id}'")
        _user_last_status.pop(absorbed_key, None)
        _user_error_counts.pop(absorbed_key, None)

    return {"status": "merged", "absorbed_user_id": absorbed_user_id, "into_user_id": into_user_id}

@app.get("/leaderboard")
def get_leaderboard():
    # Reflects whichever campaign is currently active, same as /get_work -- defaults to the RAG
    # shape while idle (arbitrary but stable) rather than returning nothing.
    if CURRENT_MODE == "finetune":
        result = _finetune_leaderboard()
    elif CURRENT_MODE == "audit":
        result = _audit_leaderboard()
    else:
        result = _rag_leaderboard()
    result["mode"] = CURRENT_MODE
    return result

@app.get("/admin/audit_pending")
def get_audit_pending():
    """Every chunk currently mid-conversation (proposed and awaiting review, or sent back for
    revision) -- lets an operator see what's in flight without waiting for it to resolve on its
    own."""
    return read_json_file(AUDIT_PENDING_FILE, {})

@app.get("/admin/mode")
def get_mode():
    return {"mode": CURRENT_MODE}

@app.post("/admin/mode")
def set_mode(mode: str, force: bool = False):
    global CURRENT_MODE
    if mode not in ("idle", "rag", "finetune", "audit"):
        raise HTTPException(status_code=400, detail="mode must be one of: idle, rag, finetune, audit")
    if mode == "finetune" and not force and not _rag_campaign_complete():
        total = len(rag_chunk_queue)
        completed = len(load_lock_state(RAG_LOCK_FILE)["completed"])
        raise HTTPException(
            status_code=409,
            detail=f"RAG campaign is not finished ({completed}/{total} chunks) -- fine-tune pair "
                   f"generation is meant to run after RAG extraction completes. Retry with "
                   f"force=true to override."
        )
    CURRENT_MODE = mode
    # Marked dirty (clean_shutdown=False) immediately -- if the process dies before a clean
    # shutdown writes True, the next startup's "unfinished campaign" flag reflects THIS mode,
    # not whatever was persisted before the switch.
    save_server_mode_state(CURRENT_MODE, clean_shutdown=False)
    log_event("admin", "", "⚙", Colors.WHITE + Colors.BOLD, f"campaign mode switched to {mode.upper()}")
    return {"mode": CURRENT_MODE}

@app.get("/version")
def get_version():
    return {
        "min_client_version": MIN_CLIENT_VERSION,
        "latest_client_version": LATEST_CLIENT_VERSION,
        "download_url": CLIENT_DOWNLOAD_URL,
    }

@app.post("/diagnostics")
def submit_diagnostics(payload: dict):
    # Deliberately a raw dict, not a Pydantic model -- this is observability data, not campaign
    # state, so it shouldn't need a schema migration every time a new diagnostic field is added
    # client-side. task_gave_up/task_cancelled/session_start events land here (see
    # CUBYZ_FOLDING.py's submit_diagnostic_to_server()) -- the much chattier per-attempt
    # task_retry events stay purely local, so this endpoint doesn't get hit on every single retry.
    payload["received_at"] = time.time()
    append_jsonl(CLIENT_DIAGNOSTICS_FILE, payload, "client diagnostic")

    if payload.get("event") == "session_start" and payload.get("user_id"):
        # The admin dashboard used to have zero hardware info for any volunteer -- OS, GPU
        # vendor, VRAM, system RAM -- confirmed live. This is the one place that information
        # actually reaches the server at all, so it's captured into its own dict (not just left
        # sitting in the append-only diagnostics log) for render_dashboard() to read directly.
        _user_hardware_info[payload["user_id"].lower()] = {
            "platform": payload.get("platform"), "gpu_type": payload.get("gpu_type"),
            "total_vram_gb": payload.get("total_vram_gb"), "system_ram_gb": payload.get("system_ram_gb"),
            "dual_lane": payload.get("dual_lane"),
            # primary_is_gpu/benchmark_*_time were already being sent in this same event and
            # silently dropped -- exactly the data needed to explain the confusing-looking case of
            # a real, correctly-detected GPU sitting unused while the client runs on CPU: VRAM
            # detection succeeding just means the card exists, not that benchmark_lane() (a real
            # inference call, not a guess) found it fast/working enough to actually use. Confirmed
            # live: a volunteer's dashboard panel showed "NVIDIA GPU (12GB VRAM)" right next to
            # "lane: CPU" with nothing explaining the gap.
            "primary_is_gpu": payload.get("primary_is_gpu"),
            # Never actually captured despite being in the payload all along -- _format_benchmark_note's
            # capability-tier explanation showed "(?)" for the winning tier instead of e.g. "medium".
            "hardware_tier": payload.get("hardware_tier"),
            "benchmark_gpu_time": payload.get("benchmark_gpu_time"),
            "benchmark_cpu_time": payload.get("benchmark_cpu_time"),
            # The actual exception (timeout vs connection error vs Ollama-side error, etc.) --
            # benchmark_lane() used to swallow this into a bare None, so a failed GPU benchmark
            # was completely unexplainable from the dashboard beyond "FAILED or timed out".
            "benchmark_gpu_error": payload.get("benchmark_gpu_error"),
            "benchmark_cpu_error": payload.get("benchmark_cpu_error"),
        }
        _save_user_hardware_info()

    if payload.get("event") == "task_gave_up" and payload.get("mode") == "rag":
        chunk_id = payload.get("chunk_id")
        # See campaign_state_lock's comment -- same read-modify-write hazard on lock_state.json.
        if chunk_id:
            with campaign_state_lock:
                state = load_lock_state(RAG_LOCK_FILE)
                if chunk_id not in state["completed"]:
                    # Release the lock immediately (don't make the next node wait out the full
                    # TASK_TIMEOUT before they can even try) and count this as one independent
                    # give-up. Only after RAG_GIVE_UP_THRESHOLD separate nodes have all given up
                    # is the chunk marked permanently completed -- with no RAG output ever
                    # written for it, which is the accepted tradeoff (finetune's 0-pairs give-up
                    # path already accepts the same tradeoff) against the alternative of infinite
                    # wasted swarm compute on a chunk that's structurally never going to pass
                    # validation.
                    state["locked"].pop(chunk_id, None)
                    gave_up_counts = state.setdefault("gave_up_counts", {})
                    gave_up_counts[chunk_id] = gave_up_counts.get(chunk_id, 0) + 1
                    if gave_up_counts[chunk_id] >= RAG_GIVE_UP_THRESHOLD:
                        state["completed"].append(chunk_id)
                        gave_up_counts.pop(chunk_id, None)
                        log_event("rag", "", "⚠", Colors.RED, f"{Colors.BOLD}{chunk_id}{Colors.RESET} permanently given up after {RAG_GIVE_UP_THRESHOLD} independent failures -- marked done with no output")
                    save_lock_state(RAG_LOCK_FILE, state)

    return {"status": "logged"}

if __name__ == "__main__":
    import uvicorn

    if _TTY:
        # rag/finetune/audit_initialize_chunks() print their scan summaries with plain print() --
        # normally fine, but under the textual console there's no UI up yet to show them in, so
        # they'd otherwise flash past as ordinary scrollback right before the screen cuts over to
        # the panel (confirmed live). Captured here and replayed into the Events panel instead
        # (see _seed_startup_events()) so that content is visible WITHIN the console, not before
        # it. A SystemExit (e.g. a missing source directory -- a real fatal misconfiguration, not
        # a startup formality) is deliberately let through to the real terminal instead of being
        # swallowed silently, since the console never gets a chance to open in that case anyway.
        # verbose=False on all three: their "PIPELINE METRICS" banners are pure decoration
        # (title + separator lines) that ate most of the Events panel's 10-line budget with no
        # real information a fresh operator needs -- confirmed live, Nick asked for them gone.
        # Genuine warnings/errors from inside these functions (a corrupt source file, a missing
        # directory) aren't behind the verbose flag, so they still get captured and seeded below.
        import io, contextlib
        _startup_buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(_startup_buf):
                rag_initialize_chunks(verbose=False)
                finetune_initialize_chunks(verbose=False)
                audit_initialize_chunks(verbose=False)
        except SystemExit:
            sys.stdout.write(_startup_buf.getvalue())
            raise
        _seed_startup_events(_startup_buf.getvalue())
    else:
        rag_initialize_chunks()
        finetune_initialize_chunks()
        audit_initialize_chunks()

    if _TTY:
        # The old CLI startup menu (server_startup_gate(), still used below for the non-TTY
        # branch) picked the initial mode with a numbered prompt before anything else ran --
        # redundant now that CubyzAdminApp's own Campaign Mode RadioSet does the exact same job
        # live, on the same screen as everything else, and can be changed anytime without a
        # restart. CURRENT_MODE just starts at its module-level default ("idle") and the operator
        # picks a real mode from the sidebar once the console is up.
        pass
    else:
        # No real terminal to run the interactive console against -- fall back to the original
        # numbered-menu gate so a mode still has to be picked deliberately before serving.
        server_startup_gate()

    # Dirty the persisted state the moment we're about to actually start serving -- only the
    # finally block below (a real clean stop) clears it back to True.
    save_server_mode_state(CURRENT_MODE, clean_shutdown=False)

    if _TTY:
        # See _run_uvicorn_in_background's comment: textual's driver needs the main thread for
        # its own signal handling, so uvicorn runs in the background here instead -- the inverse
        # of every prior version of this file (and of the non-TTY branch below).
        _DASHBOARD_ACTIVE = True
        threading.Thread(target=_run_uvicorn_in_background, daemon=True).start()
        try:
            CubyzAdminApp().run()
        except KeyboardInterrupt:
            pass
        finally:
            save_server_mode_state(CURRENT_MODE, clean_shutdown=True)
            print("\n[X] Server shut down cleanly.")
    else:
        # No real terminal to run an interactive console against (piped output, a log file, a
        # systemd unit) -- uvicorn just runs directly in the main thread here, same as every
        # version of this file before textual was introduced, with plain sequential
        # log_event() lines instead of a live console.
        try:
            # access_log=False turns off uvicorn's own per-request "INFO: <ip> - "GET ...
            # HTTP/1.1" 200 OK" line -- every request already gets a real, readable log_event()
            # line above when something meaningful actually happens (a task dispatched, a fix
            # applied, etc), so the raw access log was pure noise on top of that. Startup
            # messages and real errors (5xx, exceptions inside a route) still print via
            # uvicorn's separate error logger, unaffected by this.
            uvicorn.run(app, host="0.0.0.0", port=7000, access_log=False)
        except KeyboardInterrupt:
            pass
        finally:
            save_server_mode_state(CURRENT_MODE, clean_shutdown=True)
            print("\n[X] Server shut down cleanly.")
