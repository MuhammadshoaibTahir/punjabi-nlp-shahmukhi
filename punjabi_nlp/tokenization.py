import re

def sentence_tokenize(text):
    sentences = re.split(r"[.!?]", text)
    return [s.strip() for s in sentences if s.strip()]

def word_tokenize(text):
    # Separate punctuation from words
    text = re.sub(r"([?.!,])", r" \1 ", text)
    tokens = text.split()
    
    # Remove punctuation tokens
    tokens = [t for t in tokens if t not in [".", "?", "!", ","]]
    
    return tokens