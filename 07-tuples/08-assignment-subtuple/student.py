def subtuple(xs, ys):

    if ys == () or (type(ys) == int and ys in xs):
         return True

    for i in range(0,len(xs)):
        for j in range(0,len(ys)):
            if ys[j] != xs[i+j]:
                break
            if j == len(ys)-1:
                return True
        if (len(xs) - len(ys) - i) < 0:
            return False
    return False