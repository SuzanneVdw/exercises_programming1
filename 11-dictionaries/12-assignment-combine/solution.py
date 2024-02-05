def combine(d1, d2):
    result = {}
    for key, value in d1.items():
        if value in d2:
            result[key] = d2[value]
    return result