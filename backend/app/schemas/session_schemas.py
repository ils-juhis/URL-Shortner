from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UserSessionBase(BaseModel):
    user_agent: str
    ip_address: str

class UserSessionCreate(UserSessionBase):
    pass

class UserSession(UserSessionBase):
    id: int
    created_at: datetime
    last_seen_at: datetime

    class Config:
            model_config = ConfigDict(
        from_attributes=True
    )