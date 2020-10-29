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

    testimg = pygame.image.load('Perfect25px.png')
    snekopen = pygame.image.load('OpenMouth25px.png')
    snekclos = pygame.image.load('ClosedMouth25px.png')
    snekbadi = pygame.image.load('Body25px.png')
    snektel = pygame.image.load('Tail25px.png')

    snakex = 350
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


        cube.put(board.screen, 600, 100, testimg)
        cube.put(board.screen, snakex, 100, snektel)
        cube.put(board.screen, snakex + 50, 100, snekbadi)
        cube.put(board.screen, snakex + 50 + 40, 95, snekopen)

        pygame.display.update()


    # Game Over
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()