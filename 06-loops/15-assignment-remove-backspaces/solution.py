def remove_backspaces(string):
    result = ''
    for char in string:
        if char == '\b':
            result = result[:-1]
        else:
            result += char
    return result