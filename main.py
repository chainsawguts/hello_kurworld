import sys


def repl_standby():
    while True:
        user_expression = user_input()
        if user_expression == "exit":
            break
        else:
            tokens = input_splitter(user_expression)
            result = calculator(tokens)
            if result == None:
                print("Try again!")
            else:
                print(*result)


def user_input():
    expression = input("Enter your expression: ").lower().strip()
    return expression


def input_splitter(expression):
    tokens = expression.split()
    return tokens


def calculator(tokens):
    try:
        stack = []
        operators = {"+": add, "-": subtract, "*": multiply, "/": divide}
        for token in tokens:
            if token.isnumeric() or (token[0] == "-" and token[1:].isdigit()):
                stack.append(int(token))
            elif token in operators:
                operators[token](stack)
        return stack
    except IndexError:
        print("Enter at least two numbers.")
    except ZeroDivisionError:
        print("Cannot divide by 0.")


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
    if len(sys.argv) > 1:
        result = calculator(sys.argv)
        if result == None:
            print("Try again!")
        else:
            print(*result)
    else:
        repl_standby()


# This is the standard boilerplate that calls the main() function.
# Do not modify this block.
if __name__ == "__main__":
    main()
