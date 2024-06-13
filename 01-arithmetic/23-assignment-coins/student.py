def coins(amount):
    coins_5 = amount//5
    coins_2 = (amount - 5*coins_5)//2
    coins_1 = amount - 5*coins_5 - 2*coins_2
    return coins_5 + coins_2 + coins_1