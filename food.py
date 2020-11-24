import pygame
import random

class Food:
    def __init__(self, snake):
        self.position = (0, 0)
        self.lastpos = (0, 0)
        self.food = pygame.image.load('img/Apple20px.png')
        self.update_pos(snake)
        self.spawn_again = True

    def update_pos(self, snake):
        if (not snake.alive):
            self.spawn_again = False
            return
         
        self.lastpos = self.position
        self.position = (random.randint(17, (46)) * 20
                         , random.randint(3, (32)) * 20)  # these ranges are based on the board coordinates.
        while self.position is snake.positions: # this will keep on repositioning until it is not in the snake's body
            print("spawning new food")
            self.position = (random.randint(17, (46)) * 20
                             , random.randint(3, (32)) * 20)  # these ranges are based on the board coordinates.
