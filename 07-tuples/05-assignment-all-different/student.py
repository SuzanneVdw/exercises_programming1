def all_different(xs):

    for i in range(0,len(xs)):
        for j in range(i+1,len(xs)):
            if xs[i] == xs[j]:
                return False
            
    return True