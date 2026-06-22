from motor.motor_asyncio import AsyncIOMotorDatabase

from app.schemas.url_schemas import URL, URLCreate
import string
import random

def generate_short_code(length: int = 6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))

class URLService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db

    def create_url(self, url: URLCreate, user_id: int):
        short_code = generate_short_code()
        db_url = URL(
            target_url=url.target_url,
            custom_alias=url.custom_alias,
            is_active=url.is_active,
            expires_at=url.expires_at,
            user_id=user_id,
            short_url=short_code
        )
        self.db.add(db_url)
        self.db.commit()
        self.db.refresh(db_url)
        return db_url