from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.core.database_service import get_db
from app.schemas.role_schemas import Role, RoleCreate
from app.services.role_service import RoleService

router = APIRouter()

@router.post("/roles", response_model=Role)
def create_role(role: RoleCreate, db: AsyncIOMotorDatabase = Depends(get_db)):
    return RoleService(db).create_role(role)