from console_input import player_input
from win_cons import check_for_victory, announce_winner
MOVE_LIST = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]


def show_board(ml):
    line = "____ _____ ____"
    bar = " | "
    print(ml[0] + bar + ml[1] + bar + ml[2])
    print(line)
    print(ml[3] + bar + ml[4] + bar + ml[5])
    print(line)
    print(ml[6] + bar + ml[7] + bar + ml[8])


def update_board(ml, choice, player):
    ml[choice] = player
    return ml


def player_turn(log, player):
    print("   ")

    choice = player_input(log)
    uml = update_board(MOVE_LIST, choice, player)
    vic, win = check_for_victory(uml)
    print("   ")

    return choice, uml, vic, win


def set_game_info(game_info, choice, uml, vic, win):
    game_info['turn_log'].append(choice)
    game_info['victory'] = vic
    game_info['winner'] = win

    show_board(uml)

    announce_winner(game_info['winner'])
