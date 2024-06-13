def hours(duration):
    return duration//3600

def minutes(duration):
    leftovers = duration-(hours(duration)*3600)
    return leftovers//60

def seconds(duration):
    leftovers = duration-(hours(duration)*3600)
    print(leftovers)
    return leftovers-minutes(leftovers)*60


