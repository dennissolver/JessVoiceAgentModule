import os
from pathlib import Path
from dotenv import set_key

def prompt_env_var(key, description, default=None, optional=False):
    value = input(f"{description}{' [' + default + ']' if default else ''}: ").strip()
    if not value and default is not None:
        return default
    if not value and optional:
        return ""
    while not value:
        print("This field is required.")
        value = input(f"{description}: ").strip()
    return value

def write_env_file(env_path, values):
    print(f"✅ Writing to {env_path}")
    with open(env_path, 'w') as f:
        for key, val in values.items():
            f.write(f"{key}={val}\n")

def main():
    print("🛠️  Jess Voice Agent Setup Wizard")
    print("----------------------------------")

    elevenlabs_key = prompt_env_var("ELEVENLABS_API_KEY", "Enter your ElevenLabs API Key")
    groq_key = prompt_env_var("GROQ_API_KEY", "Enter your Groq API Key")
    openai_key = prompt_env_var("OPENAI_API_KEY", "Enter your OpenAI API Key", optional=True)
    claude_key = prompt_env_var("ANTHROPIC_API_KEY", "Enter your Anthropic (Claude) API Key", optional=True)

    primary_llm = prompt_env_var("PRIMARY_LLM_PROVIDER", "Choose primary LLM provider [groq, openai, claude]", default="groq")
    fallback_llm = prompt_env_var("LLM_FALLBACK", "Choose fallback LLM provider [openai, claude, groq]", optional=True)
    jess_mode = prompt_env_var("JESS_MODE", "What mode is this agent in? (e.g., discovery, support)", default="discovery")
    voice_name = prompt_env_var("JESS_VOICE", "What is the ElevenLabs voice preset to use?", default="jess")

    agent_id = prompt_env_var("NEXT_PUBLIC_AGENT_ID", "What is your ElevenLabs Agent ID for frontend?")
    project_name = prompt_env_var("NEXT_PUBLIC_PROJECT_NAME", "What is the project name for this deployment?", default="JessVoiceAgent")

    backend_env = {
        "ELEVENLABS_API_KEY": elevenlabs_key,
        "GROQ_API_KEY": groq_key,
        "OPENAI_API_KEY": openai_key,
        "ANTHROPIC_API_KEY": claude_key,
        "PRIMARY_LLM_PROVIDER": primary_llm,
        "LLM_FALLBACK": fallback_llm,
        "JESS_MODE": jess_mode,
        "JESS_VOICE": voice_name
    }

    frontend_env = {
        "NEXT_PUBLIC_AGENT_ID": agent_id,
        "NEXT_PUBLIC_PROJECT_NAME": project_name
    }

    write_env_file(".env", backend_env)
    write_env_file(".env.local", frontend_env)

    print("\n🎉 Setup complete. You can now run your backend and frontend services.")

if __name__ == "__main__":
    main()
