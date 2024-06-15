def passing_percentage(grades):
    passing_students = 0
    for i in grades:
        if i >= 10:
            passing_students += 1
    return (passing_students/len(grades))*100