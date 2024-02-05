def plagiarism(s1, s2):
    lines1 = set(s1.splitlines())
    lines2 = set(s2.splitlines())
    return len(lines1 & lines2)