def rpg2(n_sides, goal):
    total_wins = 0
    for i in range(1,n_sides+1):
        for j in range(1,n_sides+1):
            if i + j >= goal:
                total_wins += 1
    return (total_wins/(n_sides**2))*100

def rpg3(n_sides, goal):
    total_wins = 0
    for i in range(1,n_sides+1):
        for j in range(1,n_sides+1):
            for k in range(1,n_sides+1):
                if i + j + k >= goal:
                    total_wins += 1
    return (total_wins/(n_sides**3))*100