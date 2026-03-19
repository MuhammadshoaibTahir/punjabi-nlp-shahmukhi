STOPWORDS = {
    "تے", "ہے", "نوں", "دا", "دی", "دے",
    "سی", "میں", "تو", "وی"
}

def remove_stopwords(tokens):
    return [t for t in tokens if t not in STOPWORDS]