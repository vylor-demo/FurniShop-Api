from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.features.chairs.routers.chair_router import chairs_router

app = FastAPI(title="FurniShop Demo API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chairs_router, prefix="/api/v1/chairs", tags=["chairs"])


@app.get("/")
def read_root():
    return {"status": "online", "message": "Welcome to Furnishop API"}
