def group_by_first_letter(strings):
    letter_dict = {}
    for i in strings:
        uppercase = i[0].upper()
        if uppercase not in letter_dict:
            letter_dict[uppercase] = [i]
        else:
            letter_dict[uppercase].append(i)
    return letter_dict