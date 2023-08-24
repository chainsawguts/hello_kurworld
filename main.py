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
    for token in tokens:
        if token.isnumeric():
            stack.append(int(token))
        elif token == "+":
            add(stack)
        elif token == "-":
            subtract(stack)
        elif token == "*":
            multiply(stack)
        elif token == "/":
            divide(stack)
    print(stack)
    return stack


def add(stack):
    x = stack.pop()
    y = stack.pop()
    result = y + x
    stack.append(result)
    print(result)


def subtract(stack):
    x = stack.pop()
    y = stack.pop()
    result = y - x
    stack.append(result)
    print(result)


def multiply(stack):
    x = stack.pop()
    y = stack.pop()
    result = y * x
    stack.append(result)
    print(result)


def divide(stack):
    x = stack.pop()
    y = stack.pop()
    result = y / x
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
