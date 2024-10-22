import numpy as np
from app.application.text_to_speech_service import TextToSpeechService
from app.infrastructure.services.tts_service import TTSService
from app.schema.tts_response import TTSResponse


class TestTextToSpeechService:
    def setup_method(self):
        self.tts_service = TTSService()
        self.text_to_speech_service = TextToSpeechService(self.tts_service)

    def test_process_sentence(self, mocker):
        waveform = np.ndarray(shape=(2,), dtype=float)
        mocker.patch(
            "app.infrastructure.services.tts_service.TTSService.to_waveform",
            return_value=waveform,
        )

        ttsResponse = self.text_to_speech_service.process_sentence(
            "สวัสดีชาวโลก"
        )
        assert isinstance(ttsResponse, TTSResponse)
        assert ttsResponse.waveform.all() == waveform.all()
