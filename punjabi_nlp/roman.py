import re

def roman_to_shahmukhi(text):
    words = text.split()
    converted = []

    for w in words:
        lw = w.lower()

        # MENU variations
        if re.fullmatch(r"m(e|i)?n(u|oo)?", lw):
            converted.append("مینوں")

        # TUSI / TUSSI variations 🔥 FIXED
        elif re.fullmatch(r"t(u|oo)?s+s(i|ee)?", lw):
            converted.append("تسی")

        # MAIN
        elif re.fullmatch(r"m(a|e)?i(n)?", lw):
            converted.append("میں")

        # AY / AE
        elif lw in ["ay", "ae"]:
            converted.append("اے")

        # THEEK
        elif re.fullmatch(r"th(e|ee)?k", lw):
            converted.append("ٹھیک")

        # LAGDA
        elif lw.startswith("lag"):
            converted.append("لگدا")

        # O
        elif lw == "o":
            converted.append("او")

        else:
            converted.append(w)

    return " ".join(converted)