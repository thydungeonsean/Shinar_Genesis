from random import randint


class FarmMap(object):

    num_farm_patterns = 3

    def __init__(self):

        self.farms = {}

    def add_farm(self, (x, y)):
        self.farms[(x, y)] = randint(0, FarmMap.num_farm_patterns-1)

    def remove_farm(self, (x, y)):
        del self.farms[(x, y)]
