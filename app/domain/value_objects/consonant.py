from enum import Enum


class ConsonantClass(Enum):
    LOW_CLASS = "LOW_CLASS"
    MID_CLASS = "MID_CLASS"
    HIGH_CLASS = "HIGH_CLASS"


LOW_CLASS_CONSONANTS = [
    "ค",
    "ฅ",
    "ฆ",
    "ง",
    "ช",
    "ซ",
    "ฌ",
    "ญ",
    "ฑ",
    "ฒ",
    "ณ",
    "ท",
    "ธ",
    "น",
    "พ",
    "ฟ",
    "ภ",
    "ม",
    "ย",
    "ร",
    "ล",
    "ว",
    "ฬ",
    "ฮ",
]
MID_CLASS_CONSONANTS = ["ก", "จ", "ฎ", "ฏ", "ด", "ต", "บ", "ป", "อ"]
HIGH_CLASS_CONSONANTS = ["ข", "ฃ", "ฉ", "ฐ", "ถ", "ผ", "ฝ", "ศ", "ษ", "ส", "ห"]
ALL_CONSONANTS = [
    *LOW_CLASS_CONSONANTS,
    *MID_CLASS_CONSONANTS,
    *HIGH_CLASS_CONSONANTS,
]
STOP_CONSONANTS = [
    "ก",
    "ข",
    "ค",
    "ฆ",
    "ป",
    "พ",
    "ภ",
    "ฟ",
    "บ",
    "ต",
    "ฏ",
    "ถ",
    "ฐ",
    "ท",
    "ฒ",
    "ฑ",
    "ธ",
    "จ",
    "ช",
    "ฌ",
    "ส",
    "ศ",
    "ษ",
    "ด",
    "ฎ",
]
