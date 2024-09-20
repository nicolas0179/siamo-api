import pytest
from app.application.tone_identifier_service import ToneIdentifierService
from app.domain.value_objects.consonant import ConsonantClass
from app.domain.value_objects.syllable import SyllableType
from app.domain.value_objects.tone import Tone, ToneMarker
from app.infrastructure.services.tokenizer_service import TokenizerService
from app.schema.tone_identifier_response import ToneResponse


class TestToneIdentifierService:
    def setup_method(self):
        self.tokenizer_service = TokenizerService()
        self.tone_identifier_service = ToneIdentifierService(
            self.tokenizer_service
        )

    def test_process_sentence_with_empty_sentence(self):
        with pytest.raises(ValueError, match="Sentence is empty"):
            self.tone_identifier_service.process_sentence("")

    def test_process_sentence_with_non_thai_sentence(self):
        with pytest.raises(
            ValueError, match="Sentence contains non-Thai characters"
        ):
            self.tone_identifier_service.process_sentence("Hello, world!")

    def test_process_sentence_with_long_sentence(self):
        with pytest.raises(
            ValueError,
            match="Text is too long. Please split your text into chunks of "
            "500 characters or less.",
        ):
            self.tone_identifier_service.process_sentence("ประเทศไทยมี" * 50)

    def test_split_into_syllables(self):
        assert self.tone_identifier_service.split_into_syllables(
            "ประเทศไทย"
        ) == [
            "ประ",
            "เทศ",
            "ไทย",
        ]

    def test_identify_tone_particular_cases(self):
        assert self.tone_identifier_service.identify_tone("ก็") == ToneResponse(
            name=Tone.FALLING_TONE.name, symbol=Tone.FALLING_TONE.value
        )

    def test_get_tone_marker(self):
        assert (
            self.tone_identifier_service.get_tone_marker("ผ่าน")
            == ToneMarker.LOW_TONE_MARKER
        )
        assert (
            self.tone_identifier_service.get_tone_marker("น้ำ")
            == ToneMarker.FALLING_TONE_MARKER
        )
        assert (
            self.tone_identifier_service.get_tone_marker("ก๊า")
            == ToneMarker.HIGH_TONE_MARKER
        )
        assert (
            self.tone_identifier_service.get_tone_marker("ก๋า")
            == ToneMarker.RISING_TONE_MARKER
        )
        assert (
            self.tone_identifier_service.get_tone_marker("บาท")
            == ToneMarker.NO_TONE_MARKER
        )

    def test_get_consonant_class(self):
        assert (
            self.tone_identifier_service.get_consonant_class("ล")
            == ConsonantClass.LOW_CLASS
        )
        assert (
            self.tone_identifier_service.get_consonant_class("ต")
            == ConsonantClass.MID_CLASS
        )
        assert (
            self.tone_identifier_service.get_consonant_class("ฉ")
            == ConsonantClass.HIGH_CLASS
        )

    def test_get_initial_consonant(self):
        assert self.tone_identifier_service.get_initial_consonant("ตก") == "ต"
        assert self.tone_identifier_service.get_initial_consonant("เกง") == "ก"
        assert self.tone_identifier_service.get_initial_consonant("ลิ") == "ล"

    def test_get_initial_consonant_class_of_word(self):
        assert (
            self.tone_identifier_service.get_initial_consonant_class_of_word(
                "ตก"
            )
            == ConsonantClass.MID_CLASS
        )
        assert (
            self.tone_identifier_service.get_initial_consonant_class_of_word(
                "ลิ"
            )
            == ConsonantClass.LOW_CLASS
        )
        assert (
            self.tone_identifier_service.get_initial_consonant_class_of_word(
                "ฉลอง"
            )
            == ConsonantClass.HIGH_CLASS
        )

    def test_is_dead_or_live_syllable(self):
        assert (
            self.tone_identifier_service.is_dead_or_live_syllable("ตก")
            == SyllableType.DEAD
        )
        assert (
            self.tone_identifier_service.is_dead_or_live_syllable("เกง")
            == SyllableType.LIVE
        )
        assert (
            self.tone_identifier_service.is_dead_or_live_syllable("ลิ")
            == SyllableType.DEAD
        )
        assert (
            self.tone_identifier_service.is_dead_or_live_syllable("เขา")
            == SyllableType.LIVE
        )

    def test_has_final_consonant(self):
        assert self.tone_identifier_service.has_final_consonant("ตก") is True
        assert self.tone_identifier_service.has_final_consonant("ซัก") is True
        assert self.tone_identifier_service.has_final_consonant("ลิ") is False

    def test_is_ending_with_stop_consonant(self):
        assert (
            self.tone_identifier_service.is_ending_with_stop_consonant("ตก")
            is True
        )
        assert (
            self.tone_identifier_service.is_ending_with_stop_consonant("เกง")
            is False
        )

    def test_contains_short_vowel(self):
        assert self.tone_identifier_service.contains_short_vowel("ลิ") is True
        assert (
            self.tone_identifier_service.contains_short_vowel("เกง") is False
        )
