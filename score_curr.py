import pygame
import highscore

pygame.font.init()


class Score_Curr:
	curr = 0
	txt = None

	def __init__(self):
		self.txt = self.make_txt(self.curr)

	def make_txt(self, score):
		txt_str = 'Your Score is: {}'.format(score)
		txt = pygame.font.SysFont('Comic Sans MS', 25)
		return txt.render(txt_str, False, (0, 0, 0))
	
	def reset(self):
		self.curr = 0

	def update(self):
		self.curr += 1
		self.txt = self.make_txt(self.curr)