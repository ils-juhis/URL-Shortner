from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.core.database_service import get_db
from app.schemas.user_schemas import User, UserCreate, UserUpdate
from app.services.user_service import UserService
from app.core.security import get_current_user
from app.models.user import User as UserModel

router = APIRouter()

@router.post("/users", response_model=User)
def create_user(user: UserCreate, db: AsyncIOMotorDatabase = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    # Add authorization check here
    return UserService(db).create_user(user)

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate, db: AsyncIOMotorDatabase = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    # Add authorization check here
    return UserService(db).update_user(user_id, user)