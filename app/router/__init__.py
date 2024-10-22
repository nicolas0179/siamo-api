from fastapi import APIRouter

from app.router import tone_identifier_router
from app.router import text_to_speech_router

router = APIRouter()
router.include_router(tone_identifier_router.router)
router.include_router(text_to_speech_router.router)
