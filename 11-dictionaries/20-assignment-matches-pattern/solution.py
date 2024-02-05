def matches_pattern(pattern, string):
    if len(pattern) != len(string):
        return False
    bindings = {}
    for i in range(len(pattern)):
        pc = pattern[i]
        sc = string[i]
        if pc in bindings:
            if bindings[pc] != sc:
                return False
        elif sc in bindings.values():
            return False
        else:
            bindings[pc] = sc
    return True
