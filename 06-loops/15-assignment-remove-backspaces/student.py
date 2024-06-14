def remove_backspaces(string):
    result = string[0]
    for i in range(1,len(string)):
        if string[i-1] == "\\" and string[i] == "b":
            result = result[0:len(result)-2]
        else:
            result += string[i]
    return result