# FlowMind AI — Dashboard

React + Vite dashboard for the FlowMind AI backend.

## Setup

```bash
cd frontend
npm install
cp .env.example .env
# edit .env if your backend isn't at http://localhost:8000
npm run dev
```

Then open the URL Vite prints (usually http://localhost:5173).

Make sure the backend is running first (`uvicorn backend.main:app` from
the project root) — the dashboard talks to it directly over HTTP.

## Pages

| Page | Talks to |
|---|---|
| Chat | `POST /api/chat` |
| Files & Editor | `GET/POST /api/files/*` (confined to the project directory) |
| Browser | routed through chat — the Browser tool itself is still a placeholder in the backend |
| GitHub | `GET /api/github/summary` |
| Image | `POST /api/images/generate` |
| Video | `POST /api/video/generate` |
| Voice | `POST /api/voice/speak` |
| Testing | `POST /api/testing/run` |
| Deployment | `POST /api/deployment/run` |
| Logs | `GET /api/logs/recent` |

## Build for production

```bash
npm run build
```

Output goes to `frontend/dist/` — serve it with any static file host, or
point Nginx/Caddy at it alongside the backend.
