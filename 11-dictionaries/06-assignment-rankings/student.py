def rankings(participants):
    ranking = {}
    number = 1
    for i in participants:
        ranking[i] = number
        number += 1
    return ranking