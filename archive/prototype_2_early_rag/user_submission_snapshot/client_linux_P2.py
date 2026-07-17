import os
import sys
import json
import time
import subprocess
import shutil
import urllib.request
import urllib.error
import signal

if not sys.platform.startswith("linux"):
    sys.exit("[X] This script is explicitly configured for Linux systems only.")

SERVER_URL = "http://ashframe.net:7000"
OLLAMA_URL = "http://localhost:11434/api/generate"

SESSION_CHUNKS_COMPLETED = 0
SESSION_LINES_CRUNCHED = 0
CURRENT_DASHBOARD_STATE = None

RAG_JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "summary": {"type": "string"},
        "comprehensive_explanation": {"type": "string"},
        "code_example": {"type": ["string", "null"]},
        "synthetic_queries": {"type": "array", "items": {"type": "string"}, "minItems": 2, "maxItems": 4}
    },
    "required": ["summary", "comprehensive_explanation", "code_example", "synthetic_queries"]
}

BASE_SYSTEM_PROMPT = """You are a deterministic data-extraction compiler documenting the Cubyz voxel engine.
Your task is to parse raw content and emit strict JSON mapping its technical realities.

## Source Weight Hierarchy:
- WIKI (.md, .txt): Definitive functional/gameplay ground truth.
- CODE (.zig): Structural foundation for concrete architecture, syntax, and execution pathways.
- GITHUB REVIEWS: Historical context for debugging, design adjustments, and troubleshooting regressions.

## Operational Constraints:
1. ZERO EXTRAPOLATION: Rely exclusively on explicit tokens and syntax present in the chunk. Never assume behaviors.
2. COMPACT SENTENCES: Omit filler words, narrative setups, and conversational transitions. Provide raw, high-density facts.
3. CODE RULES: Write minimal, fully-functional Zig code blocks for .zig files. For non-code documents or where no logic exists, set 'code_example' to null.
4. JSON PURITY: Do not wrap output in Markdown text prose. Emit only the exact schema-compliant JSON structure.
"""

LOW_VRAM_REASONING_RULE = """
5. THOUGHT CONSTRAINT: Before emitting final fields, use the first 2 sentences of 'comprehensive_explanation' to map explicitly found dependencies, scopes, and signatures to guarantee logical correctness under local hardware limits.
"""

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
    try:
        with open("/proc/meminfo", "r") as f:
            for line in f:
                if line.startswith("MemTotal:"):
                    return int(line.split()[1]) / 1048576.0
    except Exception:
        pass
    return 8.0

