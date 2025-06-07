# Jess Voice Chat Module

This is a Railway-ready voice agent system using FastAPI, Next.js, and ElevenLabs TTS.

## Setup

1. Clone or unzip the project.
2. Run the environment setup wizard:
   ```bash
   python setup_env.py
   ```
3. Start the backend:
   ```bash
   uvicorn backend.main:app --reload
   ```
4. Start the frontend:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Features

- ElevenLabs Text-to-Speech
- Browser Speech Recognition
- Groq, OpenAI, Claude LLM integration
- Configurable via `.env` and `.env.local`
- Embeddable widget in `public/jess-agent.js`

## Deployment

You can deploy the app to Railway using `railway.json`.

## License

MIT
