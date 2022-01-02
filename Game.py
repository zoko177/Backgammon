import pygame
import functions as fun
import pickle


class button():

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = 93
        self.height = 505

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

    def draw(self, win, outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)


def newgame(cont_game):
    game(cont_game)


def save_score(Board, Turn, BlackBase, WhiteBase, fun ):

    with open('score_save.pkl', 'rb') as input:
        arr = pickle.load(input)

    if Turn:
        arr[0] += fun.Score(Board, Turn, BlackBase, WhiteBase)
    else:
        arr[1] += fun.Score(Board, Turn, BlackBase, WhiteBase)

    with open('score_save.pkl', 'wb') as output:
        pickle.dump(arr, output, pickle.HIGHEST_PROTOCOL)

    fun.Score(Board, Turn, BlackBase, WhiteBase)


def boardUpdae(board, win, highlight1, highlight2, cube1, cube2):
    whites = pygame.image.load("WhiteStone.png")
    blacks = pygame.image.load("BlackStone.png")
    whitess = pygame.image.load("WhiteStoneS.png")
    blackss = pygame.image.load("BlackStoneS.png")
    backround = pygame.image.load("BoardGame.jpg")
    win.blit(backround, (0, 0))
    lgihtd = pygame.image.load("Highlight1.png")
    lightu = pygame.image.load("Highlight2.png")
    font = pygame.font.SysFont('comicsans', 60)


    bx = 1190 #Bot Side X start
    by = 955 #Bot side Y start
    tx = 110 #Top Side X start
    ty = 40 #Top Side Y start
    mx = 675 #Mid Side X start
    my = 540 #Mid Side Y start

    if cube1:

        dice1=pygame.image.load("Dice"+str(cube1)+".png")
        win.blit(dice1, (30,420))

    if cube2:
        dice2=pygame.image.load("Dice"+str(cube2)+".png")
        win.blit(dice2, (30,600))

    for i in range(12): #Update bot side of the board
        if i > 5:
            bx = 1190-45
        else:
            bx = 1190

        if i == highlight1 or i == highlight2:
            win.blit(lgihtd, (bx-20-i*94, by-300))

        if board[i] > 0:
            for j in range(board[i]):
                if j == 6:
                    text = font.render(('+'+str(board[i]-6)), 1, (255, 255, 255))
                    win.blit(text, (bx-i*94, by-j*90-5))
                    break
                win.blit(whites, (bx-i*94, by-j*90-5))
        elif board[i]<0:
            for j in range(board[i]*(-1)):
                if j == 6:
                    text = font.render(('+'+str(board[i]*(-1)-6)), 1, (0, 0, 0))
                    win.blit(text, (tx+30+(i-12)*94, ty+j*90-5))
                    break
                win.blit(blacks, (bx-i*94, by-j*90)) #


    for i in range(12,24): #Update bot side of the board
        if i > 17:
            tx = 110+45
        else:
            tx = 110
        if i == highlight1 or i == highlight2:
            pos = (tx - 25+(i - 12) * 94.5, ty-25)
            win.blit(lightu, pos)
        if board[i] > 0:
            for j in range(board[i]):
                if j == 6:
                    text = font.render(('+'+str(board[i]-6)), 1, (255, 255, 255))
                    win.blit(text, (tx+30+(i-12)*94, ty+j*90-5))
                    break
                win.blit(whites, (tx+(i-12)*94, ty+j*90-5))
        elif board[i] < 0:
            for j in range(board[i]*(-1)):
                if j == 6:
                    text = font.render(('+'+str(board[i]*(-1)-6)), 1, (0, 0, 0))
                    win.blit(text, (tx+30+(i-12)*94, ty+j*90-5))
                    break
                win.blit(blacks, (tx+(i-12)*94, ty+j*90))

    if board[24]:
        for i in range(board[24]):
            if i == 3:
                text = font.render(('+'+str((board[24] - 3))), 1, (255, 255, 255))
                win.blit(text, (mx, my + 50 * i))
                break
            pos = (mx, my + 50 * i)
            win.blit(whitess, pos)

    if board[25]:
        for i in range(1, board[25]*(-1)+1):
            if i == 4:
                text = font.render(('+'+str(board[25]*(-1) - 3)), 1, (0, 0, 0))
                win.blit(text, (mx, my - 50 * i))
                break
            pos = (mx, my - 50 * i)
            win.blit(blackss, pos)

    pygame.display.update()


