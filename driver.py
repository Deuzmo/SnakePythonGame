import pygame
from highscore import HighScore
import board
import score_curr


def set_score(curr_score, score):
    # Set score if needed
    if curr_score > score.score:
        score.score = curr_score
        score.set_score()


def main():
    pygame.init()
    clock = pygame.time.Clock()
    gaming = True

    # High Score constructor
    score = HighScore()

    # Score constructor
    scoreObj = score_curr.Score_Curr()
    curr_score = 0

    while gaming:
        clock.tick(12)
        board.snake_obj.update_pos()
        board.displayboard(scoreObj)
        # Return something to signify valid move
        bad_move = board.snake_obj.move()
        if bad_move:
            board.game_over()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()

                    # QUIT
                    if mouse[0] >= 565 and mouse[0] <= 715 and mouse[1] >= 360 and mouse[1] <= 390:
                        set_score(curr_score, score)
                        pygame.quit()
                        sys.exit()
                    # PLAY AGAIN
                    if mouse[0] >= 565 and mouse[0] <= 715 and mouse[1] >= 400 and mouse[1] <= 430:
                        main()
        else:
            if board.snake_obj.getheadpos() == board.food_obj.position:
                board.snake_obj.length += 1
                curr_score += 1
                board.food_obj.update_pos(board.snake_obj)
                scoreObj.update()
                if curr_score > score.score: 
                    # set new high score on screen
                    board.update_score(curr_score)

            board.draw_all()
            pygame.display.update()

    # Game Over
    set_score(curr_score, score)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
