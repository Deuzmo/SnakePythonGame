import pygame
# from board import Board
# from snake import Snake
# from food import Food
from highscore import HighScore


def main():
    pygame.init()
    gaming = True

    # High Score constructor
    score = HighScore()

    # Class Board constructor
    # board = Board() 

    # Class Snake constructor
    # snake = Snake()

    # Class Food constructor
    # food = Food()

    while gaming:
    	# Handle Events
    	for event in pygame.event.get():

    		# Quit Game
    		if event.type == pygame.QUIT:
    			gaming = False

    		if event.type == pygame.KEYDOWN:
    			print(event)
    			# case/switch for up,down,left,right
    			# add appropriate offset to snake coords (head)

    	# Boundary check snake -> Edges and self
    	# Check if snake ate food -> Increase snake length, move food coord
    	# Update board

    # Game Over
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()