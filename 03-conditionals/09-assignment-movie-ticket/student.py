from math import ceil

def movie_ticket(duration, imax, student, ticket_count):
    price = 10
    if 90 <= duration < 120:
        price += 1
    if 120 <= duration < 150:
        price += 2
    if duration > 150:
        price += 5
    if imax == True:
        price = ceil(price * 1.2)
    if student == True:
        price -= 3

    return price*ticket_count
