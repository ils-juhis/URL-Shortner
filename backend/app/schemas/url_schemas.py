from pydantic import BaseModel, ConfigDict, HttpUrl
from typing import Optional
from datetime import datetime

class URLBase(BaseModel):
    target_url: HttpUrl
    custom_alias: Optional[str] = None
    is_active: bool = True
    expires_at: Optional[datetime] = None

class URLCreate(URLBase):
    pass

class URL(URLBase):
    id: int
    short_url: str
    clicks: int = 0
    created_at: datetime
    updated_at: datetime

    class Config:
            model_config = ConfigDict(
        from_attributes=True
    )