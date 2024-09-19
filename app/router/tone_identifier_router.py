from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.infrastructure.services.tokenizer_service import TokenizerService
from app.schema.error_message import ErrorMessage
from app.schema.tone_identifier_response import ToneIdentifierResponse
from app.application.tone_identifier_service import ToneIdentifierService

router = APIRouter()


# Dependency injection
tokenizer_service = TokenizerService()
tone_identifier_service = ToneIdentifierService(tokenizer_service)


# Schema for the input sentence
class Sentence(BaseModel):
    text: str


@router.post(
    "/toneIdentifier",
    responses={
        200: {"model": ToneIdentifierResponse, "description": "OK."},
        500: {"model": ErrorMessage, "description": "Internal Server Error."},
    },
    tags=["Tone Identifier"],
    summary="Tone Identification for a sentence.",
    description="This endpoint identifies the tone of each syllable for a "
    "given sentence.",
    response_model=ToneIdentifierResponse,
)
async def tone_identifier(sentence: Sentence):
    try:
        return tone_identifier_service.process_sentence(sentence.text)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
