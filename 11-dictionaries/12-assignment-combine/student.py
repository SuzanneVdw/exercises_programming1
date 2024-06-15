def combine(d1, d2):
    d3 = {}
    for i in d1:
        if d1[i] in d2:
            d3[i] = d2[d1[i]]
    return d3