#!/usr/bin/env py

def tip_calculator():
    total_price = int(input("Enter total price: "))
    tip_percentage = input("Enter tip percentage (default=20): ")
    if tip_percentage == '':
        tip_percentage = 20
    tip_percentage = int(tip_percentage)
    with_tip = round(total_price + total_price*(tip_percentage/100))
    print(f"You have to pay {with_tip}")

def main():
    tip_calculator()

if __name__ == '__main__':
    main()