# === Stage 1: Build stage with dependencies installed ===
FROM python:3.11-slim AS backend-builder

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend

# === Stage 2: Runtime image ===
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Confirm uvicorn is correctly installed (debug step)
RUN which uvicorn && uvicorn --version

# Copy built app from previous stage
COPY --from=backend-builder /app /app

EXPOSE 8000

# ✅ Use uvicorn to launch FastAPI app
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
