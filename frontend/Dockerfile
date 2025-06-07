# === Frontend Dockerfile: Jess Voice Agent (Next.js) ===
FROM node:20-alpine AS builder

WORKDIR /app

# Copy package files and install deps
COPY frontend/package*.json ./
RUN npm install

# Copy rest of frontend and build
COPY frontend ./
RUN npm run build

# === Production image ===
FROM node:20-alpine AS runner
WORKDIR /app

ENV NODE_ENV production
ENV PORT 3000

# Copy only built assets
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

EXPOSE 3000

CMD ["npm", "start"]
