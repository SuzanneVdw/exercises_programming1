def parse_position_x(string):
    without_parentheses = string[1:-1]
    index = without_parentheses.find(',')
    left = without_parentheses[:index]
    return float(left)


def parse_position_y(string):
    without_parentheses = string[1:-1]
    index = without_parentheses.find(',')
    right = without_parentheses[index+2:]
    return float(right)