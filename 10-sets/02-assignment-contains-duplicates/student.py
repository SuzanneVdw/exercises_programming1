def contains_duplicates(xs):
    xs_set = set()
    for i in xs:
        xs_set.add(i)
    if len(xs) == len(xs_set):
        return False
    return True