# Multi-stage Dockerfile: Build frontend, serve backend
FROM node:18 AS frontend-builder
WORKDIR /app
COPY frontend ./frontend
RUN cd frontend && npm install && npm run build

FROM python:3.12-slim AS backend
WORKDIR /app

# Install backend dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend and built frontend
COPY backend ./backend
COPY setup_env.py .
COPY launch_backend.py .
COPY launch_frontend.py .
COPY launch.py .
COPY railway.json .
COPY .env .
COPY .env.local .
COPY --from=frontend-builder /app/frontend/out ./frontend_build

EXPOSE 8000
CMD ["python", "launch.py"]
