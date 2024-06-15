def election_winner(votes):
    votes_dict = {}
    winning_votes = 0
    winner = None
    for i in votes:
        if i in votes_dict:
            votes_dict[i] += 1
        else:
            votes_dict[i] = 1
    for i in votes_dict:
        if votes_dict[i] > winning_votes:
            winner = i
            winning_votes = votes_dict[i]
    return winner