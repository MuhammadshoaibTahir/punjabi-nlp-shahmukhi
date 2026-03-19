from .normalization import normalize
from .tokenization import sentence_tokenize, word_tokenize
from .stopwords import remove_stopwords
from .utils import detect_script
from .roman import roman_to_shahmukhi
from collections import Counter

class PunjabiPipeline:
    def __init__(self, remove_stops=True):
        self.remove_stops = remove_stops

    def process(self, text):
        result = {}

        # Detect script
        # Normalize
        norm_text = normalize(text)

        # Convert Roman → Shahmukhi
        norm_text = roman_to_shahmukhi(norm_text)

        # 🔥 Detect script AFTER processing
        script = detect_script(norm_text)
        result["script"] = script

        result["normalized_text"] = norm_text

        # Sentence tokenize
        sentences = sentence_tokenize(norm_text)
        result["sentences"] = sentences

        # Word tokenize
        tokens = word_tokenize(norm_text)

        # Remove stopwords
        if self.remove_stops:
            tokens = remove_stopwords(tokens)

        result["tokens"] = tokens
        result["token_count"] = len(tokens)

        # Frequency analysis 🔥
        result["frequency"] = dict(Counter(tokens))

        return result