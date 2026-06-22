from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.core.database_service import get_db
from app.schemas.session_schemas import UserSession
from app.services.session_service import SessionService
from app.core.security import get_current_user
from app.models.user import User
from typing import List

router = APIRouter()

@router.get("/sessions", response_model=List[UserSession])
def get_sessions(db: AsyncIOMotorDatabase = Depends(get_db), current_user: User = Depends(get_current_user)):
    return SessionService(db).get_sessions(user_id=current_user.id)

@router.delete("/sessions/{session_id}")
def revoke_session(session_id: int, db: AsyncIOMotorDatabase = Depends(get_db), current_user: User = Depends(get_current_user)):
    SessionService(db).revoke_session(session_id=session_id, user_id=current_user.id)
    return {"message": "Session revoked successfully"}