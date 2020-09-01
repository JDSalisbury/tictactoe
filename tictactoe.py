MOVE_LIST = [" * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * "]


def show_board(ml):
    print(ml[0] + " | " + ml[1] + " | " + ml[2])
    print("____ _____ ____")
    print(ml[3] + " | " + ml[4] + " | " + ml[5])
    print("____ _____ ____")
    print(ml[6] + " | " + ml[7] + " | " + ml[8])


show_board(MOVE_LIST)
