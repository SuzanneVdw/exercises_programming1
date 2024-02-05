def passing_percentage(grades):
    passing = 0
    for grade in grades:
        if grade >= 10:
            passing += 1
    return passing / len(grades) * 100