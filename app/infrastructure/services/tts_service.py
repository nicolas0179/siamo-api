from typing import Any

import numpy as np
from app.domain.interfaces.itts_service import ITTSService
from pythaitts import TTS


class TTSService(ITTSService):
    def __init__(self):
        self.tts = TTS()

    def to_waveform(self, text: str) -> np.ndarray | str:
        wave = self.tts.tts(text, return_type="waveform")
        return wave
