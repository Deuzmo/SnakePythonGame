# in a way this is just an abstraction of any object on the game board
# I am using blit because I plan to use png files to represent the food and the snake parts.
import pygame

def put(board, x, y, item):
    board.blit(item, (x, y))
    #pygame.display.update()


