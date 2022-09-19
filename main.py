import pygame
import random
import time
import os

WINDOW_SCREEN_WIDTH = 510
WINDOW_SCREEN_HEIGHT = 510

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE= (255, 255, 255)

pygame.display.set_caption("8-Puzzle Game")

def drawGrid(gridDistance, rows, surface):
    sizeBtwn = gridDistance // rows

    x = 0
    y = 0

    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, COLOR_BLACK, (x, 0), (x, gridDistance))
        pygame.draw.line(surface, COLOR_BLACK, (0, y), (gridDistance, y))

def draw(gridDistance, rows, surface):
    surface.fill(COLOR_WHITE)
    drawGrid(gridDistance, rows, surface)

    pygame.display.update()

def main():

    rows = 3
    size = WINDOW_SCREEN_WIDTH
    distanceBetweenGrids = WINDOW_SCREEN_WIDTH // rows
    print(distanceBetweenGrids)
    window = pygame.display.set_mode((WINDOW_SCREEN_WIDTH*2, WINDOW_SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        draw(size, rows, window)

main()
