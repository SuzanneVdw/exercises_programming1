def all_equal(xs):
    for i in range(1, len(xs)):
        if xs[i-1] != xs[i]:
            return False
    return True