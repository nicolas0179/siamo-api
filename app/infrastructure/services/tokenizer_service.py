from typing import List
from pythainlp.tokenize import syllable_tokenize
from pythainlp.util import isthai
from app.domain.interfaces.itokenizer_service import ITokenizerService


class TokenizerService(ITokenizerService):

    def tokenize_syllable(self, text: str) -> List[str]:
        return syllable_tokenize(text, keep_whitespace=False)

    def is_thai_sentence(self, text: str) -> bool:
        return isthai(text, ignore_chars=" ")
