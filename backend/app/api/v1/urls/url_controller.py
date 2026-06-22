from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.core.database_service import get_db
from app.schemas.url_schemas import URL, URLCreate
from app.services.url_service import URLService
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/urls", response_model=URL)
def create_url(url: URLCreate, db: AsyncIOMotorDatabase = Depends(get_db), current_user: User = Depends(get_current_user)):
    return URLService(db).create_url(url, user_id=current_user.id)