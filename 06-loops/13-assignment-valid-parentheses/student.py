def valid_parentheses(string):
    number_open = 0
    for i in string:
        if number_open < 0:
            return False
        if i == "(":
            number_open += 1
        if i == ")":
            number_open -= 1
    if number_open == 0:
        return True
    return False


