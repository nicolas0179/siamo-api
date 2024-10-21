"""This module defines the response structure for a tone identifier
API endpoint."""

from pydantic import BaseModel


class ToneResponse(BaseModel):
    """Represents the response structure for a tone."""

    name: str
    symbol: str


class SyllableResponse(BaseModel):
    """Represents the response structure for a syllable."""

    syllable: str
    romanization: str
    tone: ToneResponse


class ToneIdentifierResponse(BaseModel):
    """Represents the response structure for a tone identifier API endpoint."""

    syllables: list[SyllableResponse]
