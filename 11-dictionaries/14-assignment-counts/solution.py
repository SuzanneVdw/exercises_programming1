def counts(xs):
    result = {}
    for x in xs:
        result[x] = result.get(x, 0) + 1
    return result