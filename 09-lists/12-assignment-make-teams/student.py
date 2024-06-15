def make_teams(participants, team_size):
    if team_size > len(participants):
        return participants
    number_teams = len(participants)//team_size
    leftovers = len(participants)%team_size
    print(leftovers)
    actual_team_size = team_size + leftovers//number_teams
    actual_leftovers = len(participants)%actual_team_size
    teams_list = []
    starts_at = 0
    for i in range(0,number_teams):
        teams_list.append(participants[starts_at:starts_at+actual_team_size])
        starts_at += actual_team_size
    for i in range(0,actual_leftovers):
        teams_list[i].append(participants[starts_at])
        starts_at += 1
    return teams_list