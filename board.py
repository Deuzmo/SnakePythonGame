from constants import *
import pygame
import snake
import food
import score
import high_score


# set game screen size
size = FRAME_WIDTH, FRAME_HEIGHT
screen = pygame.display.set_mode(size)

#Initialize board objects
snake_obj = snake.Snake()
food_obj = food.Food(snake_obj)
score_obj = score.Score()

# use on game over
hs_obj = high_score.High_Score() # hs object

# Updates current game score
def update_curr_score(score):
    score.update()
    screen.blit(score.txt, (320, 0))

# Displays Game Over view
# TODO: Fix fitment of text
def game_over():

    # Prompt user to input user for high score display
    if score_obj.curr > hs_obj.min_score:
        if not hs_obj.score_set: # so it doesnt loop

            # REPLACE test with user input name
            hs_obj.add_new_high_score('test', score_obj.curr)
            hs_obj.set_high_scores()

    # Black out screen
    screen.fill(pygame.Color(255, 255, 255, 255))
    pygame.draw.rect(screen, (10,10,10,10), [320,40,640,640])

    # Draw game over
    txt = pygame.font.SysFont('Comic Sans MS', 25)
    res = txt.render('GAME OVER', False, (0,200,0))
    screen.blit(res, (565,320))

    # Draw buttons
    pygame.draw.rect(screen, (255, 255, 255, 255), [565,360,150,30]) # x, y, width(x), height(y)
    pygame.draw.rect(screen, (255, 255, 255, 255), [565,400,150,30])

    # Draw button text
    txt = pygame.font.SysFont('Comic Sans MS', 20)
    res = txt.render('QUIT', False, (0,200,0))
    screen.blit(res, (600,360))
    res = txt.render('PLAY AGAIN', False, (0,200,0))
    screen.blit(res, (575,400))


# Renders the given item into the board.
def render_item(x, y, item):
    screen.blit(item, (x, FRAME_HEIGHT-y))


def draw_food(food):
    render_item(food.position[0], food.position[1], food.food)


def draw_score(score):
    txt_str = 'Your Score is: {}'.format(score.curr)
    font = pygame.font.SysFont('Comic Sans MS', 25)
    img = font.render(txt_str, False, (0, 0, 0))
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
    if (snake_obj.alive):
        displayboard()
        draw_score(score_obj)
        draw_food(food_obj)
        draw_snake(snake_obj, food_obj)
    else:
        game_over()
        draw_score(score_obj)
    
    


def reinitialize():
    global snake_obj
    global food_obj
    snake_obj = snake.Snake()
    food_obj = food.Food(snake_obj)
    score_obj.reset()
    hs_obj.reset()


# keeps screen printed until game is quit
def displayboard():

    # make screen background white
    screen.fill(pygame.Color(255, 255, 255, 255))

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
