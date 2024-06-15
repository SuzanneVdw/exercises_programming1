from collections import namedtuple

Color = namedtuple("Color", ["r","g","b"])

def valid_color(color):
    if 0 <= color.r <= 255 and 0 <= color.b <= 255 and 0 <= color.g <= 255:
        return True
    return False

def clamp_color(color):
    red = color.r
    green = color.g
    blue = color.b
    if red < 0:
        red = 0
    if red > 255:
        red = 255
    if green < 0:
        green = 0
    if green > 255:
        green = 255
    if blue < 0:
        blue = 0
    if blue > 255:
        blue = 255
    new_color = Color(red,green,blue)
    return new_color