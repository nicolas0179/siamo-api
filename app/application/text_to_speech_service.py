from app.schema.tts_response import TTSResponse
from app.domain.interfaces.itts_service import ITTSService


class TextToSpeechService:
    def __init__(self, tts_service: ITTSService):
        self.tts_service = tts_service

    def process_sentence(self, sentence: str) -> TTSResponse:
        waveform = self.tts_service.to_waveform(sentence)
        return TTSResponse(waveform=waveform)
