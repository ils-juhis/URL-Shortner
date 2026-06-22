from motor.motor_asyncio import AsyncIOMotorDatabase

from app.models.user_session import UserSession
from fastapi import HTTPException

class SessionService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db

    def get_sessions(self, user_id: int):
        return self.db.query(UserSession).filter(UserSession.user_id == user_id).all()

    def revoke_session(self, session_id: int, user_id: int):
        session = self.db.query(UserSession).filter(UserSession.id == session_id).first()
        if not session or session.user_id != user_id:
            raise HTTPException(status_code=404, detail="Session not found")
        self.db.delete(session)
        self.db.commit()