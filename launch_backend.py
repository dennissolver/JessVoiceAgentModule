import os
import uvicorn

if __name__ == "__main__":
    # Ensure PYTHONPATH is set to the root of the project
    os.environ["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))

    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
