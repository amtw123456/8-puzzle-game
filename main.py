import pygame
import random
import time
import os

WINDOW_SCREEN_WIDTH = 510
WINDOW_SCREEN_HEIGHT = 510

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (230, 230, 230)
COLOR_BLUE = (0, 0, 255)
COLOR_AMBER = (255, 191, 0)
COLOR_PASTELYELLOW = (253,253,150)

pygame.display.set_caption("8-Puzzle Game")

class Grid(object):
    def __init__(self, surface, tiles, rows, gridSize):
        self.gridSize = gridSize
        self.surface = surface
        self.tiles = tiles
        self.rows = rows

    def drawGrid(self):
        sizeBtwn = self.gridSize // self.rows

        x = 0
        y = 0

        for l in range(self.rows):
            x = x + sizeBtwn
            y = y + sizeBtwn

            pygame.draw.line(self.surface, COLOR_BLACK, (x, 0), (x, self.gridSize))
            pygame.draw.line(self.surface, COLOR_BLACK, (0, y), (self.gridSize, y))

    def drawTiles(self):
        for i in range(len(self.tiles)):
            if self.tiles[i] == None:
                continue
            else:
                self.tiles[i].drawTile()

    def moveTiles(self): # optional
        for i in range(len(self.tiles)):
            if self.tiles[i] == None:
                continue
            else:
                self.tiles[i].moveTile()

class Tile(object):
    def __init__(self, posX, posY, sizeOfTile, tileNumber, surface):
        self.posX = posX
        self.posY = posY
        self.surface = surface
        self.sizeOfTile = sizeOfTile
        self.tileNumber = tileNumber
        self.rect = pygame.draw.rect(surface, (0, 0, 0), (posX, posY, sizeOfTile, sizeOfTile))
        self.tileImage = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'number' + str(tileNumber) + '.png')), (sizeOfTile, sizeOfTile))

    def drawTile(self):
        self.surface.blit(self.tileImage, (self.posX, self.posY))

    def moveTile(self, direction):
        if(direction == 0):
            for i in range(34):
                self.posY -= 5
                self.rect.y -= 5
                time.sleep(0.02)
                self.surface.blit(self.tileImage, (self.posX, self.posY))
                pygame.display.update()
            time.sleep(0.05)

        elif(direction == 1):
            for i in range(34):
                self.posX -= 5
                self.rect.x -= 5
                time.sleep(0.02)
                self.surface.blit(self.tileImage, (self.posX, self.posY))
                pygame.display.update()
            time.sleep(0.05)

        elif(direction == 2):
            for i in range(34):
                self.posY += 5
                self.rect.y += 5
                time.sleep(0.02)
                self.surface.blit(self.tileImage, (self.posX, self.posY))
                pygame.display.update()
            time.sleep(0.05)

        elif(direction == 3):
            for i in range(34):
                self.posX += 5
                self.rect.x += 5
                time.sleep(0.02)
                self.surface.blit(self.tileImage, (self.posX, self.posY))
                pygame.display.update()
            time.sleep(0.05)

    def tileClicked(self, cursorPosX, cursorPosY):
        if(self.rect.collidepoint((cursorPosX, cursorPosY))):
            return self.tileNumber

def getTileIndex(tileNumber, arrayList, rows):
    for i in range(rows):
        for j in range(rows):
            if(arrayList[i][j] == tileNumber):
                return i, j
                break

def display2dArray(arrayList, rows):
    for i in range(rows):
        for j in range(rows):
            print(arrayList[i][j], end=" ")
        print()
    print()

def draw(surface, gridDistance, rows, tiles, GRID):
    surface.fill(COLOR_GRAY)
    GRID.drawTiles()
    GRID.drawGrid()

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def readFile():
    f = open("puzzle.in", "r")
    Lines = f.readlines()
    inList = []

    for i in range(len(Lines)):
        splitArray = Lines[i].split()
        tempList = []
        for j in range(len(splitArray)):
            tempList.append(int(splitArray[j]))
        inList.append(tempList)

    return inList

def getInvCount(array2d):
    inv_count = 0
    empty_value = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if array2d[j] != empty_value and array2d[i] != empty_value and array2d[i] > array2d[j]:
                inv_count += 1
    return inv_count

def isSolvable(puzzle) :
    inv_count = getInvCount([j for sub in puzzle for j in sub])
    return (inv_count % 2 == 0)

