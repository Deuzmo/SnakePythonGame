from constants import *
from enum import Enum
import pygame
import snake
import food
import score
import high_score
import pygame_textinput


# set game screen size
size = FRAME_WIDTH, FRAME_HEIGHT
screen = pygame.display.set_mode(size)

#Initialize board objects
snake_obj = snake.Snake()
food_obj = food.Food(snake_obj)
score_obj = score.Score()
text_input = pygame_textinput.TextInput(text_color=RED, font_size=30, 
                                       max_string_length=7, antialias=True,
                                       repeat_keys_initial_ms=400,
                                       repeat_keys_interval_ms=400)
save_highscore = False


# Indicates game state, perhaps convert board to an object?
class Game_state(Enum):
    MENU = 0
    PLAYING = 1
    GAMEOVER_SCREEN = 2
    HIGHSCORE_SCREEN = 3


# Initial state will be menu
state = Game_state.MENU

# Initialize game over screen objects
hs_obj = high_score.High_Score()  # hs object


# Displays Main Menu
def display_menu():
    screen.fill(SILVER)
    pygame.draw.rect(screen, BLACK, [320,40,BOARD_WIDTH,BOARD_LENGTH])  
    img = pygame.image.load('img/Snek640x320p.png')
    x_offset = img.get_rect().width/2
    render_item(CENTER_X - x_offset, FRAME_HEIGHT - 100, img)
    
    first_btn_pos = CENTER_X - ((BTN_W)*3 + 40)/2
    second_btn_pos = first_btn_pos + BTN_W + 20
    third_btn_pos = second_btn_pos + BTN_W + 20
    
    btn_y_pos = CENTER_Y + 180

    # Draw QUIT button
    pygame.draw.rect(screen, GRAY, [first_btn_pos, 
                                    btn_y_pos,
                                    BTN_W,
                                    BTN_H])  # x, y, width(x), height(y)  

    # Draw PLAY button
    pygame.draw.rect(screen, GRAY, [second_btn_pos, 
                                    btn_y_pos,
                                    BTN_W,
                                    BTN_H])  # x, y, width(x), height(y)  

    # Draw High Scores button
    pygame.draw.rect(screen, GRAY, [third_btn_pos, 
                                    btn_y_pos,
                                    BTN_W,
                                    BTN_H])  # x, y, width(x), height(y)

    # Decide whether buttons are lighted up or not
    mx, my = pygame.mouse.get_pos()
    if (mx >= first_btn_pos and mx <= first_btn_pos+BTN_W and
            my >= btn_y_pos and my <= btn_y_pos+BTN_H):
        pygame.draw.rect(screen, LIGHTGRAY, [first_btn_pos, btn_y_pos, BTN_W, BTN_H])
    elif (mx >= second_btn_pos and mx <= second_btn_pos+BTN_W and
            my >= btn_y_pos and my <= btn_y_pos+BTN_H):
        pygame.draw.rect(screen, LIGHTGRAY, [second_btn_pos, btn_y_pos, BTN_W, BTN_H])
    elif (mx >= third_btn_pos and mx <= third_btn_pos+BTN_W and
            my >= btn_y_pos and my <= btn_y_pos+BTN_H):
        pygame.draw.rect(screen, LIGHTGRAY, [third_btn_pos, btn_y_pos, BTN_W, BTN_H])

    first_txt_center = first_btn_pos + (BTN_W/2)
    second_txt_center = first_txt_center + BTN_W + 20
    third_txt_center =  second_txt_center + BTN_W + 20
    # Draw QUIT button text
    txt = pygame.font.SysFont('Comic Sans MS', 20)
    img = txt.render('QUIT', True, BLACK)
    offset_from_center = img.get_rect().width/2
    screen.blit(img, (first_txt_center - offset_from_center, btn_y_pos))

    # DRAW PLAY Button text
    txt = pygame.font.SysFont('Comic Sans MS', 20)
    img = txt.render('PLAY', True, BLACK)
    offset_from_center = img.get_rect().width/2
    screen.blit(img, (second_txt_center - offset_from_center, btn_y_pos))

    # DRAW High Scores Button text
    txt = pygame.font.SysFont('Comic Sans MS', 20)
    img = txt.render('HIGH SCORES', True, BLACK)
    offset_from_center = img.get_rect().width/2
    screen.blit(img, (third_txt_center - offset_from_center, btn_y_pos))

