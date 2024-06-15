def plagiarism(s1, s2):
    s1_split = s1.split()
    s1_set = set()
    s2_split = s2.split()
    s2_set = set()
    for i in s1_split:
        s1_set.add(i)
    for i in s2_split:
        s2_set.add(i)
    unique_lines = s1_set - s2_set
    return len(s1_set)-len(unique_lines)
    