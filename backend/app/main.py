from fastapi import FastAPI
from app.core.database_service import database_service

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await database_service.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await database_service.disconnect()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
