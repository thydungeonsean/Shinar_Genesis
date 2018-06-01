from random import randint


class FloodTimer(object):

    BASE_TIME = 10

    def __init__(self, variation=3):

        self.i = 0
        self.end = 0
        self.vari = variation

        self.reset()

    def reset(self):

        self.i = 0
        self.end = FloodTimer.BASE_TIME + randint(-self.vari, self.vari)

    def advance(self):
        self.i += 1

    def flood_happens(self):
        return self.i >= self.end
