from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.infrastructure.services.tts_service import TTSService
from app.schema.error_message import ErrorMessage
from app.schema.tts_response import TTSResponse
from app.application.text_to_speech_service import TextToSpeechService

router = APIRouter()


# Dependency injection
tts_service = TTSService()
text_to_speech_service = TextToSpeechService(tts_service)


# Schema for the input sentence
class Sentence(BaseModel):
    text: str


@router.post(
    "/tts",
    responses={
        200: {"model": TTSResponse, "description": "OK."},
        500: {"model": ErrorMessage, "description": "Internal Server Error."},
    },
    tags=["TTS"],
    summary="Text to Speech.",
    description="This endpoint converts a given sentence into a speech "
    "audio file.",
    response_model=TTSResponse,
)
async def text_to_speech(sentence: Sentence):
    try:
        return text_to_speech_service.process_sentence(sentence.text)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
