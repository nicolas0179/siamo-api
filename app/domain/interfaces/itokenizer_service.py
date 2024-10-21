from abc import ABC, abstractmethod
from typing import List


class ITokenizerService(ABC):
    @abstractmethod
    def tokenize_syllable(self, text: str) -> List[str]:
        pass

    @abstractmethod
    def is_thai_sentence(self, text: str) -> bool:
        pass

    @abstractmethod
    def romanize_syllable(self, syllable: str) -> str:
        pass
