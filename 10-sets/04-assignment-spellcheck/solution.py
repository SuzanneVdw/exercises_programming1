def spellcheck(document, valid_words):
    valid_words_set = set(valid_words)
    words_set = set()
    for line in document.splitlines():
        for word in line.split(' '):
            words_set.add(word.lower())
    return words_set - valid_words_set
