def is_digit(char):
    numbers = "0123456789"
    if char in numbers:
        return True
    return False

def is_student_id(string):
    string_lower = string.lower()
    if len(string) != 8:
        return False
    return (string_lower[0] == "r" or string_lower[0] == "s") and (is_digit(string[1]) and is_digit(string[2]) and is_digit(string[3]) and is_digit(string[4]) and is_digit(string[5]) and is_digit(string[6]) and is_digit(string[7]))