from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from datetime import datetime, timedelta
from jose import jwt
from fastapi_mail import MessageSchema
from app.core.security import (
    get_password_hash,
    verify_password,
    create_access_token,
    create_refresh_token,
)
from app.schemas.auth_schemas import UserCreate
from app.models.password_reset import PasswordReset
from app.core.config import settings
import random
from app.utils.email_handler import send_email
from app.utils.template_renderer import render_template

class AuthService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db

    async def get_user_by_email(self, email: str):
        return await self.db.users.find_one({"email": email})

    async def register_user(self, user: UserCreate):
        hashed_password = get_password_hash(user.password)
        user_doc = {
            "name": user.name,
            "email": user.email,
            "hashed_password": hashed_password,
            "is_active": True,
            "is_verified": False,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
        }
        result = await self.db.users.insert_one(user_doc)
        await self.send_verification_email(user.email)

    def create_email_verification_token(self, email: str):
        expire = datetime.utcnow() + timedelta(
            hours=settings.EMAIL_VERIFICATION_EXPIRE_HOURS
        )
        to_encode = {
            "exp": expire,
            "sub": email,
            "token_type": "email_verification",
        }
        encoded_jwt = jwt.encode(
            to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
        )
        return encoded_jwt

    async def send_verification_email(self, email: str):
        token = self.create_email_verification_token(email)
        verification_url = (
            f"{settings.FRONTEND_URL}/verify-email?token={token}"
        )
        html = render_template(
          "verification_email_template.html",
          verification_url=verification_url,
          expire_hours=settings.EMAIL_VERIFICATION_EXPIRE_HOURS,
        )

        await send_email(
            subject="Email Verification",
            recipients=email,
            html_content=html,
        )

    async def verify_email(self, token: str):
        try:
            payload = jwt.decode(
                token,
                settings.JWT_SECRET_KEY,
                algorithms=[settings.JWT_ALGORITHM],
            )
            if payload.get("token_type") != "email_verification":
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid token type",
                )
            email = payload.get("sub")
            if email is None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid token",
                )
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Token has expired",
            )
        except jwt.JWTError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid token",
            )

        user = await self.get_user_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
        if user["is_verified"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Account already verified",
            )

        await self.db.users.update_one(
            {"email": email},
            {
                "$set": {
                    "is_verified": True,
                    "verified_at": datetime.utcnow(),
                }
            },
        )

    async def resend_verification_email(self, email: str):
        user = await self.get_user_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
        if user["is_verified"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Account already verified",
            )
        await self.send_verification_email(email)

    async def forgot_password(self, email: str):
        existing_user = await self.get_user_by_email(email)
        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found")

        otp = "".join([str(random.randint(0, 9)) for _ in range(6)])
        password_reset_doc = PasswordReset(email=email, otp=otp)
        await self.db.password_resets.insert_one(password_reset_doc.dict())

        # TODO: Implement actual email sending
        print(f"OTP for {email}: {otp}")

        return {"message": "OTP sent to your email"}

    async def login_user(self, email: str, password: str):
        db_user = await self.get_user_by_email(email)
        if not db_user:
            raise HTTPException(
                status_code=401, detail="Incorrect email or password"
            )
        if not verify_password(password, db_user["hashed_password"]):
            raise HTTPException(
                status_code=401, detail="Incorrect email or password"
            )
        access_token = create_access_token(data={"sub": db_user["email"]})
        refresh_token = create_refresh_token(data={"sub": db_user["email"]})
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }

    async def refresh_user_token(self, email: str):
        access_token = create_access_token(data={"sub": email})
        refresh_token = create_refresh_token(data={"sub": email})
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }