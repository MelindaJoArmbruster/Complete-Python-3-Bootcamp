# def cap_text(text):
#     words = text.split()
#     cap_words = [word[0].upper() + word[1:] for word in words]
#     return ' '.join(cap_words)

import string


def cap_text(textString):
    return string.capwords(textString, sep=None)
