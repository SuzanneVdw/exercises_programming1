def split_in_two(xs):
    index = (len(xs) + 1) // 2
    return (xs[:index], xs[index:])