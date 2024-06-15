def all_equal(xs):
    for i in range(1,len(xs)):
        if xs[i] != xs[i-1]:
            return False
    return True