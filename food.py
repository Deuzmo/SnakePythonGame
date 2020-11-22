import pygame
import random
import cube


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.lastpos = (0, 0)
        self.food = pygame.image.load('img/Apple20px.png')
        self.randpos()

    def randpos(self):
        self.lastpos = self.position
        self.position = (random.randint(17, (46))*20
                         , random.randint(3, (32))*20) # these ranges are based on the board coordinates.

    def draw(self, board):
        cube.put(board, self.position[0], self.position[1], self.food)
