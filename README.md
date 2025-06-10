# Jess Voice Chat Module

Jess Voice Agent is a FastAPI + Next.js project using ElevenLabs TTS. It can run locally or on Render.

## Setup

1. Clone or unzip the project.
2. (Optional) Run the console setup wizard:
   ```bash
   python setup_env.py
   ```
When deploying to Render or another host without a terminal, start the services and visit `/setup` in the browser to provide your API keys.
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

The repository contains a `render.yaml` configuration for one-click deployment to Render.

## License

MIT
