import pygame
import sys
import score

pygame.init()

# set game screen size
width = 1280
height = 720
size = width, height
screen = pygame.display.set_mode(size)
score_sec = score.Score()


# Updates Game High Score
def update_score(new_score):
    score_sec.update(new_score)
    screen.blit(score_sec.text, (320,0))

# Displays Game Over view
# TODO: Fix fitment of text
def game_over():
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

    pygame.display.update()


# keeps screen printed until game is quit
def displayboard():
    #for event in pygame.event.get():
       # if event.type == pygame.QUIT: sys.exit()

    # make screen background white
    screen.fill(pygame.Color(255, 255, 255, 255))

    screen.blit(score_sec.text, (320,0))

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

    # draw rectangles
    hor = 360  # starting horizontal pos of rectangle
    ver = 80  # starting vertical pos of rectangle
    sq_width = 20  # rectangle width
    sq_height = 20  # rectangle height
    square_size = (sq_width, sq_height)  # var combining both rectangle width and height

    #determines num squares printed on playing board
    y_Range = int(((endY-startY)/sq_height)/2) - 1
    x_Range = int(((endX-startX)/sq_width)/2) - 1

    for y in range(y_Range):  # loops through all vertical positions
        for x in range(x_Range):  # loops through all horizontal positions
            # resets pos of each rectangle
            pos = (hor, ver)
            # draws rectangle
            pygame.draw.rect(screen, (0, 0, 0, 0), [pos, square_size])
            # increments hor position
            hor = hor + (sq_width*2)
        # resets hor position for each row
        hor = 360
        # increments ver position
        ver = ver + (sq_height*2)



    # update display
    #pygame.display.flip()
