from fastapi.testclient import TestClient
import numpy as np

from app.main import app, root_path

from app.schema.tts_response import TTSResponse

client = TestClient(app)


class TestTextToSpeechRouter:
    def test_text_to_speech(self, mocker):
        ttsResponse = TTSResponse(
            waveform=np.ndarray(shape=(2,), dtype=float),
        )
        mocker.patch(
            "app.application.text_to_speech_service.TextToSpeechService.process_sentence",
            return_value=ttsResponse,
        )
        response = client.post(f"{root_path}/tts", json={"text": "สวัสดีชาวโลก"})
        assert response.status_code == 200
        assert response.json() == ttsResponse.model_dump()

    def test_text_to_speech_with_exception(self, mocker):
        mocker.patch(
            "app.application.text_to_speech_service.TextToSpeechService.process_sentence",
            side_effect=Exception("Error"),
        )
        response = client.post(f"{root_path}/tts", json={"text": "สวัสดีชาวโลก"})
        assert response.status_code == 500
        assert response.json() == {"detail": "Error"}
