from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .core.config import settings
from .db.base import Base
from .db.session import engine
from .api.v1 import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting...")
    Base.metadata.create_all(bind=engine)
    yield
    print("Stopping...")
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API for managing online programming courses",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    api_router,
    prefix="/api/v1",
)

@app.get("/", tags=["Root"])
def health_check() -> dict[str, str]:
    return {
        "message": "Welcome to Course Service API",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "running"
    }