def detect_gpu() -> tuple:
    system_ram = get_system_ram_gb()
    try:
        res = subprocess.run(['nvidia-smi', '--query-gpu=memory.total', '--format=csv,nounits,noheader'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return "nvidia", float(res.stdout.strip().split('\n')[0]) / 1024.0
    except Exception:
        pass
    try:
        pci = subprocess.run(['lspci'], stdout=subprocess.PIPE, text=True).stdout.lower()
        if "nvidia" in pci:
            return "nvidia", 0.0
        if "amd" in pci or "radeon" in pci:
            if "graphics" in pci and "apu" in pci:
                return "amd_integrated", system_ram * 0.4
            return "amd", 16.0
        if "intel" in pci and any(x in pci for x in ["arc", "graphics", "dg2"]):
            if any(x in pci for x in ["iris", "hd graphics", "xe"]):
                return "intel_integrated", system_ram * 0.4
            return "intel", 16.0
    except Exception:
        pass
    return None, 0.0

def get_vram_and_choose_model() -> tuple:
    gpu_type, total_vram_gb = detect_gpu()
    system_ram_gb = get_system_ram_gb()

    if total_vram_gb >= 22.0:
        model = "qwen3.5:27b"
    elif total_vram_gb >= 11.0 or (gpu_type in ["amd", "intel"] and total_vram_gb > 8.0):
        model = "qwen3.5:9b"
    elif total_vram_gb >= 7.0:
        model = "qwen3.5:9b"
    elif total_vram_gb >= 5.5:
        model = "qwen3.5:4b"
    elif total_vram_gb >= 3.5:
        model = "qwen3.5:2b"
    else:
        if system_ram_gb >= 11.0:
            model = "qwen3:1.5b"
            gpu_type = "cpu"
        else:
            print(f"[X] Insufficient resource pools: {total_vram_gb:.1f} GB VRAM, {system_ram_gb:.1f} GB RAM.")
            sys.exit(1)
    return model, gpu_type, total_vram_gb

def fix_docker_permissions():
    try:
        if subprocess.run(["docker", "ps"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
            return
    except Exception:
        pass
    try:
        subprocess.run("sudo groupadd -f docker && sudo usermod -aG docker $USER", shell=True, check=True)
        os.execvp("sg", ["sg", "docker", "-c", f"{sys.executable} {' '.join(sys.argv)}"])
    except subprocess.CalledProcessError:
        sys.exit("[X] Refused to elevate permissions. Execution halted.")

def check_docker_ollama() -> bool:
    if not shutil.which("docker"):
        return False
    fix_docker_permissions()
    try:
        res = subprocess.run(["docker", "ps", "-a", "--filter", "name=ollama", "--format", "{{.Names}}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return "ollama" in res.stdout
    except Exception:
        return False

def check_bare_metal_ollama() -> bool:
    return shutil.which("ollama") is not None

def install_docker():
    distro = get_linux_distro()
    try:
        if distro in ["ubuntu", "debian", "pop", "mint"]:
            subprocess.run("sudo apt-get update && sudo apt-get install -y docker.io", shell=True, check=True)
        elif distro in ["fedora", "rhel", "centos"]:
            subprocess.run("sudo dnf install -y docker", shell=True, check=True)
        elif distro in ["arch", "manjaro"]:
            subprocess.run("sudo pacman -S --noconfirm docker", shell=True, check=True)
        else:
            subprocess.run("curl -fsSL https://get.docker.com | sh", shell=True, check=True)
        subprocess.run("sudo systemctl enable --now docker", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(f"[X] Docker installation failed: {e}")

def install_ollama_container(gpu_type: str):
    gpu_flags = ""
    image_name = "ollama/ollama"
    distro = get_linux_distro()

    if gpu_type == "nvidia":
        try:
            if distro in ["ubuntu", "debian", "pop"]:
                subprocess.run("curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg", shell=True, check=True)
                subprocess.run(". /etc/os-release; curl -s -L https://nvidia.github.io/libnvidia-container/$ID$VERSION_ID/libnvidia-container.list | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list", shell=True, check=True)
                subprocess.run("sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit", shell=True, check=True)
            elif distro in ["arch", "manjaro"]:
                subprocess.run("sudo pacman -S --noconfirm nvidia-container-toolkit", shell=True, check=True)
            elif distro in ["fedora"]:
                subprocess.run("sudo dnf config-manager --add-repo=https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo && sudo dnf install -y nvidia-container-toolkit", shell=True, check=True)
            subprocess.run("sudo systemctl restart docker", shell=True, check=True)
            gpu_flags = "--gpus all"
        except Exception:
            gpu_flags = ""
    elif gpu_type in ["amd", "amd_integrated"]:
        gpu_flags = "--device /dev/kfd --device /dev/dri"
        image_name = "ollama/ollama:rocm"
    elif gpu_type in ["intel", "intel_integrated"]:
        gpu_flags = "--device /dev/dri"

    try:
        subprocess.run(f"sudo docker run -d {gpu_flags} -v ollama:/root/.ollama -p 11434:11434 --name ollama {image_name}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(f"[X] Failed to deploy container: {e}")

def ensure_ollama_installed(gpu_type: str):
    if check_bare_metal_ollama() or check_docker_ollama():
        return
    docker_choice = input("Would you like to run Ollama inside a Docker container? (y/n): ").strip().lower()
    if docker_choice == 'y':
        if not shutil.which("docker"):
            if input("Install Docker automatically? (y/n): ").strip().lower() == 'y':
                install_docker()
            else:
                sys.exit("[X] Docker is required to deploy the container. Aborting.")
        install_ollama_container(gpu_type)
    else:
        try:
            subprocess.run("curl -fsSL https://ollama.com/install.sh | sh", shell=True, check=True)
        except Exception as e:
            sys.exit(f"[X] Manual script execution failed: {e}")

def make_request(url, payload=None):
    data = json.dumps(payload).encode('utf-8') if payload else None
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'} if data else {})
    with urllib.request.urlopen(req, timeout=120) as res:
        return json.loads(res.read().decode('utf-8'))

def fetch_user_all_time_stats(user_id: str) -> tuple:
    try:
        for user in make_request(f"{SERVER_URL}/leaderboard").get("rankings", []):
            if user["user_id"].lower() == user_id.lower():
                return user["chunks_completed"], user["lines_crunched"]
    except Exception:
        pass
    return 0, 0

def handle_interrupt_menu():
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    # Cleanly erase the dashboard block space by jumping up 9 lines
    if CURRENT_DASHBOARD_STATE:
        sys.stdout.write("\033[2K\r\033[9F\033[s\033[J")
    else:
        sys.stdout.write("\033[2K\r\033[s\033[J")
    sys.stdout.flush()

    def redraw(lines):
        sys.stdout.write("\033[u\033[J")
        for line in lines:
            print(line)
        print("\n[||] Node Execution Paused. Press [R] Resume │ [L] Leaderboard │ [U] Active Users │ [Q] Exit")
        sys.stdout.flush()

    redraw([])
    try:
        while True:
            tty.setraw(fd)
            choice = sys.stdin.read(1).lower()
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

            # \x03 is the raw escape code for Ctrl+C, allowing a clean unpause if pressed again
            if choice == "r" or choice == "\x03":
                sys.stdout.write("\033[u\033[J")
                sys.stdout.flush()
                # Reprint the dashboard right into the cleared space
                if CURRENT_DASHBOARD_STATE:
                    print_dashboard(*CURRENT_DASHBOARD_STATE, is_first=True)
                return
            elif choice == "q":
                sys.exit("\n[X] Disconnecting safely. Contributions preserved.")
            elif choice in ("l", "u"):
                try:
                    stats = make_request(f"{SERVER_URL}/leaderboard")
                except Exception:
                    stats = {}
                lines = []
                if choice == "l":
                    rankings = stats.get("rankings", [])[:3]
                    lines.append("╔" + "═"*68 + "╗\n║ " + f"{'CUBYZ DISTRIBUTED LEADERBOARD':^66}" + " ║\n╟" + "─"*68 + "╢")
                    lines.append(f"║ Progress: {stats.get('total_chunks_completed', 0)}/{stats.get('total_chunks_in_codebase', 1500)} Chunks Analyzed ({stats.get('global_percentage', 0.0):.2f}%)".ljust(69) + "║")
                    lines.append("╟" + "─"*68 + "╢\n" + f"║ {'Rank':<5} │ {'User ID':<12} │ {'Chunks':<8} │ {'Lines':<10} │ {'Status':<14} ║\n╟" + "─"*68 + "╢")
                    for user in rankings:
                        lines.append(f"║ #{user['rank']:<4} │ {user['user_id']:<12} │ {user['chunks_completed']:<8} │ {user['lines_crunched']:<10} │ {user.get('status', 'OFFLINE'):<14} ║")
                    for _ in range(3 - len(rankings)):
                        lines.append(f"║ {' ':<5} │ {'-':<12} │ {'-':<8} │ {'-':<10} │ {'-':<14} ║")
                    lines.append("╚" + "═"*68 + "╝")
                else:
                    active = [u for u in stats.get("rankings", []) if "ONLINE" in u.get("status", "")][:3]
                    lines.append("╔" + "═"*68 + "╗\n║ " + f"{'CUBYZ ACTIVE WORKER NODES':^66}" + " ║\n╟" + "─"*68 + "╢\n║ Subnet Channel Tracking Active".ljust(69) + "║\n╟" + "─"*68 + "╢\n" + f"║ {'User ID':<25} │ {'Current Activity Status':<38} ║\n╟" + "─"*68 + "╢")
                    for user in active:
                        lines.append(f"║ {user['user_id']:<25} │ {user.get('status', 'ONLINE'):<38} ║")
                    for _ in range(3 - len(active)):
                        lines.append(f"║ {'-':<25} │ {'OFFLINE':<38} ║")
                    lines.append("╚" + "═"*68 + "╝")
                redraw(lines)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def setup_sigint_handler():
    def sigint_wrapper(signum, frame):
        raise KeyboardInterrupt
    signal.signal(signal.SIGINT, sigint_wrapper)

def print_dashboard(activity, file_info, my_chunks, my_lines, global_comp, global_tot, global_pct, is_first=False):
    global CURRENT_DASHBOARD_STATE
    CURRENT_DASHBOARD_STATE = (activity, file_info, my_chunks, my_lines, global_comp, global_tot, global_pct)
    bar = '█' * int(round(20 * global_pct / 100)) + '░' * (20 - int(round(20 * global_pct / 100)))
    if len(file_info) > 52:
        file_info = "..." + file_info[-49:]

    # Using 9F relative jumping entirely prevents terminal scrollback duplication bugs
    if not is_first:
        sys.stdout.write("\033[9F\033[J")

    sys.stdout.write(
        "╔" + "═"*70 + "╗\n"
        f"║ ⚡ CURRENT JOB : {activity:<51} ║\n"
        f"║ 📂 SOURCE FILE : {file_info:<51} ║\n"
        "╟" + "─"*70 + "╢\n"
        f"║ 📊 NODE CONTRIB: {f'{my_chunks} Chunks Complete ({my_lines} lines)':<51} ║\n"
        f"║ 🌍 DATASET PROGRESS: {global_comp}/{global_tot} [{bar}] {global_pct:.2f}%".ljust(71) + "║\n"
        "╚" + "═"*70 + "╝\n"
        "\n 💡 Note: Press Ctrl+C at any time to pause or fetch the distributed leaderboard.\n"
    )
    sys.stdout.flush()

def main():
    global SESSION_CHUNKS_COMPLETED, SESSION_LINES_CRUNCHED
    setup_sigint_handler()
    user_config_file = ".cubyz_user"
    user_id = ""

    if os.path.exists(user_config_file):
        try:
            with open(user_config_file, "r", encoding="utf-8") as f:
                user_id = f.read().strip()
        except Exception:
            pass

    if not user_id:
        while True:
            user_id = input("Enter your volunteer ID (3-9 letters only): ").strip().lower()
            if user_id.isalpha() and (3 <= len(user_id) <= 9):
                try:
                    with open(user_config_file, "w", encoding="utf-8") as f:
                        f.write(user_id)
                except Exception:
                    pass
                break

    # Force a complete terminal reset here to clear input prompts before the UI starts
    sys.stdout.write("\033[H\033[2J\033[3J")
    sys.stdout.flush()

    SESSION_CHUNKS_COMPLETED, SESSION_LINES_CRUNCHED = fetch_user_all_time_stats(user_id)
    old_print = print
    globals()['print'] = lambda *args, **kwargs: None

    try:
        chosen_model, gpu_type, total_vram_gb = get_vram_and_choose_model()
        cooldown, max_threads = (4.0, 2) if total_vram_gb < 6.0 else ((1.5, 4) if total_vram_gb < 11.0 else (0.0, None))
        globals()['print'] = old_print
    except Exception as e:
        globals()['print'] = old_print
        raise e

    # ... (rest of your existing function)

    SESSION_CHUNKS_COMPLETED, SESSION_LINES_CRUNCHED = fetch_user_all_time_stats(user_id)
    old_print = print
    globals()['print'] = lambda *args, **kwargs: None

    try:
        chosen_model, gpu_type, total_vram_gb = get_vram_and_choose_model()
        cooldown, max_threads = (4.0, 2) if total_vram_gb < 6.0 else ((1.5, 4) if total_vram_gb < 11.0 else (0.0, None))
        globals()['print'] = old_print
    except Exception as e:
        globals()['print'] = old_print
        raise e

    ensure_ollama_installed(gpu_type)

    try:
        urllib.request.urlopen("http://localhost:11434", timeout=3)
    except Exception:
        if check_bare_metal_ollama():
            subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif check_docker_ollama():
            fix_docker_permissions()
            subprocess.run(["docker", "start", "ollama"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(3)

    is_docker = check_docker_ollama()
    pull_cmd = ["docker", "exec", "ollama", "ollama", "pull", chosen_model] if is_docker else ["ollama", "pull", chosen_model]
    try:
        subprocess.run(pull_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except Exception:
        sys.exit(f"[X] Model connection alignment failed for '{chosen_model}'.")

    active_prompt = BASE_SYSTEM_PROMPT + (LOW_VRAM_REASONING_RULE if chosen_model in ["qwen3:4b", "qwen3:1.5b"] else "")

    hw_modes = {
        "nvidia": ("Dedicated GPU", "NVIDIA CUDA Platform"),
        "amd": ("Dedicated GPU", "AMD ROCm Runtime Accelerator"),
        "amd_integrated": ("iGPU / APU Unified", "AMD ROCm Runtime (Unified)"),
        "intel": ("Dedicated GPU", "Intel OneAPI Runtime"),
        "intel_integrated": ("iGPU Unified", "Intel OneAPI / Level Zero"),
        "cpu": ("CPU Compute Host", "Native Host Threads (Standard)")
    }
    compute_mode, framework = hw_modes.get(gpu_type, ("CPU Compute Host", "Native Host Threads (Standard)"))

    hardware_card = (
        "\n" + "═"*55 + "\n"
        "           TRACKED HARDWARE CONFIGURATION     \n"
        "═"*55 + "\n"
        f" 🧠 COMPUTE TYPE   : {compute_mode}\n"
        f" ⚙  ACCELERATOR    : {framework}\n"
        f" 💾 DETECTED VRAM  : {total_vram_gb:.1f} GB\n"
        f" 🤖 ACTIVE ENGINE  : {chosen_model}\n"
        f" 🎯 ENGINE STRATEGY: PRIORITIZING HARD\n"
        "═"*55 + "\n\n"
    )

    sys.stdout.write(hardware_card)
    sys.stdout.flush()
    time.sleep(1.5)

    # Tracks if this is the very first time the dashboard renders below the hardware block
    first_stat_print = True

    while True:
        try:
            work_package = make_request(f"{SERVER_URL}/get_work?user_id={user_id}&hardware_tier=hard")
            total_chunks = work_package.get("total_chunks", 0)
            completed_chunks = work_package.get("completed_chunks", 0)
            global_percentage = (completed_chunks / total_chunks * 100) if total_chunks > 0 else 0.0

            if work_package.get("status") == "done":
                print("\n[★] Codebase complete!")
                break
            elif work_package.get("status") == "waiting":
                print_dashboard("IDLE (Waiting for assignments...)", "N/A", SESSION_CHUNKS_COMPLETED, SESSION_LINES_CRUNCHED, completed_chunks, total_chunks, global_percentage, is_first=first_stat_print)
                first_stat_print = False
                time.sleep(15)
                continue

            task = work_package["task"]
            chunk_content = task.get('raw_content', '')
            chunk_lines = len(chunk_content.splitlines())
            file_desc = f"[{task.get('difficulty', 'medium').upper()}] {task['relative_path']} (Chunk {task['chunk_index']})"

            print_dashboard("Generating local context analysis...", file_desc, SESSION_CHUNKS_COMPLETED, SESSION_LINES_CRUNCHED, completed_chunks, total_chunks, global_percentage, is_first=first_stat_print)
            first_stat_print = False

            is_zon = task['file_name'].lower().endswith(('.zon', 'zig.zon'))
            type_instruction = ""
            if is_zon:
                type_instruction = "\n--- DYNAMIC INSTRUCTION FOR .ZON ---\nThis is a pure ZON file. If 'code_example' is output, it MUST be the raw ZON block.\n"
            elif chunk_lines < 50:
                type_instruction = "\n--- DYNAMIC INSTRUCTION FOR SMALL CHUNK ---\nKeep summary and explanations under 2 short sentences.\n"

            prompt_text = f"File: {task['file_name']}\nPath: {task['relative_path']}\nContext: {task['directory_context']}\nChunk: {task['chunk_index']}\n{type_instruction}\nRaw:\n```\n{chunk_content}\n```\n"
            gen_options = {"temperature": 0.15 if task['file_name'].lower().endswith(('.md', '.txt')) else 0.02}
            if max_threads:
                gen_options["num_thread"] = max_threads

            res = make_request(OLLAMA_URL, {
                "model": chosen_model,
                "prompt": prompt_text,
                "system": active_prompt,
                "stream": False,
                "format": RAG_JSON_SCHEMA,
                "options": gen_options
            })

            try:
                parsed_data = json.loads(res.get("response", "").strip())
            except Exception as je:
                parsed_data = {
                    "summary": "Parsing failed.",
                    "comprehensive_explanation": f"Failed logic schema. Error: {je}",
                    "code_example": None,
                    "synthetic_queries": ["Error parsing secure content."]
                }

            parsed_data.update({
                "chunk_id": task["chunk_id"],
                "title": f"[{task['relative_path']}] - Chunk {task['chunk_index']}",
                "user_id": user_id,
                "lines_crunched": chunk_lines
            })

            print_dashboard("Submitting compiled payload to coordinator...", file_desc, SESSION_CHUNKS_COMPLETED, SESSION_LINES_CRUNCHED, completed_chunks, total_chunks, global_percentage, is_first=first_stat_print)
            make_request(f"{SERVER_URL}/submit_work", parsed_data)

            SESSION_CHUNKS_COMPLETED += 1
            SESSION_LINES_CRUNCHED += chunk_lines
            completed_chunks += 1
            global_percentage = (completed_chunks / total_chunks * 100) if total_chunks > 0 else 0.0

            print_dashboard("✓ System Sync Complete!", file_desc, SESSION_CHUNKS_COMPLETED, SESSION_LINES_CRUNCHED, completed_chunks, total_chunks, global_percentage, is_first=first_stat_print)

            if cooldown > 0:
                time.sleep(cooldown)

        except KeyboardInterrupt:
            handle_interrupt_menu()
        except urllib.error.HTTPError as he:
            if he.code == 403:
                sys.exit(f"\n[X] Connection Rejected: Username '{user_id}' is taken.")
            time.sleep(15)
        except (urllib.error.URLError, Exception):
            time.sleep(15)

if __name__ == "__main__":
    main()
