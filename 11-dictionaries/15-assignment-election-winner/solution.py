
def election_winner(votes):
    vote_counts = {}
    winner = None
    winner_vote_count = 0
    for vote in votes:
        updated_count = vote_counts.get(vote, 0) + 1
        vote_counts[vote] = updated_count
        if updated_count > winner_vote_count:
            winner = vote
            winner_vote_count = updated_count
    return winner