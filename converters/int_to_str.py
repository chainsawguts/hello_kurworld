def int_to_str(integer):
    num_string = ""
    
    if integer == 0:
        return 0
    
    is_negative = False
    if integer < 0:
        is_negative = True
        integer = -integer

    while integer > 0:
        digit = (integer % 10) + 48
        integer = integer // 10
        character = chr(digit)
        num_string =  character + num_string

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
