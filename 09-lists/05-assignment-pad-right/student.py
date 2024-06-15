def pad_right(xs, length, padding):
    if len(xs) >= length:
        pass
    for i in range(len(xs),length):
        xs.append(padding)