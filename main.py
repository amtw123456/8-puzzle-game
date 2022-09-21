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

pygame.font.init()
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

# class NODE:
#     def __init__(self, nodeNumber, arrayList):
#         self.nodeNumber = nodeNumber
#         self.arrayList = arrayList
#         self.parentNode = None
#         self.rightNode = None
#         self.leftNode = None
#         self.downNode = None
#         self.upNode = None
#
#     def setUpNode(self):
#         pass
#
#     def setDownNode(self):
#         pass
#
#     def setRightNode(self):
#         pass
#
#     def setLeftNode(self):
#         pass

# def BFSearch(arrayList):
#     goalState = [[1,2,3],[4,5,6],[7,8,0]]
#     frontier = [NODE(0,arrayList)]
#     while(len(frontier) != 0):
#         if(frontier.pop().arrayList == goalState):
#             print("yess")

class ButtonClass:
    def __init__(self, x, y, width, height, buttonColor, buttonColorHover, buttonText = ""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.clicked = False
        self.buttonColor = buttonColor
        self.buttonColorHover = buttonColorHover
        self.rect = pygame.Rect(x, y, width, height)
        textFont = pygame.font.Font("freesansbold.ttf",20)
        self.textRender = textFont.render(buttonText, True, COLOR_BLACK, None)

    def drawButton(self, surface):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            pygame.draw.rect(surface, self.buttonColorHover, self.rect)
            surface.blit(self.textRender, (self.x+self.width/3, self.y+self.height/4))
            return True

        else:
            pygame.draw.rect(surface, self.buttonColor, self.rect)
            surface.blit(self.textRender, (self.x+self.width/3, self.y+self.height/4))

        return False

class TextClass:
    def __init__(self, x = 0, y = 0, width = 50, height = 50, text = "", textSize = 16, textColor = COLOR_BLACK, textBackgroundColor = COLOR_GRAY):
        self.textFont = pygame.font.Font('freesansbold.ttf', textSize)
        self.textRender = self.textFont.render(text, True, textColor, textBackgroundColor)
        self.textRect = self.textRender.get_rect()
        self.textRect.x = x
        self.textRect.y = x
        self.textRect.width = width
        self.textRect.height = height

    def blitText(self, surface, x, y):
         surface.blit(self.textRender , (x, y))

    def blitTextRect(self, surface, x, y):
        pass


def main():
    arrayOfNumbers = readFile()
    tileNotArrangedText = TextClass(100, 100, 100, 50, "Tiles are not arranged!", 32)
    winText = TextClass(100, 100, 100, 50, 'All the tiles are in place!', 32)
    solvableText = TextClass(100, 100, 100, 50, 'The puzzle is Solvable!: ' + str(isSolvable(arrayOfNumbers)), 26)
    quitButton = ButtonClass(680, 300, 140, 40, COLOR_PASTELYELLOW, COLOR_AMBER, "QUIT")
    # bfsButton = ButtonClass(545, 400, 130, 40, COLOR_PASTELYELLOW, COLOR_AMBER, "BFS")
    # dfsButton = ButtonClass(685, 400, 130, 40, COLOR_PASTELYELLOW, COLOR_AMBER, "DFS")
    # nextButton = ButtonClass(825, 400, 130, 40, COLOR_PASTELYELLOW, COLOR_AMBER, "NEXT")
    clock = pygame.time.Clock()

    size = WINDOW_SCREEN_WIDTH
    rows = 3

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
            tileNotArrangedText.blitText(window, 580, 200)
            solvableText.blitText(window, 580, 100)
            cursorPosX, cursorPosY = pygame.mouse.get_pos()
            quitButton.drawButton(window)
            # bfsButton.drawButton(window)
            # dfsButton.drawButton(window)
            # nextButton.drawButton(window)
            pygame.display.update()

            if event.type == pygame.QUIT:
                exit()
            if pygame.mouse.get_pressed()[0] == 1:
                if(quitButton.drawButton(window)):
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
                                winText.blitText(window, 580, 200)
                                pygame.display.update()
                                time.sleep(3)
                                exit()
                            break

        draw(window, size, rows, tiles, GRID)
main()
