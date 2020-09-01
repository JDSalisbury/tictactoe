def check_for_victory(l):
    status = False
    winner = ""
    p1 = l[0]
    p2 = l[1]
    p3 = l[2]
    p4 = l[3]
    p5 = l[4]
    p6 = l[5]
    p7 = l[6]
    p8 = l[7]
    p9 = l[8]

    if p1 == p2 == p3:
        status = True
        winner = p1
    if p4 == p5 == p6:
        status = True
        winner = p4
    if p7 == p8 == p9:
        status = True
        winner = p7
    if p1 == p4 == p7:
        status = True
        winner = p1
    if p2 == p5 == p8:
        status = True
        winner = p2
    if p3 == p6 == p9:
        status = True
        winner = p3
    if p1 == p5 == p9:
        status = True
        winner = p1
    if p3 == p5 == p7:
        status = True
        winner = p3

    return status, winner
