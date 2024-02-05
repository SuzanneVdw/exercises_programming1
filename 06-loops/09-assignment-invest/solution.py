def invest(amount, rate, goal):
    current = amount
    year_count = 0
    while current < goal:
        current += current * rate / 100
        year_count += 1
    return year_count
