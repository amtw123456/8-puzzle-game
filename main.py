from copy import copy, deepcopy
from tkinter import *
from tkinter import messagebox
import collections
import pygame
import random
import time
import os

Tk().wm_withdraw()

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

    def setButtonColor(self, buttonColor):
        self.buttonColor = buttonColor


class TextClass:
    def __init__(self, x = 0, y = 0, width = 50, height = 50, text = "", textSize = 16, textColor = COLOR_BLACK, textBackgroundColor = COLOR_GRAY):
        self.text = text
        self.textSize = textSize
        self.textColor = COLOR_BLACK
        self.textFont = pygame.font.Font('freesansbold.ttf', textSize)
        self.textRender = self.textFont.render(self.text, True, textColor, textBackgroundColor)
        self.textRect = self.textRender.get_rect()
        self.textRect.x = x
        self.textRect.y = x
        self.textRect.width = width
        self.textRect.height = height
        self.textBackgroundColor = textBackgroundColor

    def blitText(self, surface, x, y):
         surface.blit(self.textRender , (x, y))

    def setText(self, text):
        self.text = text
        self.textFont = pygame.font.Font('freesansbold.ttf', self.textSize)
        self.textRender = self.textFont.render("Steps: " + ' '.join(self.text), True, self.textColor, self.textBackgroundColor)


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

class NODE:
    def __init__(self, nodeNumber, nodeListState):
        self.nodeListState = nodeListState
        self.nodeNumber = nodeNumber
        self.parentNode = None
        self.rightNode = None
        self.downNode = None
        self.leftNode = None
        self.upNode = None
        self.action = None

    def printNodeInfo(self):
        print("===================================================")
        print("Current node value:", self.value)
        if self.parentNode == None:
            print("Current parent node value:", self.parentNode)
        else:
            print("Current parent node value:", self.parentNode.value)
        if self.rightNode == None:
            print("Current right node value:", self.rightNode)
        else:
            print("Current right node value:", self.rightNode.value)
        if self.downNode == None:
            print("Current down node value:", self.downNode)
        else:
            print("Current down node value:", self.downNode.value)
        if self.leftNode == None:
            print("Current left node value:", self.leftNode)
        else:
            print("Current left node value:", self.leftNode.value)
        if self.upNode == None:
            print("Current up node value:", self.upNode)
        else:
            print("Current up node value:", self.upNode.value)
        print("Current node array list state:", self.nodeListState)
        print("===================================================")

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

def getZeroIndex(arrayList, rows):
    for i in range(rows):
        for j in range(rows):
            if(arrayList[i][j] == 0):
                return i, j
                break

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

def writeFile(list):
    file = open('puzzle.out', 'w')
    for steps in list:
        # write each item on a new line
        file.write("%s " % steps)
    print('Done')

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

def BFSearch(arrayList):
    explored = []
    frontier = []

    nodeNumber = 0
    frontier = [NODE(nodeNumber, deepcopy(arrayList))]
    frontier = collections.deque(frontier)

    while(len(frontier) != 0):
        currentNode = frontier.popleft()
        explored.append(deepcopy(currentNode.nodeListState))
        x, y = getZeroIndex(currentNode.nodeListState, 3)
        if(currentNode.nodeListState == [[1,2,3],[4,5,6],[7,8,0]]):
            return currentNode
        else:
            if(x - 1 >= 0):
                nodeNumber += 1
                tempList = deepcopy(currentNode.nodeListState)
                temp = tempList[x - 1][y]
                tempList[x][y] = temp
                tempList[x - 1][y] = 0
                if tempList not in explored:
                    currentNode.downNode = NODE(nodeNumber, tempList)
                    currentNode.downNode.parentNode = currentNode
                    currentNode.downNode.action = "D"
                    frontier.append(currentNode.downNode)

            if(y - 1 >= 0):
                nodeNumber += 1
                tempList = deepcopy(currentNode.nodeListState)
                temp = tempList[x][y - 1]
                tempList[x][y] = temp
                tempList[x][y - 1] = 0
                if tempList not in explored:
                    currentNode.rightNode = NODE(nodeNumber, tempList)
                    currentNode.rightNode.parentNode = currentNode
                    currentNode.rightNode.action = "R"
                    frontier.append(currentNode.rightNode)

            if(x + 1 <= 2):
                nodeNumber += 1
                tempList = deepcopy(currentNode.nodeListState)
                temp = tempList[x + 1][y]
                tempList[x][y] = temp
                tempList[x + 1][y] = 0
                if tempList not in explored:
                    currentNode.upNode = NODE(nodeNumber, tempList)
                    currentNode.upNode.parentNode = currentNode
                    currentNode.upNode.action = "U"
                    frontier.append(currentNode.upNode)

            if(y + 1 <= 2):
                nodeNumber += 1
                tempList = deepcopy(currentNode.nodeListState)
                temp = tempList[x][y + 1]
                tempList[x][y] = temp
                tempList[x][y + 1] = 0
                if tempList not in explored:
                    currentNode.leftNode = NODE(nodeNumber, tempList)
                    currentNode.leftNode.parentNode = currentNode
                    currentNode.leftNode.action = "L"
                    frontier.append(currentNode.leftNode)

