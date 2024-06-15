def heatwave(temperatures):
    over_25 = 0
    over_30 = 0
    for i in temperatures:
        if i >= 30:
            over_30 += 1
        if i >= 25:
            over_25 += 1
        else:
            over_25 = 0
            over_30 = 0
        if over_25 >= 5 and over_30 >= 3:
            return True 
    return False
    