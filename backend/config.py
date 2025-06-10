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
    ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")

settings = Settings()

required = [
    ("ELEVENLABS_API_KEY", settings.ELEVENLABS_API_KEY),
    ("ELEVENLABS_VOICE_ID", settings.ELEVENLABS_VOICE_ID),
]

if not any([settings.GROQ_API_KEY, settings.OPENAI_API_KEY, settings.ANTHROPIC_API_KEY]):
    raise RuntimeError(
        "No LLM API key provided. Set GROQ_API_KEY, OPENAI_API_KEY or ANTHROPIC_API_KEY."
    )

for name, value in required:
    if not value:
        raise RuntimeError(
            f"Missing required configuration: {name}. Run setup_env.py or visit /setup"
        )
