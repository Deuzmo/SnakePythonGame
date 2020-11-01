import pygame
import cube
from driver import GRID_SIZE
from driver import BOARD_LENGTH
from driver import BOARD_WIDTH

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self):
        self.length = 2
        self.positions = [((BOARD_LENGTH / 2), (BOARD_WIDTH / 2))]
        self.direction = RIGHT
        self.openup = pygame.image.load('OpenMouthUp20px.png')
        self.opendown = pygame.image.load('OpenMouthDown20px.png')
        self.openleft = pygame.image.load('OpenMouthLeft20px.png')
        self.openright = pygame.image.load('OpenMouthRight20px.png')
        self.closedup = pygame.image.load('ClosedMouthUp20px.png')
        self.closeddown = pygame.image.load('ClosedMouthDown20px.png')
        self.closedleft = pygame.image.load('ClosedMouthLeft20px.png')
        self.closedright = pygame.image.load('ClosedMouthRight20px.png')
        self.snekbadi = pygame.image.load('Body20px.png')
        self.tailup = pygame.image.load('TailUp20px.png')
        self.taildown = pygame.image.load('TailDown20px.png')
        self.tailleft = pygame.image.load('TailLeft20px.png')
        self.tailright = pygame.image.load('TailRight20px.png')

    def getheadpos(self):
        return self.positions[0]

    def gettail(self, offset=0):
        return self.positions[len(self.positions) - 1 - offset]

    def turn(self, dir):
        if self.length > 2 and ((dir[0], dir[1]) == self.direction or 
                                (dir[0] * -1, dir[1] * -1) == self.direction):
            return  # if the input direction is to go back when length is too long, ignore it
        else:
            self.direction = dir

    def move(self):
        current = self.getheadpos()
        x, y = self.direction
        new = (current[0] + x * GRID_SIZE, current[1] + y * GRID_SIZE)
        if len(self.positions) > 3 and new in self.positions[2:]:
            print("Oh no!")
        else:
            self.positions.insert(0, new)
            if self.length < len(self.positions):
                self.positions.pop()

    def draw(self, board, food):
        # this first 3 lines would be used to properly render the head according to the food position.
        # stolen from the move function, teehee
        headpos = self.getheadpos()
        x, y = self.direction
        front = (headpos[0] + x * GRID_SIZE, headpos[1] + y * GRID_SIZE)
        foodpos = food.position
        for p in self.positions:
            if p == self.getheadpos():
                if self.direction == UP:
                    if front == foodpos or p == food.lastpos:
                        cube.put(board, p[0]- 10, p[1] + GRID_SIZE, self.openup)
                    else:
                        cube.put(board, p[0], p[1], self.closedup)
                elif self.direction == DOWN:
                    if front == foodpos or p == food.lastpos:
                        cube.put(board, p[0], p[1], self.opendown)
                    else:
                        cube.put(board, p[0], p[1], self.closeddown)
                elif self.direction == LEFT:
                    if front == foodpos or p == food.lastpos:
                        cube.put(board, p[0] - GRID_SIZE, p[1] + 10, self.openleft)
                    else:
                        cube.put(board, p[0], p[1], self.closedleft)
                elif self.direction == RIGHT:
                    if front == foodpos or p == food.lastpos:
                        cube.put(board, p[0], p[1] + 10, self.openright)
                    else:
                        cube.put(board, p[0], p[1], self.closedright)
            elif p == self.gettail():
                orientation = tuple(map(lambda i, j, k: (i - j) / k,
                                    self.gettail(1), p, (GRID_SIZE, GRID_SIZE))
                                    )
                if orientation == UP:
                    cube.put(board, p[0], p[1], self.taildown)
                elif orientation == DOWN:
                    cube.put(board, p[0], p[1], self.tailup)
                elif orientation == LEFT:
                    cube.put(board, p[0], p[1], self.tailright)
                elif orientation == RIGHT:
                    cube.put(board, p[0], p[1], self.tailleft)
            else:
                cube.put(board, p[0], p[1], self.snekbadi)

    def handle_keys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.turn(UP)
            elif event.key == pygame.K_DOWN:
                self.turn(DOWN)
            elif event.key == pygame.K_LEFT:
                self.turn(LEFT)
            elif event.key == pygame.K_RIGHT:
                self.turn(RIGHT)
