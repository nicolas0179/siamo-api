from typing import List
from pythainlp.tokenize import syllable_tokenize
from pythainlp.util import isthai
from pythainlp.transliterate import romanize
from app.domain.interfaces.itokenizer_service import ITokenizerService


class TokenizerService(ITokenizerService):

    def tokenize_syllable(self, text: str) -> List[str]:
        return syllable_tokenize(text, keep_whitespace=False)

    def is_thai_sentence(self, text: str) -> bool:
        return isthai(text, ignore_chars=" ")

    def romanize_syllable(self, syllable: str) -> str:
        return romanize(syllable, engine="thai2rom")
