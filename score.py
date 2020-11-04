import pygame
import highscore

pygame.font.init()
hs = highscore.HighScore()

# Renders text to attach to board
def make_txt(score):
	txt_str = 'Your High Score is: {}'.format(score)
	txt = pygame.font.SysFont('Comic Sans MS', 25)
	return txt.render(txt_str, False, (0,0,0))

class Score:
	def __init__(self):
		self.text = make_txt(hs.score)

	def update(self, new_score):
		self.text = make_txt(new_score)



