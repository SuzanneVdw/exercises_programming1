def counts(xs):
    xs_dict = {}
    for i in xs:
        if i in xs_dict:
            xs_dict[i] += 1
        else:
            xs_dict[i] = 1
    return xs_dict