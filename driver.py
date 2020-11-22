import pygame
from highscore import HighScore
import board
import snake
import food
import score_curr

# 32 x 32 playing field
BOARD_WIDTH = 640
BOARD_LENGTH = 640
GRID_SIZE = 20

def set_score(curr_score, score):
    # Set score if needed
    if curr_score > score.score:
        score.score = curr_score
        score.set_score()


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

    # Score constructor
    scoreObj = score_curr.Score_Curr()


    curr_score = 0

    while gaming:
        clock.tick(10)
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                gaming = False
            s.handle_keys(event)

        board.displayboard(scoreObj)

        # Return something to signify valid move
        bad_move = s.move()
        if bad_move:
            board.game_over()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                # QUIT
                if mouse[0] >= 565 and mouse[0] <= 715 and mouse[1] >= 360 and mouse[1] <= 390:
                    set_score(curr_score, score)
                    pygame.quit()
                    quit()
                # PLAY AGAIN
                if mouse[0] >= 565 and mouse[0] <= 715 and mouse[1] >= 400 and mouse[1] <= 430:
                    main()
        else:
            if s.getheadpos() == f.position:
                s.length += 1
                curr_score += 1
                f.randpos()
                scoreObj.update()
                if curr_score > score.score: 
                    # set new high score on screen
                    board.update_score(curr_score)

            f.draw(board.screen)
            s.draw(board.screen, f)

            pygame.display.update()

    # Game Over
    set_score(curr_score, score)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
