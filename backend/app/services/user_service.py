from motor.motor_asyncio import AsyncIOMotorDatabase

from app.models.user import User
from app.schemas.user_schemas import UserCreate, UserUpdate
from app.core.security import get_password_hash

class UserService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db

    def create_user(self, user: UserCreate):
        hashed_password = get_password_hash(user.password)
        db_user = User(
            email=user.email,
            hashed_password=hashed_password,
            is_active=user.is_active,
            is_superuser=user.is_superuser
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update_user(self, user_id: int, user: UserUpdate):
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if user.email:
            db_user.email = user.email
        if user.is_active is not None:
            db_user.is_active = user.is_active
        if user.is_superuser is not None:
            db_user.is_superuser = user.is_superuser
        self.db.commit()
        self.db.refresh(db_user)
        return db_user