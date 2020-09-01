MOVE_LIST = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]


def show_board(ml):
    print(ml[0] + " | " + ml[1] + " | " + ml[2])
    print("____ _____ ____")
    print(ml[3] + " | " + ml[4] + " | " + ml[5])
    print("____ _____ ____")
    print(ml[6] + " | " + ml[7] + " | " + ml[8])


def player_input():
    value = input("Select a position...")
    check = input(f'You entered: {value} continue? (y)es (n)o  ')
    val = int(value) - 1

    return val if check == 'y' else player_input()


def update_board(ml, choice):
    ml[choice] = " X "
    return ml


show_board(MOVE_LIST)
victory = False

while(victory == False):
    choice = player_input()

    uml = update_board(MOVE_LIST, choice)

    show_board(uml)
