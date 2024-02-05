def domino_chain(dominos):
    for i in range(1, len(dominos)):
        _, a = dominos[i-1]
        b, _ = dominos[i]
        if a != b:
            return False
    return True