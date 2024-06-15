def increase_version(version, breaking_change, new_features):

    if breaking_change == True:
        new_version = (version[0]+1,0,0)
    elif new_features == True:
        new_version = (version[0],version[1]+1,0)
    else:
        new_version = (version[0],version[1],version[2]+1)
    return new_version

def is_more_recent(v1, v2):
    if v1[0] < v2[0]:
        return False
    elif v1[0] > v2[0]:
        return True
    else:
        if v1[1] < v2[1]:
            return False
        elif v1[1] > v2[1]:
            return True
        else:
            if v1[2] < v2[2]:
                return False
            elif v1[2] > v2[2]:
                return True
            else:
                return False

def is_older(v1, v2):
    return not v1 == v2 and not is_more_recent(v1,v2)

print(is_more_recent((2,1,0),(1,1,1)))