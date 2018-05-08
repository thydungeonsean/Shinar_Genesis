

class BaseMap(object):

    def __init__(self, w, h):

        self.w = w
        self.h = h

        self.array = [[self.base_value(x, y) for y in range(self.h)] for x in range(self.w)]

    def base_value(self, x, y):
        return 0

    @property
    def all_points(self):
        return ((x, y) for y in range(self.h) for x in range(self.w))

    def get_all(self, tile_id):
        if isinstance(tile_id, set):
            return filter(lambda x: self.get_tile(x) in tile_id, self.all_points)
        else:
            return filter(lambda x: self.get_tile(x) == tile_id, self.all_points)

    def set_tile(self, (x, y), value):
        self.array[x][y] = value

    def get_tile(self, (x, y)):
        return self.array[x][y]

    def in_bounds(self, (x, y)):
        return 0 <= x < self.w and 0 <= y < self.h
