def coins(amount):
    five_coins = amount // 5
    amount -= 5 * five_coins
    two_coins = amount // 2
    amount -= 2 * two_coins
    one_coins = amount
    return five_coins + two_coins + one_coins

