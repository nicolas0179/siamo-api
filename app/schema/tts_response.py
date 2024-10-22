"""This module defines the response structure for a TTS API endpoint."""

from typing import Annotated
import numpy as np
from pydantic import BaseModel, BeforeValidator, ConfigDict, PlainSerializer


def nd_array_custom_before_validator(x):
    return x


def nd_array_custom_serializer(x):
    return str(x)


NdArray = Annotated[
    np.ndarray,
    BeforeValidator(nd_array_custom_before_validator),
    PlainSerializer(nd_array_custom_serializer, return_type=str),
]


class TTSResponse(BaseModel):
    """Represents the response structure for a TTS API endpoint."""

    waveform: NdArray

    model_config = ConfigDict(arbitrary_types_allowed=True)
