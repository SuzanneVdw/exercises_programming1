def election_winner(votes):
    votes = sorted(votes)
    winner = None
    winner_vote_count = 0
    i = 0
    while i < len(votes):
        j = i
        while j < len(votes) and votes[i] == votes[j]:
            j += 1
        vote_count = j - i + 1
        if vote_count > winner_vote_count:
            winner = votes[i]
            winner_vote_count = vote_count
        i = j
    return winner