def DFSearch(arrayList):
    explored = []
    frontier = []

    nodeNumber = 0
    frontier = [NODE(nodeNumber, deepcopy(arrayList))]
    frontier = collections.deque(frontier)

    while(len(frontier) != 0):
        currentNode = frontier.pop()
        explored.append(deepcopy(currentNode.nodeListState))
        x, y = getZeroIndex(currentNode.nodeListState, 3)
        if(currentNode.nodeListState == [[1,2,3],[4,5,6],[7,8,0]]):
            return currentNode
        else:
            if(x - 1 >= 0):
                nodeNumber += 1
                tempList = deepcopy(currentNode.nodeListState)
                temp = tempList[x - 1][y]
                tempList[x][y] = temp
                tempList[x - 1][y] = 0
                if tempList not in explored:
                    currentNode.downNode = NODE(nodeNumber, tempList)
                    currentNode.downNode.parentNode = currentNode
                    currentNode.downNode.action = "D"
                    frontier.insert(0, currentNode.downNode)

            if(y - 1 >= 0):
                nodeNumber += 1
                tempList = deepcopy(currentNode.nodeListState)
                temp = tempList[x][y - 1]
                tempList[x][y] = temp
                tempList[x][y - 1] = 0
                if tempList not in explored:
                    currentNode.rightNode = NODE(nodeNumber, tempList)
                    currentNode.rightNode.parentNode = currentNode
                    currentNode.rightNode.action = "R"
                    frontier.insert(0, currentNode.rightNode)

            if(x + 1 <= 2):
                nodeNumber += 1
                tempList = deepcopy(currentNode.nodeListState)
                temp = tempList[x + 1][y]
                tempList[x][y] = temp
                tempList[x + 1][y] = 0
                if tempList not in explored:
                    currentNode.upNode = NODE(nodeNumber, tempList)
                    currentNode.upNode.parentNode = currentNode
                    currentNode.upNode.action = "U"
                    frontier.insert(0, currentNode.upNode)

            if(y + 1 <= 2):
                nodeNumber += 1
                tempList = deepcopy(currentNode.nodeListState)
                temp = tempList[x][y + 1]
                tempList[x][y] = temp
                tempList[x][y + 1] = 0
                if tempList not in explored:
                    currentNode.leftNode = NODE(nodeNumber, tempList)
                    currentNode.leftNode.parentNode = currentNode
                    currentNode.leftNode.action = "L"
                    frontier.insert(0, currentNode.leftNode)

def DFSearchMove(tileList, stepsPerState, listPerState, arrayOfNumbers, counter):
    # print("Numbers of steps:", len(stepsPerState))
    # print(arrayOfNumbers)
    # print("Steps:", stepsPerState)
    # print("Numbers of list states:", len(listPerState))

    x, y = getZeroIndex(listPerState[counter], 3)
    for j in tileList:
        if j == None:
            continue

        if stepsPerState[counter] == 'U':
            if listPerState[counter][x - 1][y] == j.tileNumber:
                j.moveTile(0)

        if stepsPerState[counter] == 'D':
            if listPerState[counter][x + 1][y] == j.tileNumber:
                j.moveTile(2)

        if stepsPerState[counter] == 'L':
            if listPerState[counter][x][y - 1] == j.tileNumber:
                j.moveTile(1)

        if stepsPerState[counter] == 'R':
            if listPerState[counter][x][y + 1] == j.tileNumber:
                j.moveTile(3)

    return listPerState[counter]


def getStepsAndList(node):
    stepsPerState = []
    listPerState = []

    while node.parentNode != None:
        stepsPerState.insert(0, node.action)
        listPerState.insert(0, node.nodeListState)
        node = node.parentNode

    return stepsPerState, listPerState

