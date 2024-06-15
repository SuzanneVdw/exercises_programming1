def find_duplicates(xs):
    existing = set()
    duplicates = []
    for i in xs:
        if i in existing:
            if i not in duplicates:
                duplicates.append(i)
        else:
            existing.add(i)
    return duplicates
