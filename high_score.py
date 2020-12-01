import pygame

pygame.font.init()

max_hs = 5

#
# Top players will be saved
#
class High_Score:

	# Constructor
	def __init__(self):


	    # Scores in list form
	    self.scores = self.get_high_scores()

	    # Use to check if curr score to be saved
	    self.min_score = self.get_min(self.scores)

	    self.score_set = False


	def reset(self):
		self.score_set = False
		self.scores = self.get_high_scores()
		self.min_score = self.get_min(self.scores)

	# Retrieves minimum to qualify for new high score
	# check if current score > minimum
	def get_min(self, scores):
		vals = []
		for item in scores:
			vals.append(item[1])
		if len(vals) == 0:
			return 0
		else:
			return min(vals)


	# Returns a list of dictionary of high scores
	# Format -> [{<username>:<high score>}]
	def get_high_scores(self):
		file = open('scores.txt', 'r')
		content = file.readlines()
		hs = []
		for line in content:
			score = line.split(' ')
			if len(score) > 1:
				hs.append((score[0], int(score[1].rstrip())))
		file.close()
		return hs

	# Writes high scores to file
	def set_high_scores(self):
		file = open('scores.txt', 'w')
		for score in self.scores:
			file.write(score[0] + ' ' + str(score[1]) + '\n')
		file.close()


	# Adds latest high score in appropriate postion
	# trims array by 1 (if length > 5) to adjust
	# CALL UPON GAME END IF CURR > MIN
	def add_new_high_score(self, name, score):
		self.score_set = True
		i = 0

		# init config
		if len(self.scores) == 0:
			self.scores.insert(0, (name, score))

		# once more hs
		else:
			for index, hs in enumerate(self.scores):
				if score > hs[1]:
					self.scores.insert(index, (name, score))
					if len(self.scores) > 5:
						self.scores = self.scores[:5]
					return