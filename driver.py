import pygame
import board
from constants import *
import sys


def main():

    pygame.init()
    clock = pygame.time.Clock()
    gaming = True

    while gaming:
        clock.tick(12)

        if (board.state is board.Game_state.MENU):
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    posx_1 = CENTER_X - ((BTN_W)*3 + 40)/2
                    posx_2 = posx_1 + BTN_W + 20
                    posx_3 = posx_2 + BTN_W + 20
                    posy = CENTER_Y + 180
                 
                    # QUIT
                    if (mx >= posx_1 and mx <= posx_1+BTN_W and 
                            my >= posy and my <= posy+BTN_H):
                        pygame.quit()
                        sys.exit()

                    # PLAY 
                    elif (mx >= posx_2 and mx <= posx_2+BTN_W and
                            my >= posy and my <= posy+BTN_H):
                        board.state = board.Game_state.PLAYING
                        board.reinitialize()
                    
                    # VIEW HIGHSCORES
                    elif (mx >= posx_3 and mx <= posx_3+BTN_W and
                            my >= posy and my <= posy+BTN_H):
                        board.state = board.Game_state.HIGHSCORE_SCREEN
 
        elif (board.state is board.Game_state.PLAYING):
            # Process input during game session
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    board.snake_obj.input_handler(event)
                    break  # Do not take more than one input per frame

            board.snake_obj.move()

            if board.snake_obj.getheadpos() == board.food_obj.position:
                board.snake_obj.grow()
                board.food_obj.update_pos(board.snake_obj)
                board.score_obj.update()

            elif (not board.snake_obj.alive):
                board.state = board.Game_state.GAMEOVER_SCREEN
       
        elif (board.state is board.Game_state.GAMEOVER_SCREEN):
            events = pygame.event.get()

            # Process keyboard presses
            board.save_highscore = board.text_input.update(events)
            # Process mouse input 
            for event in events:

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()

                    # BACK TO MENU
                    if mouse[0] >= 565 and mouse[0] <= 715 and mouse[1] >= 360 and mouse[1] <= 390:
                        board.state = board.Game_state.MENU
                    # PLAY AGAIN
                    if mouse[0] >= 565 and mouse[0] <= 715 and mouse[1] >= 400 and mouse[1] <= 430:
                        board.reinitialize()

        elif (board.state is board.Game_state.HIGHSCORE_SCREEN):
            # go back to main menu since highscore menu is not implemented
            board.state = board.Game_state.MENU

        # Render changes
        board.draw_all()
        pygame.display.update()


if __name__ == "__main__":
    main()
