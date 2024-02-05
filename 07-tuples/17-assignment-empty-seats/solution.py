def empty_seats(used_seats):
    if len(used_seats) == 0:
        return 0
    total_seats = max(used_seats) - min(used_seats) + 1
    return total_seats - len(used_seats)
