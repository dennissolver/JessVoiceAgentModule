import zipfile
import os

def zip_project(output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk("."):
            if any(x in root for x in [".git", ".venv", "__pycache__"]):
                continue
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, ".")
                zipf.write(filepath, arcname)

zip_project("JessVoiceChatModule.zip")
