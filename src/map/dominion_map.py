from base_map import BaseMap


class DominionMap(BaseMap):

    def __init__(self, w, h, state):

        self.state = state
        BaseMap.__init__(self, w, h)

    def initialize(self):
        pass

    def base_value(self, x, y):
        return None

    def draw(self, surface):

        for point in self.get_all_but(None):
            self.draw_tile(point, surface)

    def draw_tile(self, (x, y), surface):
        pass
