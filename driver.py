import pygame
import board
import sys


# def set_score(curr_score, score):
#     # Set score if needed
#     if curr_score > score.score:
#         score.score = curr_score
#         score.set_score()


def main():
    pygame.init()
    clock = pygame.time.Clock()
    gaming = True

    while gaming:
        clock.tick(12)

        if (board.snake_obj.alive):
            # Process input during game session
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    board.snake_obj.input_handler(event)
                    
            board.snake_obj.move()

            if board.snake_obj.getheadpos() == board.food_obj.position:
                board.snake_obj.grow()
                board.food_obj.update_pos(board.snake_obj)
                board.score_obj.update()
                board.hs_obj.update(board.score_obj.curr) #

        else:
            # Process input in Game Over screen
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()

                    # QUIT (TODO: return to main menu instead of quit)
                    if mouse[0] >= 565 and mouse[0] <= 715 and mouse[1] >= 360 and mouse[1] <= 390:
                        pygame.quit()
                        sys.exit()
                    # PLAY AGAIN
                    if mouse[0] >= 565 and mouse[0] <= 715 and mouse[1] >= 400 and mouse[1] <= 430:
                        board.reinitialize()

        # Render changes
        board.draw_all()
        pygame.display.update()


if __name__ == "__main__":
    main()
