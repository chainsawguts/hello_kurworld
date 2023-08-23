def user_input():
    expression = input("Enter your expression: ").lower()
    print(expression)
    return expression


def input_splitter(expression):
    tokens = expression.split()
    print(tokens)
    return tokens


def main():
    while True:
        user_expression = user_input()
        if user_expression == "exit":
            break
        else:
            input_splitter(user_expression)


# This is the standard boilerplate that calls the main() function.
# Do not modify this block.
if __name__ == "__main__":
    main()
