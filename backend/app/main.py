from fastapi import FastAPI
from app.core.database_service import database_service
from app.api.v1.auth import auth_controller
from app.api.v1.admin import role_controller
from app.api.v1.urls import url_controller
from app.api.v1.admin import user_controller
from app.api.v1.users import session_controller

app = FastAPI()

app.include_router(auth_controller.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(role_controller.router, prefix="/api/v1/admin", tags=["admin"])
app.include_router(user_controller.router, prefix="/api/v1/admin", tags=["admin"])
app.include_router(url_controller.router, prefix="/api/v1", tags=["urls"])
app.include_router(session_controller.router, prefix="/api/v1/users", tags=["users"])

@app.on_event("startup")
async def startup_event():
    await database_service.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await database_service.disconnect()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
