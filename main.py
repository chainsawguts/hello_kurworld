def user_input():
    expression = input("Enter your expression: ").lower()
    return expression


def input_splitter(expression):
    tokens = expression.split()
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
    return stack


def add(stack):
    y = stack.pop()
    x = stack.pop()
    result = x + y
    stack.append(result)


def subtract(stack):
    y = stack.pop()
    x = stack.pop()
    result = x - y
    stack.append(result)


def multiply(stack):
    y = stack.pop()
    x = stack.pop()
    result = x * y
    stack.append(result)


def divide(stack):
    y = stack.pop()
    x = stack.pop()
    result = x / y
    stack.append(result)


def main():
    while True:
        user_expression = user_input()
        if user_expression == "exit":
            break
        else:
            tokens = input_splitter(user_expression)
            result = calculator(tokens)
            print(*result)


# This is the standard boilerplate that calls the main() function.
# Do not modify this block.
if __name__ == "__main__":
    main()
