from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FlowMind AI",
    description="Next Generation AI Operating System",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production mein specific domains use karenge
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "app": "FlowMind AI",
        "status": "Running",
        "version": "1.0.0",
        "message": "Welcome to FlowMind AI 🚀"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }