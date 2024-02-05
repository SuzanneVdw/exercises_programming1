def sum_input():
    result = 0
    value = int(input("Enter integer: "))
    while value != 0:
        result += value
        value = int(input("Enter integer: "))
    print(f'The sum equals {result}.')
