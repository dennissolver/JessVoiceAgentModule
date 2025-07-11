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
5. Build the frontend for production:

   If packages are missing, run `npm install` in `frontend/` before building.
   ```bash
   cd frontend
   npm install
   npm run build
   ```

## Authentication

The backend uses **FastAPI Users** with bearer-token authentication. Log in at
`/login` and store the returned `access_token`. Include
`Authorization: Bearer <token>` when calling protected endpoints such as
`/api/save-config`. If the backend responds with `401 Unauthorized`, the
frontend clears the saved token and redirects to `/login`.
The backend logs a warning when this endpoint is called without an
`Authorization` header to help debug login issues.

The default admin credentials are:

```
Email: admin@example.com
Password: admin
```


## Features

- ElevenLabs Text-to-Speech
- Browser Speech Recognition
- Groq, OpenAI, Claude LLM integration
- Configurable via `.env` and `.env.local`
- Embeddable widget in `public/jess-agent.js`

## Environment Variables

The frontend reads the following variable from `.env.local` or your deployment environment:

`NEXT_PUBLIC_BACKEND_URL` - Base URL of the FastAPI backend used for login and configuration requests. If omitted, the setup page falls back to `http://localhost:8000`.

## Deployment

The repository contains a `render.yaml` configuration for one-click deployment to Render.

### `CORS_ORIGINS`

CORS. When deploying with `render.yaml`, set it to your frontend domain, for example
`https://jessvoiceagentmodule-front-end.onrender.com`. The variable also supports a
comma-separated list of origins, for example:

```
CORS_ORIGINS=https://example.com,https://other.com
```

#### Verify CORS setup

When the backend starts it logs the configured origins. Look for a line like
`CORS origins: [...]` in the startup output to confirm that `CORS_ORIGINS` was
loaded. You can also check that responses include the header by running:

```bash
curl -I <backend>/api/save-config
```

The output should contain `Access-Control-Allow-Origin`.

## License

MIT
