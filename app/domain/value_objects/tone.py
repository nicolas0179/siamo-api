from enum import Enum


class ToneMarker(Enum):
    LOW_TONE_MARKER = "่"
    FALLING_TONE_MARKER = "้"
    HIGH_TONE_MARKER = "๊"
    RISING_TONE_MARKER = "๋"
    NO_TONE_MARKER = ""


class Tone(str, Enum):
    LOW_TONE = ("`",)
    FALLING_TONE = ("^",)
    HIGH_TONE = ("'",)
    RISING_TONE = ("ˇ",)
    MID_TONE = "\u2013"
