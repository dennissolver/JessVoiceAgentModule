import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env

class Settings:
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    PRIMARY_LLM_PROVIDER = os.getenv("PRIMARY_LLM_PROVIDER", "groq")
    LLM_FALLBACK = os.getenv("LLM_FALLBACK", "openai")
    JESS_MODE = os.getenv("JESS_MODE", "discovery")
    JESS_VOICE = os.getenv("JESS_VOICE", "jess")

settings = Settings()
