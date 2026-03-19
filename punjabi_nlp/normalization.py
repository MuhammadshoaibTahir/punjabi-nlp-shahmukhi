import re
import unicodedata

CHAR_MAP = {
    "ك": "ک", "ي": "ی", "ة": "ہ", "ھ": "ہ",
    "أ": "ا", "إ": "ا", "آ": "ا",
    "ى": "ی", "ئ": "ی",
    "ؤ": "و",
    "ۀ": "ہ",
    "ـ": "", "ء": "",
    "ٱ": "ا",
    "،": ",", "؛": ";", "؟": "?",
    "“": '"', "”": '"', "‘": "'", "’": "'",
}

WORD_MAP = {
    "کتہے": "کتھے",
    "کدھے": "کدے",
    "اے": "ہے",
}

def normalize_unicode(text):
    return unicodedata.normalize("NFKC", text)

def normalize_characters(text):
    for k, v in CHAR_MAP.items():
        text = text.replace(k, v)
    return text

def remove_diacritics(text):
    return re.sub(r"[ًٌٍَُِّْ]", "", text)

def normalize_words(text):
    words = text.split()
    words = [WORD_MAP.get(w, w) for w in words]
    return " ".join(words)

def normalize_repetitions(text):
    return re.sub(r"(.)\1{2,}", r"\1", text)

def normalize_whitespace(text):
    return re.sub(r"\s+", " ", text).strip()

def normalize(text):
    text = normalize_unicode(text)
    text = normalize_characters(text)
    text = remove_diacritics(text)
    text = normalize_repetitions(text)
    text = normalize_words(text)
    text = normalize_whitespace(text)
    return text