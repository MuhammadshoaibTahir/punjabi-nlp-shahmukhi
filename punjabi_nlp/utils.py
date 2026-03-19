def detect_script(text):
    shahmukhi_count = 0
    gurmukhi_count = 0
    roman_count = 0

    for ch in text:
        if "\u0600" <= ch <= "\u06FF":
            shahmukhi_count += 1
        elif "\u0A00" <= ch <= "\u0A7F":
            gurmukhi_count += 1
        elif ch.isascii() and ch.isalpha():
            roman_count += 1

    if shahmukhi_count > roman_count:
        return "shahmukhi"
    elif gurmukhi_count > roman_count:
        return "gurmukhi"
    else:
        return "roman"