def main():
    clock = pygame.time.Clock()

    arrayOfNumbers = readFile()
    # arrayOfNumbers = [[3, 0, 2], [6, 5, 1], [4, 7, 8]]
    # arrayOfNumbers = [[8, 5, 4], [2, 7, 1], [3, 6, 0]]
    # print(isSolvable(arrayOfNumbers)) # test case 3

    tileNotArrangedText = TextClass(100, 100, 100, 50, "Tiles are not arranged!", 32)
    winText = TextClass(100, 100, 100, 50, 'All the tiles are in place!', 32)
    solvableText = TextClass(100, 100, 100, 50, 'The puzzle is Solvable!: ' + str(isSolvable(arrayOfNumbers)), 26)
    stepsText = TextClass(100, 100, 100, 50, '', 20)
    quitButton = ButtonClass(680, 300, 140, 40, COLOR_PASTELYELLOW, COLOR_AMBER, "QUIT")

    bfsButton = ButtonClass(545, 400, 130, 40, COLOR_PASTELYELLOW, COLOR_AMBER, "BFS")
    dfsButton = ButtonClass(685, 400, 130, 40, COLOR_PASTELYELLOW, COLOR_AMBER, "DFS")
    nextButton = ButtonClass(825, 400, 130, 40, COLOR_PASTELYELLOW, COLOR_AMBER, "NEXT")


    size = WINDOW_SCREEN_WIDTH
    counter = 0
    rows = 3

    distanceBetweenGrids = WINDOW_SCREEN_WIDTH // rows
    tileSize = distanceBetweenGrids

    window = pygame.display.set_mode((WINDOW_SCREEN_WIDTH*2, WINDOW_SCREEN_HEIGHT))

    correctPos = [[1,2,3],[4,5,6],[7,8,0]]
    tiles = []

    stepsBool = False

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
            stepsText.blitText(window, 520, 465)

            quitButton.drawButton(window)
            bfsButton.drawButton(window)
            dfsButton.drawButton(window)
            nextButton.drawButton(window)
            pygame.display.update()
            cursorPosX, cursorPosY = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if(quitButton.drawButton(window)):
                    exit()
                elif(dfsButton.drawButton(window)):
                    dfsButton.buttonColor = (175, 175, 0)
                    bfsButton.buttonColor = COLOR_PASTELYELLOW
                    currentNode = DFSearch(arrayOfNumbers)
                    steps, lists = getStepsAndList(currentNode)
                    stepsText.setText(steps)
                    stepsBool = True

                elif(bfsButton.drawButton(window)):
                    bfsButton.buttonColor = (175, 175, 0)
                    dfsButton.buttonColor = COLOR_PASTELYELLOW
                    currentNode = BFSearch(arrayOfNumbers)
                    steps, lists = getStepsAndList(currentNode)
                    stepsText.setText(steps)
                    stepsBool = True

                elif(nextButton.drawButton(window) and stepsBool):
                    arrayOfNumbers = DFSearchMove(tiles, steps ,lists, arrayOfNumbers, counter)
                    counter += 1


                # for i in range(len(tiles)):
                #     if tiles[i] == None:
                #         continue
                #     else:
                #         if(str(tiles[i].tileClicked(cursorPosX, cursorPosY)).isdigit()):
                #             number = tiles[i].tileClicked(cursorPosX, cursorPosY)
                #             x, y = getTileIndex(number, arrayOfNumbers, rows)
                #             try:
                #                 if(arrayOfNumbers[x + 1][y] == 0):
                #                     arrayOfNumbers[x + 1][y] = number
                #                     arrayOfNumbers[x][y] = 0
                #                     tiles[i].moveTile(2)
                #             except(IndexError):
                #                 pass
                #             try:
                #                 if(arrayOfNumbers[x - 1][y] == 0 and x - 1 >= 0): #
                #                     arrayOfNumbers[x - 1][y] = number
                #                     arrayOfNumbers[x][y] = 0
                #                     tiles[i].moveTile(0)
                #             except(IndexError):
                #                 pass
                #             try:
                #                 if(arrayOfNumbers[x][y + 1] == 0):
                #                     arrayOfNumbers[x][y + 1] = number
                #                     arrayOfNumbers[x][y] = 0
                #                     tiles[i].moveTile(3)
                #             except(IndexError):
                #                 pass
                #             try:
                #                 if(arrayOfNumbers[x][y - 1] == 0 and y - 1 >= 0): #
                #                     arrayOfNumbers[x][y - 1] = number
                #                     arrayOfNumbers[x][y] = 0
                #                     tiles[i].moveTile(1)
                #             except(IndexError):
                #                 pass
                #             break

                if(correctPos == arrayOfNumbers):
                    messagebox.showinfo("Cost",'Total path: ' + str(len(steps)))
                    writeFile(steps)
                    winText.blitText(window, 580, 200)
                    pygame.display.update()
                    time.sleep(3)
                    main()

        draw(window, size, rows, tiles, GRID)
main()
