from pydantic import BaseModel, Field
from datetime import datetime, timedelta

class PasswordReset(BaseModel):
    email: str
    otp: str
    expires_at: datetime = Field(default_factory=lambda: datetime.utcnow() + timedelta(minutes=15))