def getpress(but ,board , turn):

    while 1:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:  # X on top right to exit

                with open('game_save.pkl', 'wb') as output:

                    pickle.dump(board, output, pickle.HIGHEST_PROTOCOL)
                    pickle.dump(turn, output, pickle.HIGHEST_PROTOCOL)



                run = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                for i in range(27):
                    if but[i].isOver(pos):
                        return i


def game(cont_game):

    pygame.init()
    win = pygame.display.set_mode((1386, 1080))
    pygame.display.set_caption("Backgammon")
    run = True

    if (cont_game):
        with open('game_save.pkl', 'rb') as input:
            Board = pickle.load(input)
            Turn = pickle.load(input)
    else:
        Board = [-2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, -5, 5, 0, 0, 0, -3, 0, -5, 0, 0, 0, 0, 2, 0, 0]
        Turn = 1

    boardUpdae(Board, win, -1, -1, 0, 0)
    but = [None]*27
    for i in range(6): #creating right side buttons
        but[i] = button(1192-i*93, 535, (0,0,0))
        but[23 - i] = button(1192-i*93, 30, (0, 0, 0))
    for i in range(6,12): #creating left side buttons
         but[i] = button(583-(i-6)*95, 535, (0,0,0))
         but[23 - i] = button(583-(i-6)*95, 30, (0,0,0))
    but[24] = button(680, 535, (255, 255, 255))
    but[25] = button(680, 35, (0, 255, 0))
    but[26] = button(1290, 30, (255, 255, 255))
    but[24].width = but[25].width = 45
    #but[24].height = but[25].height = 45
    but[26].width = 100
    but[26].height = 1010
    # for i in range(27):
    #     if but[i]:
    #         but[i].draw(win, None)
    pygame.display.update()
    White = 0  # score
    Black = 0  # score
    atararr = [0,0]

    while fun.GameOver(Board, Turn): #Game Handler
        if Turn == 1:  # white turn
            WhiteBase = [Board[0], Board[1], Board[2], Board[3], Board[4], Board[5]]
            BlackBase = [Board[18], Board[19], Board[20], Board[21], Board[22], Board[23]]
            if fun.CanRole(Turn, Board, WhiteBase, BlackBase):
                num = getpress(but, Board, Turn)
                Dice1, Dice2 = fun.RollDice()
                boardUpdae(Board, win, -1, -1, Dice1, Dice2)
                if Dice1 == Dice2:
                    click = 4
                else:
                    click = 2
                while click:
                    if fun.WinTime(Board, Turn):
                        movecomplete = 1
                        clicknum = click
                        lastBoard = list(Board)
                        while movecomplete:
                            if not fun.GameOver(Board, Turn):
                                movecomplete = 0
                                click = 0
                                save_score(Board, Turn, BlackBase, WhiteBase, fun)
                                return
                            num = getpress(but, Board, Turn)
                            #num = 5   must be from whitebase
                            if num < 6 and Board[num] > 0:
                                op1, op2 = fun.WhereToWin(Board, Dice1, Dice2, num, Turn)
                                start = num
                                boardUpdae(Board, win, op1, op2, Dice1, Dice2)
                                num = getpress(but, Board, Turn)
                                if num == -1:
                                    click += 1
                                    start = None
                                    break
                                elif num == op1:
                                    fun.MoveWin(Board, num, start, Turn)
                                    if click <= 2:
                                        Dice1 = 0
                                    start = None
                                    if lastBoard != Board:
                                        movecomplete = 0
                                        click -= 1
                                        boardUpdae(Board, win, -1, -1, Dice1, Dice2)
                                        break
                                elif num == op2:
                                    fun.MoveWin(Board, num, start, Turn)
                                    if click <= 2:
                                        Dice2 = 0
                                    start = None
                                    if lastBoard != Board:
                                        movecomplete = 0
                                        click -= 1
                                        boardUpdae(Board, win, -1, -1, Dice1, Dice2)
                                        break
                                boardUpdae(Board, win, op1, op2, Dice1, Dice2)
                    elif fun.Cadaver(Board, Turn):
                        movecomplete = 1
                        clicknum = click
                        lastBoard = list(Board)
                        while movecomplete:
                            num = getpress(but, Board, Turn)
                            if num == 24:  # must be from graveyard (24/25)
                                op1, op2 = fun.WhereTo(Board, Dice1, Dice2, num, Turn)
                                if op1 is None and op2 is None and movecomplete:
                                    movecomplete=0
                                    Dice1 = 0
                                    Dice2 = 0
                                    click = 0
                                    break
                                boardUpdae(Board, win, op1, op2, Dice1, Dice2)
                                start = num
                                num = getpress(but, Board, Turn)
                                if num == -1:
                                    click += 1
                                    start = None
                                    break
                                elif num == op1:
                                    fun.Move(Board, num, start, Turn)
                                    if click <= 2:
                                        Dice1 = 0
                                    start = None
                                    if lastBoard != Board:
                                        movecomplete = 0
                                        click -= 1
                                        boardUpdae(Board, win, -1, -1, Dice1, Dice2)
                                        break
                                elif num == op2:
                                    fun.Move(Board, num, start, Turn)
                                    if click <= 2:
                                        Dice2 = 0
                                    start = None
                                    if lastBoard != Board:
                                        movecomplete = 0
                                        click -= 1
                                        boardUpdae(Board, win, -1, -1, Dice1, Dice2)
                                        break

                                start = None
                                boardUpdae(Board, win, op1, op2, Dice1, Dice2)
                    else:
                        movecomplete = 1
                        clicknum=click
                        lastBoard = list(Board)
                        while movecomplete:
                            #lastBoard = Board
                            num = getpress(but, Board, Turn)
                            if Board[num] > 0:  # must be from graveyard (24/25)
                                op1, op2 = fun.WhereTo(Board, Dice1, Dice2, num, Turn)
                                start = num
                                boardUpdae(Board, win, op1, op2, Dice1, Dice2)
                                num = getpress(but, Board, Turn)
                                if num == -1:
                                    click += 1
                                    start = None
                                    break
                                elif num == op1:
                                    fun.Move(Board, num, start, Turn)
                                    if click <= 2:
                                        Dice1 = 0
                                    start = None
                                    if lastBoard != Board:
                                        movecomplete = 0
                                        click -= 1
                                        boardUpdae(Board, win, -1, -1, Dice1, Dice2)
                                        break
                                elif num == op2:
                                    fun.Move(Board, num, start, Turn)
                                    if click <= 2:
                                        Dice2 = 0
                                    start = None
                                    if lastBoard != Board:
                                        movecomplete = 0
                                        click -= 1
                                        boardUpdae(Board, win, -1, -1, Dice1, Dice2)
                                        break

                                start = None
                                boardUpdae(Board, win, op1, op2, Dice1, Dice2)
                                # if click==0:
                                #     break
                        # op1, op2 = fun.WhereTo(Board, Dice1, Dice2, num, Turn)  # check where we can rotate to
                        # fun.Move(Board, op1, num, Turn)
            Turn = 0

        if Turn == 0:  # black turn
            WhiteBase = [Board[0], Board[1], Board[2], Board[3], Board[4], Board[5]]
            BlackBase = [Board[18], Board[19], Board[20], Board[21], Board[22], Board[23]]
            if fun.CanRole(Turn, Board, WhiteBase, BlackBase):
                num = getpress(but, Board, Turn)
                Dice1, Dice2 = fun.RollDice()
                boardUpdae(Board, win, -1, -1, Dice1, Dice2)
                if Dice1 == Dice2:
                    click = 4
                else:
                    click = 2
                while click:
                    if fun.WinTime(Board, Turn):
                        movecomplete = 1
                        clicknum = click
                        lastBoard = list(Board)
                        while movecomplete:
                            if not fun.GameOver(Board, Turn):
                                movecomplete = 0
                                click = 0
                                save_score(Board, Turn, BlackBase, WhiteBase, fun)
                                return
                            num = getpress(but, Board, Turn)
                            if num > 17 and num < 24 and Board[num] < 0:
                                op1, op2 = fun.WhereToWin(Board, Dice1, Dice2, num, Turn)
                                start = num
                                boardUpdae(Board, win, op1, op2, Dice1, Dice2)
                                num = getpress(but, Board, Turn)
                                if num == -1:
                                    click += 1
                                    start = None
                                    break
                                elif num == op1:
                                    fun.Move(Board, num, start, Turn)
                                    if click <= 2:
                                        Dice1 = 0
                                    start = None
                                    if lastBoard != Board:
                                        movecomplete = 0
                                        click -= 1
                                        boardUpdae(Board, win, -1, -1, Dice1, Dice2)
                                        break
                                elif num == op2:
                                    fun.Move(Board, num, start, Turn)
                                    if click <= 2:
                                        Dice2 = 0
                                    start = None
                                    if lastBoard != Board:
                                        movecomplete = 0
                                        click -= 1
                                        boardUpdae(Board, win, -1, -1, Dice1, Dice2)
                                        break

                                start = None
                                boardUpdae(Board, win, op1, op2, Dice1, Dice2)
                    elif fun.Cadaver(Board, Turn):
                        movecomplete = 1
                        clicknum = click
                        lastBoard = list(Board)
                        while movecomplete:
                            num = getpress(but, Board, Turn)
                            if num == 25:  # must be from graveyard (24/25)
                                op1, op2 = fun.WhereTo(Board, Dice1, Dice2, num, Turn)
                                if op1 is None and op2 is None and movecomplete:
                                    movecomplete=0
                                    Dice1 = 0
                                    Dice2 = 0
                                    click = 0
                                    break
                                start = num
                                boardUpdae(Board, win, op1, op2, Dice1, Dice2)
                                num = getpress(but, Board, Turn)
                                if num == -1:
                                    click += 1
                                    start = None
                                    break
                                elif num == op1:
                                    fun.Move(Board, num, start, Turn)
                                    if click <= 2:
                                        Dice1 = 0
                                    start = None
                                    if lastBoard != Board:
                                        movecomplete = 0
                                        click -= 1
                                        boardUpdae(Board, win, -1, -1, Dice1, Dice2)
                                        break
                    else:
                        movecomplete = 1
                        clicknum = click
                        lastBoard = list(Board)
                        while movecomplete:
                            num = getpress(but, Board, Turn)
                            if Board[num] < 0:  # must be from graveyard (24/25)
                                op1, op2 = fun.WhereTo(Board, Dice1, Dice2, num, Turn)
                                start = num
                                boardUpdae(Board, win, op1, op2, Dice1, Dice2)
                                num = getpress(but, Board, Turn)
                                if num == -1:
                                    click += 1
                                    start = None
                                    boardUpdae(Board, win, -1, -1, Dice1, Dice2)
                                    break
                                elif num == op1:
                                    fun.Move(Board, num, start, Turn)
                                    if click <= 2:
                                        Dice1 = 0
                                    start = None
                                    if lastBoard != Board:
                                        movecomplete = 0
                                        click -= 1
                                        boardUpdae(Board, win, -1, -1, Dice1, Dice2)
                                        break
                                elif num == op2:
                                    fun.Move(Board, num, start, Turn)
                                    if click <= 2:
                                        Dice2 = 0
                                    start = None
                                    if lastBoard != Board:
                                        movecomplete = 0
                                        click -= 1
                                        boardUpdae(Board, win, -1, -1, Dice1, Dice2)
                                        break

                                start = None
                                boardUpdae(Board, win, op1, op2, Dice1, Dice2)
        Turn = 1

    save_score(Board, Turn, BlackBase, WhiteBase, fun)
    print(Black)  # black score
    print(White)  # white score
    return


