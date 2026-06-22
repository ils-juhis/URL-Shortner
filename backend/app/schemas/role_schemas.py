from pydantic import BaseModel, ConfigDict
from typing import List

class PermissionBase(BaseModel):
    name: str
    description: str

class PermissionCreate(PermissionBase):
    pass

class Permission(PermissionBase):
    id: int

    class Config:
            model_config = ConfigDict(
        from_attributes=True
    )

class RoleBase(BaseModel):
    name: str
    description: str

class RoleCreate(RoleBase):
    permissions: List[int] = []

class Role(RoleBase):
    id: int
    permissions: List[Permission] = []

    class Config:
            model_config = ConfigDict(
        from_attributes=True
    )