from fastapi import APIRouter, Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.core.database_service import get_db
from app.schemas.auth_schemas import (
    UserCreate,
    UserLogin,
    Token,
    TokenData,
    ForgotPasswordRequest,
    ResendVerificationEmailRequest,
)
from app.schemas.user_schemas import User
from app.services.auth_service import AuthService
from app.core.security import get_current_user

router = APIRouter()


@router.post("/register")
async def register(user: UserCreate, db: AsyncIOMotorDatabase = Depends(get_db)):
    auth_service = AuthService(db)
    db_user = await auth_service.get_user_by_email(user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )
    await auth_service.register_user(user)
    return {"message": "Registration successful. Please verify your email."}


@router.get("/verify-email")
async def verify_email(token: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    auth_service = AuthService(db)
    await auth_service.verify_email(token)
    return {"message": "Email verified successfully"}


@router.post("/resend-verification")
async def resend_verification_email(
    request: ResendVerificationEmailRequest, db: AsyncIOMotorDatabase = Depends(get_db)
):
    auth_service = AuthService(db)
    await auth_service.resend_verification_email(request.email)
    return {"message": "Verification email sent."}


@router.post("/login", response_model=Token)
async def login(form_data: UserLogin, db: AsyncIOMotorDatabase = Depends(get_db)):
    return await AuthService(db).login_user(form_data.email, form_data.password)


@router.post("/forgot-password")
async def forgot_password(
    request: ForgotPasswordRequest, db: AsyncIOMotorDatabase = Depends(get_db)
):
    return await AuthService(db).forgot_password(request.email)


@router.post("/refresh", response_model=Token)
async def refresh_token(current_user: User = Depends(get_current_user)):
    return await AuthService().refresh_token(current_user)


@router.post("/logout")
async def logout(
    current_user: User = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    # Implement single-device logout logic here
    return {"message": "Logged out successfully"}


@router.post("/logout-all")
async def logout_all(
    current_user: User = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    # Implement all-devices logout logic here
    return {"message": "Logged out from all devices successfully"}