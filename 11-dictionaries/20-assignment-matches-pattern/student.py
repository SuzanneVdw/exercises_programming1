def matches_pattern(pattern, string):
    if len(pattern) != len(string):
        return False
    dict_one = {}
    dict_two = {}
    for i in range(0,len(pattern)):
        if pattern[i] not in dict_one and string[i] not in dict_two:
            dict_one[pattern[i]] = string[i]
            dict_two[string[i]] = pattern[i]
        elif pattern[i] not in dict_one and string[i] in dict_two:
            return False
        elif dict_one[pattern[i]] == string[i]:
            pass
        else:
            return False
    return True