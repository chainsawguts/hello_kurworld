import sys


def close_program():
    sys.exit()


def user_input():
    expression = input("Enter your expression: ").lower()
    print(expression)
    if expression == "exit":
        close_program()
    return expression


def main():
    while True:
        user_input()


# This is the standard boilerplate that calls the main() function.
# Do not modify this block.
if __name__ == "__main__":
    main()
