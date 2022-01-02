import random
import pickle


def GameOver(board, turn):

    if turn:  # the opposite
        for i in range(25):
            if board[i] > 0:
                return 1
        return 0
    if not turn:
        for i in board:
            if board[i] < 0:
                return 1
        return 0


def ScorePressed():
    with open('score_save.pkl', 'rb') as input:
        arr = pickle.load(input)
    print('White Score' + arr[0])
    print('Black Score' + arr[1])


def CanRole(turn, board, white, black):
    if turn:  # White's turn
        if board[24] >= 1 and max(black) <= -2:
            return 0
        return 1

    if not turn:  #Black's turn
        if board[25] <= -1 and min(white) >= 2:
            return 0
        return 1


def RollDice():
    min = 1
    max = 6
    return random.randint(min, max), random.randint(min, max)


def Cadaver(board, turn):
     if turn:
         if board[24] > 0:
             return 1
         return 0

     if not turn:
         if board[25] < 0:
             return 1
         return 0


def WhereTo(board, dice1, dice2, n, turn):
    if turn:  #white's turn

        if dice1 == 0:
            op1 = None
        else:
            if board[n - dice1] < -1 or (n - dice1) < 0:
                op1 = None
            else:
                op1 = n - dice1
        if dice2 == 0:
            op2 = None
        else:
            if board[n - dice2] < -1 or (n - dice2) < 0:
                op2 = None
            else:
                op2 = n - dice2

    if not turn:  #black's turn
        if n == 25:
            if dice1 == 0:
                op1 = None
            else:
                if board[dice1 - 1] > 1:
                    op1 = None
                else:
                    op1 = dice1 - 1
            if dice2 == 0:
                op2 = None
            else:
                if board[dice2 - 1] > 1:
                    op2 = None
                else:
                    op2 = dice2 - 1
        else:
            if dice1 == 0:
                op1 = None
            else:
                if board[n + dice1] > 1 or (n + dice1) > 23:
                    op1 = None
                else:
                    op1 = n + dice1
            if dice2 == 0:
                op2 = None
            else:
                if board[n + dice2] > 1 or (n + dice2) > 23:
                    op2 = None
                else:
                    op2 = n + dice2

    return op1, op2


def Move(board, end, start, turn):

    if turn:  # White's turn
        if end is None:
            return 1
        elif board[end] == -1:
            board[start] -= 1
            board[end] += 2
            board[25] -= 1
        else:
            board[start] -= 1
            board[end] += 1

    if not turn:  # black's turn
        if end is None:
            return 1
        elif board[end] == 1:
            board[start] += 1
            board[end] -= 2
            board[24] += 1
        else:
            board[start] += 1
            board[end] -= 1


def WinTime(board, turn):

    if turn:
        for i in range(6, 25):
            if board[i] > 0:
                return 0
        return 1
    if not turn:

        for i in range(18):
            if board[i] < 0 or board[25] < 0:
                return 0
        return 1


def WhereToWin(board, dice1, dice2, n, turn):

    if turn:
        if dice1 == 0:
            op1 = None
        else:
            if n - dice1 >= 0:
                if board[n - dice1] < -1:
                    op1 = None
            if (n - dice1) <= 0:  #  need 2 check for biger index
                op1 = 26
            else:
                op1 = n - dice1

        if dice2 == 0:
            op2 = None
        else:
            if n - dice2 >= 0:
                if board[n - dice2] < -1:
                    op2 = None
            if (n - dice2) <= 0:  # need 2 check for biger index
                op2 = 26
            else:
                op2 = n - dice2

    if not turn:
        if dice1 == 0:
            op1 = None
        else:
            if n + dice1 >= 18 and n +dice1 <= 23:
                if board[n + dice1] > 1:
                    op1 = None
            elif (n + dice1) > 23:  #  need 2 check for biger index
                op1 = 26
            else:
                op1 = n + dice1

        if dice2 == 0:
            op2 = None
        else:
            if n + dice2 >= 18 and n +dice2 <= 23:
                if board[n + dice2] > 1:
                    op2 = None
            elif (n + dice2) > 23:  # need 2 check for biger index
                op2 = 26
            else:
                op2 = n + dice2
    return op1, op2


def MoveWin(board, end, start, turn):

    if turn:  # White's turn
        if end is None:
            return 1
        elif end == 26:
            board[start] -= 1
        elif board[end] == -1:
            board[start] -= 1
            board[end] += 2
            board[25] -= 1
        else:
            board[start] -= 1
            board[end] += 1

    if not turn:  # black's turn
        if end is None:
            return 1
        elif end == 26:
            board[start] += 1
        elif board[end] == 1:
            board[start] += 1
            board[end] -= 2
            board[24] += 1
        else:
            board[start] += 1
            board[end] -= 1


def Score(Board, Turn, BlackBase, WhiteBase):
    if Turn:  # black won
        count = 0
        flag = 0
        for i in range(25):
            if Board[i] > 0:
                count += Board[i]
        for i in BlackBase:
            if BlackBase[i] > 0:
                flag = 1
        if Board[24] > 0 and count == 15 and flag:
            return 5
        elif Board[24] > 0 and count == 15:  # stars mars
            return 4
        elif flag and count == 15:  # turkish mars
            return 3
        elif count == 15:  # mars
            return 2
        else:
            return 1  # normal

    if not Turn:  # white won
        count = 0
        flag = 0
        for i in range(26):
            if Board[i] < 0:
                count += Board[i]
        for i in WhiteBase:
            if WhiteBase[i] < 0:
                Flag = 1
        if Board[25] < 0 and count == -15 and flag:
            return 5
        elif Board[25] < 0 and count == -15:  # stars mars
            return 4
        elif flag and count == -15:  # turkish mars
            return 3
        elif count == -15:  # mars
            return 2
        else:
            return 1  # normal
