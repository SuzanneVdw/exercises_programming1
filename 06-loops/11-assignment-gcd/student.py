def gcd(x, y):
    abs_x = abs(x)
    abs_y = abs(y)
    minimum = min(abs_x,abs_y)
    for i in range(minimum+1,0,-1):
        if abs_x%i == 0 and abs_y%i == 0:
            return i