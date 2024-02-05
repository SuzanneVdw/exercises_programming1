def make_teams(participants, team_size):
    team_count = max(1, len(participants) // team_size)
    teams = []
    for _ in range(team_count):
        teams.append([])
    for i in range(len(participants)):
        teams[i % team_count].append(participants[i])
    return teams