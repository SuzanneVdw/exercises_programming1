def remove_duplicates(xs):
    #TO BE IMPLEMENTED
    ys = []
    duplicates = set()
    for i in xs:
        if i not in duplicates:
            duplicates.add(i)
            ys.append(i)
    return ys