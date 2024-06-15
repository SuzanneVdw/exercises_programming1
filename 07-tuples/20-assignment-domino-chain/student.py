def domino_chain(dominos):
    for i in range(1,len(dominos)):
        if dominos[i-1][1] != dominos[i][0]:
            return False       
    return True