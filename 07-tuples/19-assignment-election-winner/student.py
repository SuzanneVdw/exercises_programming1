def election_winner(votes):
    if votes == ():
        return None
    sorted_votes = sorted(votes)
    print(sorted_votes)
    current_votes = 1
    winner_votes = 0
    winner = sorted_votes[0]
    
    for i in range(1,len(sorted_votes)):
        if sorted_votes[i-1] == sorted_votes[i]:
            current_votes += 1
            print(current_votes)
            if current_votes > winner_votes:
                winner = sorted_votes[i-1]
        else:
            if current_votes > winner_votes:
                winner = sorted_votes[i-1]
                winner_votes = current_votes
            current_votes = 1

    return winner

