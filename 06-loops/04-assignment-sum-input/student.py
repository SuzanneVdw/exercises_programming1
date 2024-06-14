def sum_input():
    sum = 0
    number = input("Enter integer: ")
    while number != "0":
        sum += int(number)
        number = input("Enter integer: ")
    print(f"The sum equals {sum}.")