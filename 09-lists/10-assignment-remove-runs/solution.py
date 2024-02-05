def remove_runs(ns):
    result = []
    for n in ns:
        if not result or result[-1] != n:
            result.append(n)
    return result