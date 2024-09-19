from typing import List
from app.domain.interfaces.itokenizer_service import ITokenizerService
from app.domain.value_objects.consonant import (
    ALL_CONSONANTS,
    LOW_CLASS_CONSONANTS,
    MID_CLASS_CONSONANTS,
    STOP_CONSONANTS,
    ConsonantClass,
)
from app.domain.value_objects.syllable import SyllableType
from app.domain.value_objects.tone import Tone, ToneMarker
from app.domain.value_objects.vowel import SHORT_VOWELS
from app.schema.tone_identifier_response import (
    SyllableResponse,
    ToneIdentifierResponse,
    ToneResponse,
)


class ToneIdentifierService:
    """Defines the application service for the tone identifier domain."""

    def __init__(self, tokenizer_service: ITokenizerService):
        self.tokenizer_service = tokenizer_service

    def process_sentence(self, sentence: str) -> ToneIdentifierResponse:
        """
        Split the sentence into syllables and identify the tone of each
        syllable.
        """

        # If the sentence is empty, raise an error
        if not sentence:
            raise ValueError("Sentence is empty")

        # If the sentence is not a Thai sentence, raise an error
        if not self.tokenizer_service.is_thai_sentence(sentence):
            raise ValueError("Sentence contains non-Thai characters")

        # If the sentence is longer than 500 characters, raise an error
        if len(sentence) > 500:
            raise ValueError(
                "Text is too long. Please split your text into chunks of "
                "500 characters or less."
            )

        # Split the sentence into syllables
        syllables: List[str] = self.__split_into_syllables(sentence)

        # Identify the tone of each syllable
        syllables_with_tone: List[SyllableResponse] = (
            self.__identify_tone_of_syllables(syllables)
        )
        return ToneIdentifierResponse(syllables=syllables_with_tone)

    def __split_into_syllables(self, sentence: str) -> List[str]:
        """
        Split the sentence into syllables.
        """
        return self.tokenizer_service.tokenize_syllable(sentence)

    def __identify_tone_of_syllables(
        self, syllables: List[str]
    ) -> List[SyllableResponse]:
        """
        Identify the tone of a syllable.
        """
        return [
            SyllableResponse(
                syllable=syllable, tone=self.__identify_tone(syllable)
            )
            for syllable in syllables
        ]

    def __identify_tone(self, syllable: str) -> ToneResponse:
        """
        Identify the tone of a syllable.
        """

        tone_marker = self.__get_tone_marker(syllable)
        if tone_marker == ToneMarker.HIGH_TONE_MARKER:
            return ToneResponse(
                name=Tone.HIGH_TONE.name, symbol=Tone.HIGH_TONE.value
            )
        if tone_marker == ToneMarker.RISING_TONE_MARKER:
            return ToneResponse(
                name=Tone.RISING_TONE.name, symbol=Tone.RISING_TONE.value
            )
        initial_consonant_class = self.__get_initial_consonant_class_of_word(
            syllable
        )
        if (
            tone_marker == ToneMarker.LOW_TONE_MARKER
            and initial_consonant_class == ConsonantClass.LOW_CLASS
        ):
            return ToneResponse(
                name=Tone.FALLING_TONE.name, symbol=Tone.FALLING_TONE.value
            )
        if (
            tone_marker == ToneMarker.LOW_TONE_MARKER
            and initial_consonant_class != ConsonantClass.LOW_CLASS
        ):
            return ToneResponse(
                name=Tone.LOW_TONE.name, symbol=Tone.LOW_TONE.value
            )
        if (
            tone_marker == ToneMarker.FALLING_TONE_MARKER
            and initial_consonant_class == ConsonantClass.LOW_CLASS
        ):
            return ToneResponse(
                name=Tone.HIGH_TONE.name, symbol=Tone.HIGH_TONE.value
            )
        if (
            tone_marker == ToneMarker.FALLING_TONE_MARKER
            and initial_consonant_class != ConsonantClass.LOW_CLASS
        ):
            return ToneResponse(
                name=Tone.FALLING_TONE.name, symbol=Tone.FALLING_TONE.value
            )
        syllable_type = self.__is_dead_or_live_syllable(syllable)
        if (
            syllable_type == SyllableType.LIVE
            and initial_consonant_class == ConsonantClass.HIGH_CLASS
        ):
            return ToneResponse(
                name=Tone.RISING_TONE.name, symbol=Tone.RISING_TONE.value
            )
        if (
            syllable_type == SyllableType.LIVE
            and initial_consonant_class != ConsonantClass.HIGH_CLASS
        ):
            return ToneResponse(
                name=Tone.MID_TONE.name, symbol=Tone.MID_TONE.value
            )
        if (
            initial_consonant_class == ConsonantClass.LOW_CLASS
            and self.__contains_short_vowel(syllable)
        ):
            return ToneResponse(
                name=Tone.HIGH_TONE.name, symbol=Tone.HIGH_TONE.value
            )
        if initial_consonant_class == ConsonantClass.LOW_CLASS:
            return ToneResponse(
                name=Tone.FALLING_TONE.name, symbol=Tone.FALLING_TONE.value
            )
        return ToneResponse(
            name=Tone.LOW_TONE.name, symbol=Tone.LOW_TONE.value
        )

    def __get_tone_marker(self, syllable: str) -> ToneMarker:
        if "่" in syllable:
            return ToneMarker.LOW_TONE_MARKER
        if "้" in syllable:
            return ToneMarker.FALLING_TONE_MARKER
        if "๊" in syllable:
            return ToneMarker.HIGH_TONE_MARKER
        if "๋" in syllable:
            return ToneMarker.RISING_TONE_MARKER
        return ToneMarker.NO_TONE_MARKER

    def __get_consonant_class(self, consonant: str) -> ConsonantClass:
        if consonant in LOW_CLASS_CONSONANTS:
            return ConsonantClass.LOW_CLASS
        if consonant in MID_CLASS_CONSONANTS:
            return ConsonantClass.MID_CLASS
        return ConsonantClass.HIGH_CLASS

    def __get_initial_consonant(self, word: str) -> str:
        for c in word:
            if c in ALL_CONSONANTS:
                return c

    def __get_initial_consonant_class_of_word(
        self, word: str
    ) -> ConsonantClass:
        initial_consonant = self.__get_initial_consonant(word)
        return self.__get_consonant_class(initial_consonant)

    def __is_dead_or_live_syllable(self, syllable: str) -> SyllableType:
        if self.__has_final_consonant(
            syllable
        ) and self.__is_ending_with_stop_consonant(syllable):
            return SyllableType.DEAD
        if self.__has_final_consonant(syllable):
            return SyllableType.LIVE
        if self.__contains_short_vowel(syllable):
            return SyllableType.DEAD
        return SyllableType.LIVE

    def __has_final_consonant(self, syllable: str) -> bool:
        return syllable[-1] in ALL_CONSONANTS

    def __is_ending_with_stop_consonant(self, syllable: str) -> bool:
        return syllable[-1] in STOP_CONSONANTS

    def __contains_short_vowel(self, syllable: str) -> bool:
        return any(c in SHORT_VOWELS for c in syllable) or all(
            c in ALL_CONSONANTS for c in syllable
        )
