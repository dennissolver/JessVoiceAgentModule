import os
import subprocess
import sys
import time
import webbrowser

def run_setup():
    if (
        sys.stdin.isatty()
        and (not os.path.exists(".env") or not os.path.exists(".env.local"))
    ):
        print("🛠️  Running setup_env.py...")
        subprocess.run([sys.executable, "setup_env.py"])
    elif not os.path.exists(".env"):
        print(
            "⚠️  Configuration missing. Start the services and visit /setup to provide API keys."
        )

def run_backend():
    print("▶️  Starting backend (FastAPI)...")
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.abspath(".")
    return subprocess.Popen([sys.executable, "launch_backend.py"], env=env)

def run_frontend():
    print("▶️  Installing frontend dependencies...")
    os.chdir("frontend")
    subprocess.run("npm install", shell=True)
    print("▶️  Starting frontend (Next.js)...")
    return subprocess.Popen("npm run dev", shell=True)

if __name__ == "__main__":
    print("🚀 Launching Jess Voice Agent System")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    run_setup()
    backend_process = run_backend()

    time.sleep(3)
    frontend_process = run_frontend()

    time.sleep(5)
    print("🌐 Opening browser to http://localhost:3000")
    webbrowser.open("http://localhost:3000")

    try:
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
        backend_process.terminate()
        frontend_process.terminate()
