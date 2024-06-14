def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    skipped_tests = 0
    taken_tests = 0
    test_average = 0

    if grade1 == None:
        skipped_tests += 1
    else:
        taken_tests += 1
        test_average += grade1

    if grade2 == None:
        skipped_tests += 1
    else:
        taken_tests += 1
        test_average += grade2

    if grade3 == None:
        skipped_tests += 1
    else:
        taken_tests += 1
        test_average += grade3

    if grade4 == None:
        skipped_tests += 1
    else:
        taken_tests += 1
        test_average += grade4

    if grade5 == None:
        skipped_tests += 1
    else:
        taken_tests += 1
        test_average += grade5

    return skipped_tests <= 1 and (test_average/taken_tests) >= 12