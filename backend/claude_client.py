import requests
from backend.config import settings

def call_claude(prompt: str) -> str:
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": settings.ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    data = {
        "model": "claude-3-sonnet-20240229",
        "max_tokens": 1000,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.ok:
        return response.json()["content"][0]["text"]
    else:
        raise Exception(f"Claude error: {response.text}")
