def increasing(ns):
    if ns == () or type(ns) == int:
        return True
    for i in range(1,len(ns)):
        if ns[i] < ns[i-1]:
            return False
        
    return True