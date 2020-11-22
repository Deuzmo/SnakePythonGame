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
    screen.blit(score_sec.text, (735,0))

# Updates current game score
def update_curr_score(scoreObj):
    scoreObj.update()
    screen.blit(scoreObj.txt, (320, 0))

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
def displayboard(scoreObj):
    #for event in pygame.event.get():
       # if event.type == pygame.QUIT: sys.exit()

    # make screen background white
    screen.fill(pygame.Color(255, 255, 255, 255))

    # insert score counter
    screen.blit(scoreObj.txt, (320, 0))

    # high score
    screen.blit(score_sec.text, (735,0))

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

    # update display
    #pygame.display.flip()
