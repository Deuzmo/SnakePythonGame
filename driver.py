import pygame
# from board import Board
# from snake import Snake
# from food import Food
from highscore import HighScore
import board
import snake
import food

# 32 x 32 playing field
BOARD_WIDTH = 640
BOARD_LENGTH = 640
GRID_SIZE = 20


def main():
    pygame.init()

    clock = pygame.time.Clock()
    gaming = True
    s = snake.Snake()
    f = food.Food()
    # High Score constructor
    score = HighScore()

    # Class Board constructor
    # board = Board()

    # Class Snake constructor
    # snake = Snake()

    # Class Food constructor
    # food = Food()

    while gaming:
        clock.tick(10)
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                gaming = False
            s.handle_keys(event)

        board.displayboard()
        s.move()
        print("Head")
        print(s.getheadpos())
        print("Food")
        print(f.position)
        if s.getheadpos() == f.position:
            s.length += 1
            f.randpos()
        # Handle Events

        # case/switch for up,down,left,right
        # add appropriate offset to snake coords (head)
        s.draw(board.screen)
        f.draw(board.screen)
        # Boundary check snake -> Edges and self
        # Check if snake ate food -> Increase snake length, move food coord
        # Update board

        pygame.display.update()

    # Game Over
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
