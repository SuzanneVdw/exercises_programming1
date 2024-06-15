def remove_runs(ns):
    ms = []
    if ns == []:
        return ms
    ms.append(ns[0])
    if len(ns) == 1: 
        return ms
    for i in range(1,len(ns)):
        if ns[i] != ns[i-1]:
            ms.append(ns[i])
    return ms

