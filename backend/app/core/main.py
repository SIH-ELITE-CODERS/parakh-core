from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.routers.auth import router as auth_router

app = FastAPI(prefix="/api")
app.include_router(auth_router)
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/api/health",
    summary="Get Server Health",
)
async def getHealth():
    return {"message": "Alive and Kickin!"}
