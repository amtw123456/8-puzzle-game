import pygame
import random
import time
import os

WINDOW_SCREEN_WIDTH = 510
WINDOW_SCREEN_HEIGHT = 510

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE= (255, 255, 255)

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
                self.tiles[i].drawTile(self.surface)


class Tile(object):
    def __init__(self, posX, posY, sizeOfTile, tileNumber):
        self.posX = posX
        self.posY = posY
        self.sizeOfTile = sizeOfTile
        self.tileNumber = tileNumber
        self.tileImage = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'number' + str(tileNumber) + '.png')), (sizeOfTile, sizeOfTile))

    def drawTile(self, surface):
        surface.blit(self.tileImage, (self.posX, self.posY))


def draw(surface, gridDistance, rows, tiles, GRID):
    surface.fill(COLOR_WHITE)
    GRID.drawGrid()
    GRID.drawTiles()
    pygame.display.update()

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def main():

    rows = 3
    size = WINDOW_SCREEN_WIDTH
    distanceBetweenGrids = WINDOW_SCREEN_WIDTH // rows
    tileSize = distanceBetweenGrids
    window = pygame.display.set_mode((WINDOW_SCREEN_WIDTH*2, WINDOW_SCREEN_HEIGHT))
    arrayOfNumbers = list(split(random.sample(range(0, 9), 9), 3))
    # arrayOfNumbers = [[1,2,3],[4,5,6],[7,0,8]]
    print(arrayOfNumbers)
    correctPos = [[1,2,3],[4,5,6],[7,8,0]]
    tiles = []

    for i in range(rows):
        for j in range(rows):
            if arrayOfNumbers[i][j] == 0:
                tiles.append(None)
            else:
                tiles.append(Tile(tileSize * j, tileSize * i, tileSize, arrayOfNumbers[i][j]))
    print(tiles)

    GRID = Grid(window, tiles, rows, size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        draw(window, size, rows, tiles, GRID)

main()
