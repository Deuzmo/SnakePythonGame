class HighScore:

    # Updates high score file
    def set_score(self):
        file = open('score.txt', 'w')
        write = 'High Score: {}'.format(self.score)
        file.write(write)
        file.close()

    # Constructor
    # Sets user high score or 0 if none available
    def __init__(self):
        # get score from file or 0 if no file
        file = open('score.txt', 'r')
        contents = file.read()
        vals = contents.split(' ')
        try:
            score = int(vals[len(vals)-1])
        except IndexError:
            score = 0
        file.close()
        self.score = score