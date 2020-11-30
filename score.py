import pygame
pygame.font.init()


class Score:
	txt = None

	def __init__(self):
		self.curr = 0
	
	def reset(self):
		self.curr = 0

	def update(self):
		self.curr += 1