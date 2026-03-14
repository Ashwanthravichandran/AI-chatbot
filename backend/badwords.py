bad_words = [
    "idiot",
    "stupid",
    "hate",
    "mad"
]

def contains_bad_words(text):

    text = text.lower()

    for word in bad_words:
        if word in text:
            return True

    return False