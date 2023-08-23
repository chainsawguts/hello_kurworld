def user_input():
    expression = input("Enter your expression: ").lower()
    print(expression)
    return expression


def main():
    while True:
        exit_check = user_input()
        if exit_check == "exit":
            break


# This is the standard boilerplate that calls the main() function.
# Do not modify this block.
if __name__ == "__main__":
    main()
