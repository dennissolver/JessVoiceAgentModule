import os
import requests
import base64
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")


def speak(text: str) -> str:
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        print(f"[TTS] Error: {response.status_code} - {response.text}")
        return ""

    # Return base64-encoded audio data
    audio = response.content
    return base64.b64encode(audio).decode("utf-8")
