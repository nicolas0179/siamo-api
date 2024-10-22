from abc import ABC, abstractmethod
import numpy as np


class ITTSService(ABC):
    @abstractmethod
    def to_waveform(self, text: str) -> np.ndarray:
        pass
