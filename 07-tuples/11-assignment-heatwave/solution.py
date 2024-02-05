def heatwave(temperatures):
    above_25_count = 0
    above_30_count = 0
    for temperature in temperatures:
        if temperature < 25:
            above_25_count = 0
            above_30_count = 0
        else:
            above_25_count += 1
            if temperature >= 30:
                above_30_count += 1
            if above_25_count >= 5 and above_30_count >= 3:
                return True
    return False