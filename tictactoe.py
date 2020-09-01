from win_cons import check_for_victory
from console_input import player_input
MOVE_LIST = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]


def show_board(ml):
    line = "____ _____ ____"
    bar = " | "
    print(ml[0] + bar + ml[1] + bar + ml[2])
    print(line)
    print(ml[3] + bar + ml[4] + bar + ml[5])
    print(line)
    print(ml[6] + bar + ml[7] + bar + ml[8])


def update_board(ml, choice):
    ml[choice] = " X "
    return ml


show_board(MOVE_LIST)
victory = False
winner = ''
turn_log = []
while(victory == False):
    print("   ")

    choice = player_input(turn_log)

    turn_log.append(choice)

    uml = update_board(MOVE_LIST, choice)
    print("   ")
    victory, winner = check_for_victory(uml)

    show_board(uml)


print(winner, " is the winner!")
