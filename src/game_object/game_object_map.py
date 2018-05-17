

class GameObjectMap(object):

    def __init__(self, state, tile_map):

        self.state = state
        self.tile_map = tile_map

        self.game_objects = []

    def initialize(self):
        pass

    def draw(self, surface):
        map(lambda x: x.draw(surface), self.game_objects)

    def run(self):
        map(lambda x: x.run(), self.game_objects)

    def get_at(self, point):
        return filter(lambda x: x.coord.int_position == point, self.game_objects)

    def occupied(self):
        return [x.coord.int_position for x in self.game_objects]

    def add_game_object(self, obj):
        self.game_objects.append(obj)

    def get_objects_with_code(self, obj_code):
        return filter(lambda x: x.obj_code == obj_code, self.game_objects)

