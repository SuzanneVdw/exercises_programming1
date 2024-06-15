def split_name(full_name):
    space_loc = full_name.find(" ")
    first_name = full_name[0:space_loc]
    last_name = full_name[space_loc+1:]
    name_tuple = (first_name,last_name)
    return name_tuple