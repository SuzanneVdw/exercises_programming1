def count_lines_in_file(path):
    list_lines = []
    with open(path) as file:
        for i in file:
            list_lines.append(i)
    return len(list_lines)