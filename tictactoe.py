from win_cons import check_for_victory
MOVE_LIST = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]


def show_board(ml):
    line = "____ _____ ____"
    bar = " | "
    print(ml[0] + bar + ml[1] + bar + ml[2])
    print(line)
    print(ml[3] + bar + ml[4] + bar + ml[5])
    print(line)
    print(ml[6] + bar + ml[7] + bar + ml[8])


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
winner = ''
while(victory == False):
    print("   ")
    choice = player_input()

    uml = update_board(MOVE_LIST, choice)
    print("   ")
    victory, winner = check_for_victory(uml)

    show_board(uml)


print(winner, " is the winner!")
