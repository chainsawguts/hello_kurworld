def str_to_int(string):
    character_list = list(string)

    is_negative = False
    if character_list[0] == "-":
        is_negative = True
        character_list = character_list[1:]

    result = 0
    for element in character_list:
        if element.isdigit():
            unicode = ord(element)
            digit = unicode - 48
            result = result * 10 + digit
        else:
            return "Invalid number."

    if is_negative == True:
        result *= -1
    return result


while True:
    string = input("Your string: ")
    conversion = str_to_int(string)
    print(f"Your integer: {conversion}")
