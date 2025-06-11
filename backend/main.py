from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from auth import (
    fastapi_users,
    auth_backend,
    current_active_user,
    UserRead,
    UserCreate,
    UserUpdate,
    create_db_and_admin,
)
from config import settings
from llm_router import query_llm
from tts import speak
from jess_chat.discovery_agent import handle_discovery_prompt
from jess_chat.memory import update_memory
import os

app = FastAPI()


@app.on_event("startup")
async def startup() -> None:
    await create_db_and_admin()

origins_env = os.getenv("CORS_ORIGINS", "*")
origins = [o.strip() for o in origins_env.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

class ChatRequest(BaseModel):
    prompt: str
    session_id: str = "default"

class ConfigPayload(BaseModel):
    ELEVENLABS_API_KEY: str
    ELEVENLABS_VOICE_ID: str
    ELEVENLABS_AGENT_ID: str
    GROQ_API_KEY: str | None = None
    OPENAI_API_KEY: str | None = None
    ANTHROPIC_API_KEY: str | None = None
    PRIMARY_LLM_PROVIDER: str = "groq"
    LLM_FALLBACK: str | None = None
    NEXT_PUBLIC_PROJECT_NAME: str
    NEXT_PUBLIC_BACKEND_URL: str

@app.get("/")
def root():
    return {"message": "Jess Voice Agent is running"}

@app.post("/chat")
def chat(data: ChatRequest):
    print("📩 Received chat prompt:", data.prompt)

    memory_prompt = handle_discovery_prompt(data.prompt)
    print("🧠 Memory-enhanced prompt:", memory_prompt)

    update_memory(data.session_id, memory_prompt)

    response = query_llm(memory_prompt)
    print("🤖 LLM raw response:", response)

    audio_base64 = speak(response)
    print("🔊 Audio base64 (first 50):", audio_base64[:50])

    return {"reply": response, "audio": audio_base64}

def write_env_file(path: str, values: dict):
    with open(path, "w") as f:
        for k, v in values.items():
            f.write(f"{k}={v}\n")


@app.post("/api/save-config")
def save_config(payload: ConfigPayload, user=Depends(current_active_user)):
    backend_keys = {
        "ELEVENLABS_API_KEY": payload.ELEVENLABS_API_KEY,
        "ELEVENLABS_VOICE_ID": payload.ELEVENLABS_VOICE_ID,
        "ELEVENLABS_AGENT_ID": payload.ELEVENLABS_AGENT_ID,
        "GROQ_API_KEY": payload.GROQ_API_KEY or "",
        "OPENAI_API_KEY": payload.OPENAI_API_KEY or "",
        "ANTHROPIC_API_KEY": payload.ANTHROPIC_API_KEY or "",
        "PRIMARY_LLM_PROVIDER": payload.PRIMARY_LLM_PROVIDER,
        "LLM_FALLBACK": payload.LLM_FALLBACK or "",
    }

    frontend_keys = {
        "NEXT_PUBLIC_ELEVENLABS_AGENT_ID": payload.ELEVENLABS_AGENT_ID,
        "NEXT_PUBLIC_PROJECT_NAME": payload.NEXT_PUBLIC_PROJECT_NAME,
        "NEXT_PUBLIC_BACKEND_URL": payload.NEXT_PUBLIC_BACKEND_URL,
        "NEXT_PUBLIC_ELEVENLABS_VOICE_ID": payload.ELEVENLABS_VOICE_ID,
    }

    write_env_file(".env", backend_keys)
    write_env_file(".env.local", frontend_keys)
    return {"status": "saved"}


