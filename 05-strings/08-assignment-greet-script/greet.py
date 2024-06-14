#!/usr/bin/env py
def greet(name):
    return f"Hello, {name}!"

def main():
    # Startup code
    name = input("What is your name?")
    print(greet(name))


if __name__ == '__main__':
    main()