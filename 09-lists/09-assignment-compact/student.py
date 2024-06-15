def compact(xs):
    ys = []
    for i in xs:
        if i != None:
            ys.append(i)
    return ys

def compact_in_place(xs):
    i = 0
    if xs == []:
        return None
    while True:
        if xs[i] == None:
            xs.pop(i)
            i -= 1
        i += 1
        if i >= len(xs):
            break