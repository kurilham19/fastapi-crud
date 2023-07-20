from fastapi import APIRouter
from src.routes.userRouter import router as userRouter

router = APIRouter()

router.include_router(userRouter, prefix="/users")