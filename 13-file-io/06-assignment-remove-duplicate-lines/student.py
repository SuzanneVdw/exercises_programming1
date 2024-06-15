def remove_duplicate_lines(source, destination):
    list_lines = []
    with open(source, encoding='utf-8') as file:
        for i in file:
            list_lines.append(i)
    
    with open(destination, 'w', encoding='utf-8') as file:
        file.write(list_lines[0])
        for i in range(1,len(list_lines)):
            if list_lines[i] != list_lines[i-1]:
                file.write(list_lines[i])