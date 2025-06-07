import os
import subprocess

def get_project_name():
    try:
        with open(".env", "r") as f:
            for line in f:
                if line.startswith("PROJECT_NAME="):
                    return line.strip().split("=", 1)[1]
    except:
        pass
    return "JessVoiceAgent"

project_name = get_project_name()
print(f"📦 Initializing Git repository for project: {project_name}")

subprocess.run(["git", "init"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Initial commit"])

use_cli = input("❓ Use GitHub CLI to create repo? (y/n): ").lower() == "y"

if use_cli:
    subprocess.run(["gh", "repo", "create", project_name, "--public", "--source=.", "--remote=origin", "--push"])
else:
    repo_url = input("🔗 Enter GitHub repo URL (e.g. https://github.com/user/repo.git): ").strip()
    subprocess.run(["git", "remote", "add", "origin", repo_url])
    subprocess.run(["git", "branch", "-M", "main"])
    subprocess.run(["git", "push", "-u", "origin", "main"])
