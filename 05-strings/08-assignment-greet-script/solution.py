def greet(name):
    return f"Hello, {name}!"

def interactive_greet():
    name = input("What is your name? ")
    print(greet(name))


def main():
    interactive_greet()

if __name__ == '__main__':
    main()