def matching_brackets(string):
    open_brackets = []
    if string == "":
        return True
    for i in string:
        if i == "(" or i == "[" or i == "{":
            open_brackets.append(i)
        elif i == ")":
            if len(open_brackets) == 0:
                return False
            elif open_brackets[-1] == "(":
                open_brackets.pop()
            else:
                return False
        elif i == "]":
            if len(open_brackets) == 0:
                return False
            elif open_brackets[-1] == "[":
                open_brackets.pop()
            else:
                return False
        elif i == "}":
            if len(open_brackets) == 0:
                return False
            elif open_brackets[-1] == "{":
                open_brackets.pop()
            else:
                return False           
    if open_brackets == []:
        return True
    else:
        return False
