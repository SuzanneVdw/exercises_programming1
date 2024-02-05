
def increasing(ns):
    for i in range(1, len(ns)):
        if ns[i-1] > ns[i]:
            return False
    return True