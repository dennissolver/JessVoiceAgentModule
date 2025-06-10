from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from config import settings
from llm_router import query_llm
from tts import speak
from jess_chat.discovery_agent import handle_discovery_prompt
from jess_chat.memory import update_memory

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str
    session_id: str = "default"

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


