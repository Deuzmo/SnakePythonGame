import pygame
from constants import (UP, DOWN, LEFT, RIGHT,
                       BOARD_LENGTH, BOARD_WIDTH, GRID_SIZE)


class Snake:
    def __init__(self):
        self.length = 2
        self.positions = [((BOARD_LENGTH / 2 + GRID_SIZE), (BOARD_WIDTH / 2 + GRID_SIZE))]
        self.direction = RIGHT
        self.openup = pygame.image.load('img/OpenMouthUp20px.png')
        self.opendown = pygame.image.load('img/OpenMouthDown20px.png')
        self.openleft = pygame.image.load('img/OpenMouthLeft20px.png')
        self.openright = pygame.image.load('img/OpenMouthRight20px.png')
        self.closedup = pygame.image.load('img/ClosedMouthUp20px.png')
        self.closeddown = pygame.image.load('img/ClosedMouthDown20px.png')
        self.closedleft = pygame.image.load('img/ClosedMouthLeft20px.png')
        self.closedright = pygame.image.load('img/ClosedMouthRight20px.png')
        self.snekbadi = pygame.image.load('img/Body20px.png')
        self.tailup = pygame.image.load('img/TailUp20px.png')
        self.taildown = pygame.image.load('img/TailDown20px.png')
        self.tailleft = pygame.image.load('img/TailLeft20px.png')
        self.tailright = pygame.image.load('img/TailRight20px.png')
        self.alive = True

    def grow(self):
        self.length += 1

    def getheadpos(self):
        return self.positions[0]

    def gettail(self, offset=0):
        return self.positions[len(self.positions) - 1 - offset]

    def turn(self, dir):
        if self.length > 2 and ((dir[0], dir[1]) == self.direction or 
                                (dir[0] * -1, dir[1] * -1) == self.direction):
            return  # if the inrender_item direction is to go back when length is too long, ignore it
        else:
            self.direction = dir

    def move(self):
        current = self.getheadpos()
        x, y = self.direction
        new = (current[0] + x * GRID_SIZE, current[1] + y * GRID_SIZE)

        # Self-collision check
        if len(self.positions) > 3 and new in self.positions[2:]:
            self.alive = False
        # Border Collision check
        elif (new[0] <= 320 or new[0] >= 960
                or new[1] <= 40 or new[1] >= 680):
            self.alive = False
        else:
            self.positions.insert(0, new)
            if self.length < len(self.positions):
                self.positions.pop()
            self.alive = True

    def input_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.turn(UP)
            elif event.key == pygame.K_DOWN:
                self.turn(DOWN)
            elif event.key == pygame.K_LEFT:
                self.turn(LEFT)
            elif event.key == pygame.K_RIGHT:
                self.turn(RIGHT)