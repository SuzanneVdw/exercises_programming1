
def concatenate(xs, ys):
    if xs is ys:
        ys = ys[:]
    for y in ys:
        xs.append(y)