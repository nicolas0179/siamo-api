from fastapi import APIRouter

from app.router import tone_identifier_router

router = APIRouter()
router.include_router(tone_identifier_router.router)
