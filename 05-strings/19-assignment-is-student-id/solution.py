def is_digit(char):
    return char in '0123456789'

def is_student_id(string):
    if len(string) != 8:
        return False
    if string[0].lower() not in 'rs':
        return False
    if not is_digit(string[1]):
        return False
    if not is_digit(string[2]):
        return False
    if not is_digit(string[3]):
        return False
    if not is_digit(string[4]):
        return False
    if not is_digit(string[5]):
        return False
    if not is_digit(string[6]):
        return False
    if not is_digit(string[7]):
        return False
    return True