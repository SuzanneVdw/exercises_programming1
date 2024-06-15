from math import ceil

def split_in_two(xs):
    left_tuple = xs[0:ceil(len(xs)/2)]
    right_tuple = xs[ceil(len(xs)/2):]
    result = (left_tuple,right_tuple)
    return result