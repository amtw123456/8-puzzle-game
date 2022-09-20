import pygame
import random
import time
import os

WINDOW_SCREEN_WIDTH = 510
WINDOW_SCREEN_HEIGHT = 510

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (230, 230, 230)

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

    def moveTiles(self):
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

        elif(direction == 1):
            for i in range(34):
                self.posX -= 5
                self.rect.x -= 5
                time.sleep(0.02)
                self.surface.blit(self.tileImage, (self.posX, self.posY))
                pygame.display.update()

        elif(direction == 2):
            for i in range(34):
                self.posY += 5
                self.rect.y += 5
                time.sleep(0.02)
                self.surface.blit(self.tileImage, (self.posX, self.posY))
                pygame.display.update()

        elif(direction == 3):
            for i in range(34):
                self.posX += 5
                self.rect.x += 5
                time.sleep(0.02)
                self.surface.blit(self.tileImage, (self.posX, self.posY))
                pygame.display.update()

        # self.rect.y += 5

    def tileClicked(self, cursorPosX, cursorPosY):
        if(self.rect.collidepoint((cursorPosX, cursorPosY))):
            # print("Tile:", self.tileNumber)
            # self.moveTile(0)
            return self.tileNumber
        # if ((self.sizeOfTile * counterX) < cursorPosX and (self.sizeOfTile * counterY) < cursorPosY) and (
        #     (self.sizeOfTile * counterX) < cursorPosX and ((self.sizeOfTile * counterY) + self.sizeOfTile) > cursorPosY) and (
        #     ((self.sizeOfTile * counterX)  + self.sizeOfTile) > cursorPosX and (self.sizeOfTile * counterY) < cursorPosY) and (
        #     ((self.sizeOfTile * counterX)  + self.sizeOfTile) > cursorPosX and ((self.sizeOfTile * counterY) + self.sizeOfTile) > cursorPosY):

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
    GRID.drawGrid()
    GRID.drawTiles()
    # GRID.moveTiles()
    pygame.display.update()

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def main():
    clock = pygame.time.Clock()
    rows = 3
    size = WINDOW_SCREEN_WIDTH
    distanceBetweenGrids = WINDOW_SCREEN_WIDTH // rows
    tileSize = distanceBetweenGrids
    window = pygame.display.set_mode((WINDOW_SCREEN_WIDTH*2, WINDOW_SCREEN_HEIGHT))
    # arrayOfNumbers = list(split(random.sample(range(0, 9), 9), 3))
    arrayOfNumbers = [[1,2,3],[4,0,6],[7,5,8]]
    print(arrayOfNumbers)
    correctPos = [[1,2,3],[4,5,6],[7,8,0]]
    tiles = []

    for i in range(rows):
        for j in range(rows):
            if arrayOfNumbers[i][j] == 0:
                tiles.append(None)
            else:
                tiles.append(Tile(tileSize * j, tileSize * i, tileSize, arrayOfNumbers[i][j], window))
    print(tiles)

    GRID = Grid(window, tiles, rows, size)

    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                cursorPosX, cursorPosY = pygame.mouse.get_pos()
                for i in range(len(tiles)):
                    if tiles[i] == None:
                        continue
                    else:
                        if(str(tiles[i].tileClicked(cursorPosX, cursorPosY)).isdigit()):
                            number = tiles[i].tileClicked(cursorPosX, cursorPosY)
                            x, y = getTileIndex(number, arrayOfNumbers, rows)
                            # print(arrayOfNumbers[x][y], arrayOfNumbers[x + 1][y]) # go down
                            print(x, y)
                            print(arrayOfNumbers[x][y], arrayOfNumbers[x - 1][y]) # go down
                            display2dArray(arrayOfNumbers, rows)
                            try:
                                if(arrayOfNumbers[x + 1][y] == 0):
                                    arrayOfNumbers[x + 1][y] = number
                                    arrayOfNumbers[x][y] = 0
                                    tiles[i].moveTile(2)
                            except(IndexError):
                                pass
                            try:
                                if(arrayOfNumbers[x - 1][y] == 0):
                                    print("Red")
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
                                if(arrayOfNumbers[x][y - 1] == 0):
                                    arrayOfNumbers[x][y - 1] = number
                                    arrayOfNumbers[x][y] = 0
                                    tiles[i].moveTile(1)
                            except(IndexError):
                                pass
                                # elif(arrayOfNumbers[x][y - 1] == 0):
                                #     arrayOfNumbers[x][y - 1] = number
                                #     arrayOfNumbers[x][y] = 0
                                #     tiles[i].moveTile(0)


                            display2dArray(arrayOfNumbers, rows)
                            break




        draw(window, size, rows, tiles, GRID)

main()
