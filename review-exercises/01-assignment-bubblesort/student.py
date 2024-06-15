def bubblesort(ns):
    while is_sorted(ns) == False:
        for i in range(1,len(ns)):
            if ns[i-1] > ns[i]:
                first_number = ns[i]
                second_number = ns[i-1]
                ns[i-1] = first_number
                ns[i] = second_number

def is_sorted(ns):
    for i in range(1,len(ns)):
        if ns[i-1] > ns[i]:
            return False
    return True