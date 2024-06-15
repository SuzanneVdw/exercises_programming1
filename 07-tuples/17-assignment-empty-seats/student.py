def empty_seats(used_seats):
    unused_seats = 0
    for i in range(1,len(used_seats)):
        unused_seats += (used_seats[i] - used_seats[i-1])-1
    return unused_seats