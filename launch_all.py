import os
import subprocess
import sys
from pathlib import Path

def run_setup():
    if sys.stdin.isatty() and (not Path(".env").exists() or not Path(".env.local").exists()):
        print("🛠️  Running setup_env.py...")
        subprocess.run([sys.executable, "setup_env.py"])
    elif not Path(".env").exists():
        print("⚠️  Configuration missing. Start the services and visit /setup to provide API keys.")

def run_backend():
    backend_env = os.environ.copy()
    backend_env["PYTHONPATH"] = os.path.abspath(".")
    print("▶️  Starting backend (FastAPI)...")
    return subprocess.Popen([sys.executable, "launch_backend.py"], env=backend_env)

def run_frontend():
    print("▶️  Starting frontend (Next.js)...")
    return subprocess.Popen([sys.executable, "launch_frontend.py"])

if __name__ == "__main__":
    print("🚀 Launching Jess Voice Agent backend and frontend...")
    run_setup()
    backend_process = run_backend()
    frontend_process = run_frontend()

    try:
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
        backend_process.terminate()
        frontend_process.terminate()
