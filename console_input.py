

def val_mod(v):
    return v - 1


def int_input(log):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        try:
            value = int(input("Select a position...   "))
            if value not in nums:
                raise ValueError
            if (val_mod(value)) in log:
                raise ValueError
        except ValueError:
            print("Not an option! Try again.")
            continue
        else:
            break
    return value


def format_str_input(check):
    val = check.lower()
    return val[0]


def confirm_input(value):
    lets = ['y', 'n']
    while True:
        try:
            check = input(f'You entered: {value} continue? (y)es (n)o  ')
            val = format_str_input(check)
            if val not in lets:
                raise ValueError
        except ValueError:
            print("Not an option! Try again.")
            continue
        else:
            break
    return val


def player_input(log):
    value = ''
    val = -1
    check = ''
    value = int_input(log)

    check = confirm_input(value)

    val = val_mod(value)

    return val if check == 'y' else player_input(log)
