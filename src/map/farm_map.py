from random import randint


class FarmMap(object):

    num_farm_patterns = 3

    def __init__(self, map):

        self.map = map
        self.farms = {}
        self.updated_tiles = []

    def add_farm(self, (x, y)):
        self.farms[(x, y)] = randint(0, FarmMap.num_farm_patterns-1)
        self.updated_tiles.append((x, y))

    def remove_farm(self, (x, y)):
        del self.farms[(x, y)]
        self.updated_tiles.append((x, y))

    def is_farm(self, point):
        return point in self.farms

    def run(self):

        if self.updated_tiles:
            self.map.map_image.update(self.updated_tiles)
            del self.updated_tiles[:]
