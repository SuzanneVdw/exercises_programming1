def inverse_lookup(dictionary, value):
    result = []
    for k, v in dictionary.items():
        if v == value:
            result.append(k)
    return result
