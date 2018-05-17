

class Vector(object):

    def __init__(self, *args):

        self.x = 0.0
        self.y = 0.0

        self.set_initial_value(*args)

    def set_initial_value(self, *args):
        if args:

            if len(args) > 2:
                raise Exception("not valid parameter for vector")
            elif len(args) == 2:
                self.x = float(args[0])
                self.y = float(args[1])
            elif len(args) == 1:
                self.x = float(args[0][0])
                self.y = float(args[0][1])

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
