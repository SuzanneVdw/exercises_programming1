def matching_brackets(string):
    stack = []

    for char in string:
        if char in '([{':
            stack.append(char)
        else:
            if char == ')':
                expected_bracket = '('
            elif char == '}':
                expected_bracket = '{'
            else:
                expected_bracket = '['

            if len(stack) == 0 or stack[-1] != expected_bracket:
                return False

            stack.pop()

    return len(stack) == 0