from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.features.bedrooms.routers.bedroom_router import bedrooms_router
from app.features.chairs.routers.chair_router import router as chairs_router
from app.features.desks.routers.desk_router import router as desks_router
from app.features.living_rooms.routers.living_room_router import living_rooms_router

app = FastAPI(title="FurniShop Demo API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chairs_router, prefix="/api/v1/chairs", tags=["chairs"])
app.include_router(desks_router, prefix="/api/v1/desks", tags=["desks"])
app.include_router(
    living_rooms_router,
    prefix="/api/v1/living-rooms",
    tags=["living-rooms"],
)
app.include_router(bedrooms_router, prefix="/api/v1/bedrooms", tags=["bedrooms"])


@app.get("/")
def read_root():
    return {"status": "online", "message": "Welcome to Furnishop API"}
