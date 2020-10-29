import time

import pygame
# from board import Board
# from snake import Snake
# from food import Food
from highscore import HighScore
import board
import cube


def main():
    pygame.init()

    food = pygame.image.load('Perfect50px.png')
    snekopen = pygame.image.load('OpenMouth50px.png')
    snekclos = pygame.image.load('ClosedMouth50px.png')
    snekbadi = pygame.image.load('Body50px.png')
    snektel = pygame.image.load('TailLeft50px.png')

    snakex = 300
    snakey = 100

    dx = 50
    dy = 10;

    gaming = True

    # High Score constructor
    score = HighScore()

    # Class Board constructor
    # board = Board()

    # Class Snake constructor
    # snake = Snake()

    # Class Food constructor
    # food = Food()

    while gaming:
        board.displayboard()
        # Handle Events
        for event in pygame.event.get():

            # Quit Game
            if event.type == pygame.QUIT:
                gaming = False

            if event.type == pygame.KEYDOWN:
                print(event)
                if event.key == pygame.K_RIGHT:
                    snakex += dx
                # case/switch for up,down,left,right
                # add appropriate offset to snake coords (head)

        # Boundary check snake -> Edges and self
        # Check if snake ate food -> Increase snake length, move food coord
        # Update board
        if snakex <= 450:
            cube.put(board.screen, 600, 100, food)
        cube.put(board.screen, snakex, 100, snektel)
        cube.put(board.screen, snakex + 50, 100, snekbadi)
        if 500 > snakex > 350:
            cube.put(board.screen, snakex + 50 + 50, 75, snekopen)
        else:
            cube.put(board.screen, snakex + 50 + 50, 85, snekclos)

        if snakex > 800:
            snakex = 300

        pygame.display.update()

    # Game Over
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
