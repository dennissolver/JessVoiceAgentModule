# Agent Guidelines

This repository contains a FastAPI backend and a Next.js frontend.

## Testing
- After making changes you must run the following commands:
  - `python -m py_compile $(git ls-files '*.py')`
  - `npm run --prefix frontend build`

If any command fails you must mention it in the PR `Testing` section.

## Code Style
- Use 4 spaces for indentation in Python.
- Use TypeScript for all frontend pages under `frontend/app`.
- Keep documentation up to date when adding or removing features.
