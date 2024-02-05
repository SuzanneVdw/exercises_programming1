def is_capitalized(string):
    if len(string) == 0:
        return False

    first_char = string[0]
    remaining_chars = string[1:]
    return first_char.upper() == first_char and remaining_chars.lower() == remaining_chars
