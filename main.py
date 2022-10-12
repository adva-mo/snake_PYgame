from turtle import width
from pygame.locals import *

import pygame, sys
import os

pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE")

FPS = 60

bg_color = (140, 171, 168)
BLACK = (0, 0, 0)
snake = "c"


def draw_window():
    WIN.fill(bg_color)
    # WIN.blit(snake, (snake.x, snake.y))
    pygame.display.update()


def main():
    # snake = pygame.Rect(700, 300, 10, 10)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
    draw_window()
