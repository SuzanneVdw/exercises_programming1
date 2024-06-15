def mastermind(code, guess):
    correct_pos = 0
    wrong_pos = 0
    for i in range(0,len(guess)):
        if guess[i] == code[i]:
            correct_pos += 1
            code[i] = "X"
    for i in range(0,len(guess)):
        if guess[i] in code:
            wrong_pos += 1
            code_pos = code.index(guess[i])
            code[code_pos] = "X"
    return [correct_pos,wrong_pos]