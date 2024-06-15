def inverse_lookup(dictionary, value):
    keys_list = []
    for i in dictionary:
        if dictionary[i] == value:
            keys_list.append(i)
    return keys_list