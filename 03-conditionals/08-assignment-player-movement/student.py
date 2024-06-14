def player_movement(position, left_arrow, right_arrow, shift):
    if shift == False:
        if left_arrow == True:
            position -= 1
        if right_arrow == True:
            position += 1
    if shift == True:
        if left_arrow == True:
            position -= 2
        if right_arrow == True:
            position += 2
    return position
