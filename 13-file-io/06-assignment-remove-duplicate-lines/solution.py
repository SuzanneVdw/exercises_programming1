
def remove_duplicate_lines(source, destination):
    with open(source) as in_file:
        with open(destination, 'w', encoding='utf-8') as out_file:
            last_line = None
            for line in in_file:
                if line != last_line:
                    out_file.write(line)
                    last_line = line
