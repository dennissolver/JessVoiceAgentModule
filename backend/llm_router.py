from config import settings
from groq_client import call_groq
from openai_client import call_openai
from claude_client import call_claude

def query_llm(prompt: str, provider: str = None) -> str:
    provider = provider or settings.PRIMARY_LLM_PROVIDER.lower()

    try:
        if provider == "groq":
            return call_groq(prompt)
        elif provider == "openai":
            return call_openai(prompt)
        elif provider == "claude":
            return call_claude(prompt)
        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")
    except Exception as e:
        print(f"[LLM ERROR] {e}")
        fallback = settings.LLM_FALLBACK
        if fallback and fallback != provider:
            print(f"🔁 Falling back to {fallback}")
            return query_llm(prompt, provider=fallback)
        raise e
