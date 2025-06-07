# === Stage 1: Build backend ===
FROM python:3.11-slim AS backend-builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend

# === Stage 2: Final image ===
FROM python:3.11-slim

WORKDIR /app

# Copy backend from previous stage
COPY --from=backend-builder /app /app

# Expose the FastAPI backend port
EXPOSE 8000

# Use Railway-injected environment variables
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
