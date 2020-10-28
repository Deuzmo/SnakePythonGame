import sys, pygame
pygame.init()

#set game screen size
width = 1280
height = 720
size = width, height
screen = pygame.display.set_mode(size)

#keeps screen printed until game is quit
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    #make screen background white
    screen.fill(pygame.Color(255, 255, 255, 255))
    
    #draw border
    startX = 310
    startY = 30
    endX = 950
    endY = 670
    length = 660
    thick = 20
    pygame.draw.rect(screen, (0, 0, 0, 0), [startX, startY, length, thick])
    pygame.draw.rect(screen, (0, 0, 0, 0), [startX, startY, thick, length])
    pygame.draw.rect(screen, (0, 0, 0, 0), [startX, endY, length, thick])
    pygame.draw.rect(screen, (0, 0, 0, 0), [endX, startY, thick, length])
    
    #draw rectangles
    hor = 350                           #starting horizontal pos of rectangle
    ver = 70                            #starting vertical pos of rectangle
    sq_width = 100                      #rectangle width 
    sq_height = 100                     #rectangle height
    square_size = (sq_width, sq_height) #var combining both rectangle width and height
    
    for y in range(5):                  #loops through all vertical positions
        for x in range(5):              #loops through all horizontal positions
            #resets pos of each rectangle
            pos = (hor, ver)
            #draws rectangle
            pygame.draw.rect(screen, (0, 0, 0, 0), [pos, square_size])
            #increments hor position
            hor = hor + 120
        #resets hor position for each row
        hor = 350
        #increments ver position
        ver = ver + 120
        
    #update display    
    pygame.display.flip()

