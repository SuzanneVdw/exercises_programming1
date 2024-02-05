
def remove_all(xs, item_to_remove):
    for i in range(len(xs) - 1, -1, -1):
        if xs[i] == item_to_remove:
            del xs[i]