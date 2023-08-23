def user_input():
    expression = input("Enter your expression: ").lower()
    print(expression)
    return expression


def input_splitter(expression):
    tokens = expression.split()
    print(tokens)
    return tokens


def calculator(tokens):
    stack = []
    for _ in tokens:
        if _.isnumeric():
            stack.append(_)
        elif _ == "+":
            add(stack)
    print(stack)
    return stack


def add(stack):
    x = int(stack.pop())
    y = int(stack.pop())
    result = x + y
    stack.append(result)
    print(result)


def main():
    while True:
        user_expression = user_input()
        if user_expression == "exit":
            break
        else:
            tokens = input_splitter(user_expression)
            calculator(tokens)


# This is the standard boilerplate that calls the main() function.
# Do not modify this block.
if __name__ == "__main__":
    main()
