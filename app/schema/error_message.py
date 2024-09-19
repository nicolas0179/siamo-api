"""This module contains the data models for error messages."""

from pydantic import BaseModel


class ErrorMessage(BaseModel):
    """Represents an error message."""

    message: str
