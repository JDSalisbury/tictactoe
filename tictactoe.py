
from game_mechanics import show_board, player_turn, MOVE_LIST, set_game_info


show_board(MOVE_LIST)

game_info = {
    'victory': False,
    'winner': '',
    'turn_log': [],
    'player_one': ' X ',
    'player_two': ' O ',
}

while(game_info['victory'] == False):

    choice, uml, vic, win = player_turn(
        game_info['turn_log'], game_info['player_one'])

    set_game_info(game_info, choice, uml, vic, win)

    if game_info['winner']:
        break

    # player two

    choice, uml, vic, win = player_turn(
        game_info['turn_log'], game_info['player_two'])

    set_game_info(game_info, choice, uml, vic, win)
