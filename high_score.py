import pygame

pygame.font.init()

class High_Score:
	curr = 0
	txt = None

	# Constructor
	# Sets user high score or 0 if none available
	def __init__(self):
	    self.curr = self.get_score()
	    self.txt = self.make_txt(self.curr)

	    #new
	    self.scores = self.high_scores()

	    # check against this
	    self.min_score = self.get_min(self.scores)

	# Retrieves minimum to qualify for new high score
	# check if current score > minimum
	def get_min(self, scores):
		vals = []
		for item in scores:
			vals.append(item.values()[0])
		return min(vals)


	# Returns a list of dictionary of high scores
	# Format -> [{<username>:<high score>}]
	def high_scores(self):
		file = open('scores.txt', 'r')
		content = file.readlines()
		hs = []
		for line in content:
			score = line.split(' ')
			if len(score) > 1:
				hs.append({score[0]:int(score[1].rstrip())})
		file.close()
		return hs

	def add_new_high_score(self, name, score):
		i = 0
		for hs in self.scores:
			curr = hs.values[0]
			if score > curr:
				hs.insert(i, {name:score})
				break

	# Updates high score file
	def set_score(self):
	    file = open('score.txt', 'w')
	    write = 'High Score: {}'.format(self.curr)
	    file.write(write)
	    file.close()

	# Renders text to attach to board
	def make_txt(self, score):
		txt_str = 'Your High Score is: {}'.format(score)
		txt = pygame.font.SysFont('Comic Sans MS', 25)
		return txt.render(txt_str, False, (0,0,0))

	def update(self, score):
		self.curr = score
		self.txt = self.make_txt(score)
		self.set_score()

	def get_score(self):
		# get score from file or 0 if no file
	    file = open('score.txt', 'r')
	    contents = file.read()
	    vals = contents.split(' ')
	    try:
	        score = int(vals[len(vals)-1])
	    except IndexError:
	        score = 0
	    file.close()
	    return score