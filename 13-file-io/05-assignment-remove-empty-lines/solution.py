def remove_empty_lines(source, destination):
    with open(source) as in_file:
        with open(destination, 'w', encoding='utf-8') as out_file:
            for line in in_file:
                if line != '\n':
                    out_file.write(line)
