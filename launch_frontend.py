import os
import subprocess
import platform

def run_frontend():
    print("▶️  Installing frontend dependencies...")
    os.chdir("frontend")
    npm_command = "npm.cmd" if platform.system() == "Windows" else "npm"
    subprocess.run([npm_command, "install"], shell=True)
    print("▶️  Starting frontend (Next.js)...")
    subprocess.run([npm_command, "run", "dev"], shell=True)

if __name__ == "__main__":
    run_frontend()

