from fastapi.testclient import TestClient

from app.domain.value_objects.tone import Tone

from app.main import app, root_path

from app.schema.tone_identifier_response import (
    SyllableResponse,
    ToneIdentifierResponse,
    ToneResponse,
)

client = TestClient(app)


class TestToneIdentifierRouter:
    def setup_method(self):
        pass

    def test_tone_identifier(self, mocker):
        toneIdentifierResponse = ToneIdentifierResponse(
            text="สวัสดีชาวโลก",
            syllables=[
                SyllableResponse(
                    syllable="สวัสดี",
                    tone=ToneResponse(
                        name=Tone.HIGH_TONE.name, symbol=Tone.HIGH_TONE.value
                    ),
                )
            ],
        )
        mocker.patch(
            "app.application.tone_identifier_service.ToneIdentifierService.process_sentence",
            return_value=toneIdentifierResponse,
        )
        response = client.post(
            f"{root_path}/toneIdentifier", json={"text": "สวัสดีชาวโลก"}
        )
        assert response.status_code == 200
        assert response.json() == toneIdentifierResponse.model_dump()

    def test_tone_identifier_with_exception(self, mocker):
        mocker.patch(
            "app.application.tone_identifier_service.ToneIdentifierService.process_sentence",
            side_effect=Exception("Error"),
        )
        response = client.post(
            f"{root_path}/toneIdentifier", json={"text": "สวัสดีชาวโลก"}
        )
        assert response.status_code == 500
        assert response.json() == {"detail": "Error"}
