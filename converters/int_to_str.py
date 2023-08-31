def int_to_str(integer):
    num_string = ""
    digit_list = []

    is_negative = False
    if integer < 0:
        is_negative = True
        integer = abs(integer)

    while integer > 0:
        digit = integer % 10
        integer = integer // 10
        digit_list.insert(0, digit + 48)

    while digit_list:
        character = chr(digit_list.pop(0))
        num_string += character

    if is_negative == True:
        num_string = "-" + num_string
    return num_string


while True:
    try:
        integer = int(input("Your integer: "))
        conversion = int_to_str(integer)
        print(f"Your string: {conversion}")
    except ValueError:
        print("Enter a valid number.")