# Displays Game Over view
def game_over():
    global text_input
    # Black out screen
    pygame.draw.rect(screen, BLACK, [320,40,640,640])
    # Prompt user to input user for high score display
    if score_obj.curr > hs_obj.min_score:
        txt = pygame.font.SysFont('Comic Sans MS', 25)
        if not hs_obj.score_set:
            img = txt.render('You have achieved a new high score!', True, LIME)
            sub_img = txt.render('Enter a username to save score:', True, LIME)
            offset_from_center = img.get_rect().width/2
            render_item(CENTER_X - offset_from_center,
                        (CENTER_Y/2) + 330,
                        img)
            render_item(CENTER_X - offset_from_center,
                        (CENTER_Y/2) + 300,
                        sub_img)
            txt_img = text_input.get_surface()
            pygame.draw.rect(screen, WHITE, [CENTER_X-50, 280,100,30])
            render_item(CENTER_X-50, 430, txt_img)

            # Return true if return key hit
            if save_highscore:
                hs_obj.add_new_high_score(text_input.get_text(), score_obj.curr)
                hs_obj.set_high_scores()
                text_input.clear_text()
        else:
            saved = txt.render('High Score saved.', True, LIME)
            offset_from_center = saved.get_rect().width/2
            render_item(CENTER_X - offset_from_center,
                        (CENTER_Y/2) + 330,
                        saved)

    # Draw game over
    txt = pygame.font.SysFont('Comic Sans MS', 25)
    img = txt.render('GAME OVER', True, RED)
    offset_from_center = img.get_rect().width/2
    render_item(CENTER_X - offset_from_center, CENTER_Y + 40, img)

    # Draw MENU button
    pygame.draw.rect(screen, GRAY, [565,360,150,30]) # x, y, width(x), height(y)  
    # Draw PLAY AGAIN button
    pygame.draw.rect(screen, GRAY, [565,400,150,30])


    # Decide whether buttons are lighted up or not
    mposx, mposy = pygame.mouse.get_pos()
    if (mposx >= 565 and mposx <= 715 and mposy >= 360 and mposy <= 390):
        pygame.draw.rect(screen, LIGHTGRAY, [565,360,150,30])  # x, y, width(x), height(y)
    elif (mposx >= 565 and mposx <= 715 and mposy >= 400 and mposy <= 430):
        pygame.draw.rect(screen, LIGHTGRAY, [565,400,150,30])

    # Draw MENU button text
    txt = pygame.font.SysFont('Comic Sans MS', 20)
    img = txt.render('MENU', True, BLACK)
    offset_from_center = img.get_rect().width/2
    render_item(CENTER_X - offset_from_center, CENTER_Y, img)

    # DRAW PLAY AGAIN Button text
    txt = pygame.font.SysFont('Comic Sans MS', 20)
    img = txt.render('PLAY AGAIN', True, BLACK)
    offset_from_center = img.get_rect().width/2
    render_item(CENTER_X - offset_from_center, CENTER_Y - 40, img)


# Renders the given item into the board.
def render_item(x, y, item):
    screen.blit(item, (x, FRAME_HEIGHT-y))


def draw_food(food):
    render_item(food.position[0], food.position[1], food.food)


def draw_score(score):
    txt_str = 'Your Score is: {}'.format(score.curr)
    font = pygame.font.SysFont('Comic Sans MS', 25)
    img = font.render(txt_str, True, (0, 0, 0))
    render_item(320, 720, img)

def draw_snake(snake, food):

    # this first 3 lines would be used to properly render the head according
    # to the food positionn. Stolen from the move function, teehee
    headpos = snake.getheadpos()
    x, y = snake.direction
    front = (headpos[0] + x * GRID_SIZE, headpos[1] + y * GRID_SIZE)
    foodpos = food.position
    for p in snake.positions:
        if p == snake.getheadpos():
            if snake.direction == UP:
                if front == foodpos or p == food.lastpos:
                    food.lastpos = (-1, -1)  # this prevents lingering hitbox
                    # for the last position of the food.
                    render_item(p[0] - 10, p[1] + GRID_SIZE, snake.openup)
                else:
                    render_item(p[0], p[1], snake.closedup)
            elif snake.direction == DOWN:
                if front == foodpos or p == food.lastpos:
                    food.lastpos = (-1, -1)
                    render_item(p[0], p[1], snake.opendown)
                else:
                    render_item(p[0], p[1], snake.closeddown)
            elif snake.direction == LEFT:
                if front == foodpos or p == food.lastpos:
                    food.lastpos = (-1, -1)
                    render_item(p[0] - GRID_SIZE, p[1] + 10, snake.openleft)
                else:
                    render_item(p[0], p[1], snake.closedleft)
            elif snake.direction == RIGHT:
                if front == foodpos or p == food.lastpos:
                    food.lastpos = (-1, -1)
                    render_item(p[0], p[1] + 10, snake.openright)
                else:
                    render_item(p[0], p[1], snake.closedright)
        elif p == snake.gettail():
            orientation = tuple(map(lambda i, j, k: (i - j) / k,
                                snake.gettail(1), p, (GRID_SIZE, GRID_SIZE))
                                )
            if orientation == UP:
                render_item(p[0], p[1], snake.taildown)
            elif orientation == DOWN:
                render_item(p[0], p[1], snake.tailup)
            elif orientation == LEFT:
                render_item(p[0], p[1], snake.tailright)
            elif orientation == RIGHT:
                render_item(p[0], p[1], snake.tailleft)
        else:
            render_item(p[0], p[1], snake.snekbadi)


# Function handles logic for deciding what to draw at every frame
def draw_all():
    global state
    if state is Game_state.MENU:
        display_menu()
    elif (state is Game_state.PLAYING):
        displayboard()
        draw_score(score_obj)
        draw_food(food_obj)
        draw_snake(snake_obj, food_obj)
    elif (state is Game_state.GAMEOVER_SCREEN):
        game_over()
    elif (state is Game_state.HIGHSCORE_SCREEN):
        #  Do stuff related to highscore
        return
    
    

# Function handles reinitialization of the game when clicking PLAY AGAIN
def reinitialize():
    global snake_obj
    global food_obj
    global state
    state = Game_state.PLAYING
    snake_obj = snake.Snake()
    food_obj = food.Food(snake_obj)
    score_obj.reset()
    hs_obj.reset()


# displays the game board
def displayboard():

    # make screen background white
    screen.fill(SILVER)

    # draw border
    startX = 320
    startY = 40
    endX = 960
    endY = 680
    length = 660
    thick = 20
    pygame.draw.rect(screen, (0, 0, 0, 0), [startX, startY, length, thick])
    pygame.draw.rect(screen, (0, 0, 0, 0), [startX, startY, thick, length])
    pygame.draw.rect(screen, (0, 0, 0, 0), [startX, endY, length, thick])
    pygame.draw.rect(screen, (0, 0, 0, 0), [endX, startY, thick, length])
    
    #draw grass texture
    background = pygame.image.load('img/grass.jpg')
    screen.blit(background, (340, 60))
