import pygame
import random
import cube


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.food = pygame.image.load('Perfect50px.png')
        self.randpos()

    def randpos(self):
        self.position = (random.randint(0, (32-1))*20
                         , random.randint(0, (32-1))*20)

    def draw(self, board):
        cube.put(board, self.position[0], self.position[1], self.food)
