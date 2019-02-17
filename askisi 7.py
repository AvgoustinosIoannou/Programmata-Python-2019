import random

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

#elegxoi gia niki
def check(board):
    w = 0
    for i in range(3):
        if (board[i - 1][0] == 1 and board[i - 1][1] == 1 and board[i - 1][2] == 1):
            w = 1
        elif ((board[i - 1][0] == 2 and board[i - 1][1] == 2 and board[i - 1][2] == 2)):
            w = 2
    for i in range(3):
        if (board[0][i - 1] == 1 and board[1][i - 1] == 1 and board[2][i - 1] == 1):
            w = 1
        elif ((board[0][i - 1] == 2 and board[1][i - 1] == 2 and board[2][i - 1] == 2)):
            w = 2
    if (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1):
        w = 1
    elif ((board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2)):
        w = 2
    if (board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1):
        w = 1
    elif ((board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2)):
        w = 2
    return w

p = 0
exit = 0
while (1):
#sinthiki gia eksodo
    if (exit == 1):
        break
#paizei o xristis
    play_grammi = raw_input("Dwse Grammi: ")
    play_stili = raw_input("Dwse Stili: ")
    x = int(play_grammi)
    y = int(play_stili)
    if (board[x - 1][y - 1] == 0):
        board[x - 1][y - 1] = 1
        p += 1
    else:
        print "Chose Another Move"
        continue
    win = check(board)
    if (win == 1):
        print "You Win!!!"
        break

    if (p == 9):
        print "Draw"
        break

#paizei o ipologistis
    while (1):
        r_grammi = random.randint(0, 2)
        r_stili = random.randint(0, 2)
        if (board[r_grammi][r_stili] == 0):
            board[r_grammi][r_stili] = 2
            p += 1
            print board[0]
            print board[1]
            print board[2]
            print p
#kalei sinartisi elegxou
            win = check(board)
            if (win == 2):
                print "Computer Wins!!!"
                exit = 1
                break

            if (p == 9):
                print "Draw"
                break
            break

print board[0]
print board[1]
print board[2]