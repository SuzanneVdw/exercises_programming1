def spellcheck(document, valid_words):
    document_list = (document.lower()).split()
    document_set = set()
    valid_words_set = set()
    for i in document_list:
        document_set.add(i)
    for i in valid_words:
        valid_words_set.add(i)
    return document_set - valid_words_set