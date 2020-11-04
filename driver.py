import pygame
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

    # Class Snake constructor
    s = snake.Snake()

    # Class Food constructor
    f = food.Food()
    # High Score constructor
    score = HighScore()

    curr_score = 0

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
            curr_score += 1
            # if curr_score > score.score : set new high score on screen
            f.randpos()
        # Handle Events

        # case/switch for up,down,left,right
        # add appropriate offset to snake coords (head)
        f.draw(board.screen)
        s.draw(board.screen, f)
        # Boundary check snake -> Edges and self
        # Check if snake ate food -> Increase snake length, move food coord
        # Update board

        pygame.display.update()

    # Game Over
    pygame.quit()

    # Set score if needed
    if curr_score > score.score:
        score.score = curr_score
        score.set_score()
    quit()


if __name__ == "__main__":
    main()
