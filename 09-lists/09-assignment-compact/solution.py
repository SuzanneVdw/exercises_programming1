def compact(xs):
    result = []
    for x in xs:
        if x is not None:
            result.append(x)
    return result


def compact_in_place(xs):
    for i in range(len(xs) - 1, -1, -1):
        if xs[i] is None:
            del xs[i]