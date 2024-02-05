def count_lines_in_file(path):
    result = 0
    with open(path, encoding='utf-8') as file:
        while file.readline():
            result += 1
    return result