def main():
    arrayOfNumbers = readFile()
    pygame.font.init()

    tileNotArrangedFont = pygame.font.Font('freesansbold.ttf', 32)
    myWinFont = pygame.font.Font('freesansbold.ttf', 32)
    mySolvableFont =  pygame.font.Font('freesansbold.ttf', 26)
    smallFont = pygame.font.Font('freesansbold.ttf',16)
    tileNotArrangedText = tileNotArrangedFont.render('Tiles are not arranged!', True, COLOR_BLACK, COLOR_GRAY)
    winText = myWinFont.render('All the tiles are in place!', True, COLOR_BLACK, COLOR_GRAY)
    solvableText = mySolvableFont.render('The puzzle is Solvable!: ' + str(isSolvable(arrayOfNumbers)), True, COLOR_BLACK, COLOR_GRAY)
    quitText = smallFont.render('QUIT' , True , COLOR_BLACK)
    quitTextRect = quitText.get_rect()
    quitTextRect.x = 680
    quitTextRect.y = 300
    quitTextRect.height = 40
    quitTextRect.width = 140
    winTextRect = winText.get_rect()
    solvableTextRect = solvableText.get_rect()
    tileNotArrangedTextRect = tileNotArrangedText.get_rect()

    clock = pygame.time.Clock()
    rows = 3
    size = WINDOW_SCREEN_WIDTH
    distanceBetweenGrids = WINDOW_SCREEN_WIDTH // rows
    tileSize = distanceBetweenGrids
    window = pygame.display.set_mode((WINDOW_SCREEN_WIDTH*2, WINDOW_SCREEN_HEIGHT))

    correctPos = [[1,2,3],[4,5,6],[7,8,0]]
    tiles = []

    for i in range(rows):
        for j in range(rows):
            if arrayOfNumbers[i][j] == 0:
                tiles.append(None)
            else:
                tiles.append(Tile(tileSize * j, tileSize * i, tileSize, arrayOfNumbers[i][j], window))

    GRID = Grid(window, tiles, rows, size)

    while True:
        clock.tick(30)
        for event in pygame.event.get():
            window.blit(tileNotArrangedText, (580, 200))
            window.blit(solvableText, (580, 100))
            cursorPosX, cursorPosY = pygame.mouse.get_pos()
            if(quitTextRect.collidepoint(cursorPosX, cursorPosY)):
                pygame.draw.rect(window, COLOR_AMBER,[680,300,140,40])
            else:
                pygame.draw.rect(window, COLOR_PASTELYELLOW,[680,300,140,40])
            window.blit(quitText , (730,313))
            pygame.display.update()

            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if(quitTextRect.collidepoint(cursorPosX, cursorPosY)):
                    exit()
                for i in range(len(tiles)):
                    if tiles[i] == None:
                        continue
                    else:
                        if(str(tiles[i].tileClicked(cursorPosX, cursorPosY)).isdigit()):
                            number = tiles[i].tileClicked(cursorPosX, cursorPosY)
                            x, y = getTileIndex(number, arrayOfNumbers, rows)
                            try:
                                if(arrayOfNumbers[x + 1][y] == 0):
                                    arrayOfNumbers[x + 1][y] = number
                                    arrayOfNumbers[x][y] = 0
                                    tiles[i].moveTile(2)
                            except(IndexError):
                                pass
                            try:
                                if(arrayOfNumbers[x - 1][y] == 0 and x - 1 >= 0): #
                                    arrayOfNumbers[x - 1][y] = number
                                    arrayOfNumbers[x][y] = 0
                                    tiles[i].moveTile(0)
                            except(IndexError):
                                pass
                            try:
                                if(arrayOfNumbers[x][y + 1] == 0):
                                    arrayOfNumbers[x][y + 1] = number
                                    arrayOfNumbers[x][y] = 0
                                    tiles[i].moveTile(3)
                            except(IndexError):
                                pass
                            try:
                                if(arrayOfNumbers[x][y - 1] == 0 and y - 1 >= 0): #
                                    arrayOfNumbers[x][y - 1] = number
                                    arrayOfNumbers[x][y] = 0
                                    tiles[i].moveTile(1)
                            except(IndexError):
                                pass
                            if(correctPos == arrayOfNumbers):
                                window.blit(winText, (580, 200))
                                pygame.display.update()
                                time.sleep(3)
                                exit()
                            break

        # if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        #     pygame.draw.rect(window,COLOR_WHITE,[width/2,height/2,140,40])
        # else:

        draw(window, size, rows, tiles, GRID)
main()
