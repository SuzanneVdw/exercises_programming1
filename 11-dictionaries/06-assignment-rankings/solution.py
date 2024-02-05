def rankings(participants):
    result = {}
    for index in range(len(participants)):
        participant = participants[index]
        ranking = index + 1
        result[participant] = ranking
    return result
