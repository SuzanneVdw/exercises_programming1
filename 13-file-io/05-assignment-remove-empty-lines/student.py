def remove_empty_lines(source, destination):
    list_lines = []
    with open(source, encoding='utf-8') as file:
        for i in file:
            list_lines.append(i)

    with open(destination, 'w', encoding='utf-8') as file:
        for i in list_lines:
            if i != "\n":
                file.write(i)