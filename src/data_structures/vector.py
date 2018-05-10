

class Vector(object):

    def __init__(self):

        self.x = 0.0
        self.y = 0.0

    def set_position(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def set_from_tuple(self, (x, y)):
        self.set_position(x, y)

    def match_vector(self, vec):
        self.set_position(vec.x, vec.y)

    def add_vector(self, vec):
        self.set_position(self.x + vec.x, self.y + vec.y)

    def subtract_vector(self, vec):
        self.set_position(self.x - vec.y, self.y - vec.y)

    def multiply(self, m):
        self.set_position(self.x * m, self.y * m)

    def divide(self, d):
        self.set_position(self.x / d, self.y / d)

    @property
    def position(self):
        return self.x, self.y

    @property
    def int_position(self):
        return int(self.x), int(self.y)
