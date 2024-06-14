def parse_position_x(string):
    comma_loc = string.find(",")
    return float(string[1:comma_loc])

def parse_position_y(string):
    comma_loc = string.find(",")
    return float(string[comma_loc+2:-1])