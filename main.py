import pygame
import Game
import functions as fun


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, self.color)
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


def mainmenubuttons():
    newgameBut.draw(win, (0, 0, 0))
    resumeBut.draw(win, (0, 0, 0))
    bestBut.draw(win, (0, 0, 0))
    quitBut.draw(win, (0, 0, 0))


def mainbumoi(x):#Mouse over changing color to red from white
    a = (255, 0, 0)
    b = (255, 255, 255)
    if x:
        return a, b, b, b
    else:
        return b, b, b, b


pygame.init()

win = pygame.display.set_mode((1386, 1080))

pygame.display.set_caption("Backgammon")
run = True
backround = pygame.image.load("MainMenue.jpg")
win.blit(backround, (0, 0))
newgameBut = button((255, 255, 255), 575, 300, 250, 150, 'New Game')
resumeBut = button((255, 255, 255), 575, 420, 250, 150, 'Resume')
bestBut = button((255, 255, 255), 575, 570, 250, 150, 'Best Score')
quitBut = button((255, 255, 255), 575, 720, 250, 150, 'Quit')

while run:
    mainmenubuttons()
    pygame.display.update()
    #pygame.time.delay(100)
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT: #X on top right to exit
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEMOTION: #Mouse over changing color to red from white
            if newgameBut.isOver(pos):
                newgameBut.color, resumeBut.color, bestBut.color, quitBut.color = mainbumoi(1)
            elif resumeBut.isOver(pos):
                resumeBut.color, newgameBut.color, bestBut.color, quitBut.color = mainbumoi(1)
            elif bestBut.isOver(pos):
                bestBut.color, newgameBut.color, resumeBut.color, quitBut.color = mainbumoi(1)
            elif quitBut.isOver(pos):
                quitBut.color, bestBut.color, newgameBut.color, resumeBut.color = mainbumoi(1)
            else:
                newgameBut.color, resumeBut.color, bestBut.color, quitBut.color = mainbumoi(0)

        if event.type == pygame.MOUSEBUTTONUP:
            if quitBut.isOver(pos):
                run = False
                pygame.quit()
                quit()
            elif newgameBut.isOver(pos):
                run = False
                pygame.quit()
                Game.newgame(False)
                break
            elif resumeBut.isOver(pos):
                Game.newgame(True)
            elif bestBut.isOver(pos):
                fun.ScorePressed()
