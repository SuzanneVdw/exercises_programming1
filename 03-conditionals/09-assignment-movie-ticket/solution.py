def player_movement(position, left_arrow, right_arrow, shift):
    if shift:
        step = 2
    else:
        step = 1

    if left_arrow:
        position -= step
    if right_arrow:
        position += step

    return position