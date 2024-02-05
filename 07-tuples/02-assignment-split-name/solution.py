def split_name(full_name):
    space_index = full_name.find(' ')
    first_name = full_name[:space_index]
    last_name = full_name[space_index+1:]
    return (first_name, last_name)