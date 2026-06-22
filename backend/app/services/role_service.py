from motor.motor_asyncio import AsyncIOMotorDatabase

from app.models.role import Role
from app.models.permission import Permission
from app.schemas.role_schemas import RoleCreate

class RoleService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db

    def create_role(self, role: RoleCreate):
        db_role = Role(name=role.name, description=role.description)
        self.db.add(db_role)
        self.db.commit()
        self.db.refresh(db_role)
        return db_role