from random import *


class RiverGenerator(object):

    def __init__(self, base_map):

        self.base_map = base_map
        self.river = []

    def generate_river(self):

        self.seed_river()

        while self.head_of_river[1] < self.base_map.h - 1:
            self.advance_river()

        self.end_river()

        return self.river

    def seed_river(self):

        mid = self.base_map.w / 2
        spread = mid / 2
        offset = randint(-spread, spread)
        start_x = mid + offset
        self.river.extend(((start_x, 0), (start_x, 1)))

    @property
    def head_of_river(self):
        return self.river[-1]

    def end_river(self):

        x, y = self.head_of_river
        self.river.append((x, y+1))

    def advance_river(self):

        available = self.find_available_points(self.head_of_river)
        self.river.append(choice(available))

    def find_available_points(self, (x, y)):

        possible = [(x-1, y), (x+1, y), (x, y+1)]
        possible = filter(self.valid_point, possible)

        return possible

    def valid_point(self, (x, y)):

        if not self.base_map.dominion_map.in_bounds((x, y)):
            return False
        if (x, y) in self.river:
            return False
        if (x, y-1) in self.river and (x+1, y) in self.river or (x-1, y) in self.river:
            return False

        return True
