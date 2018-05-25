

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
        if isinstance(obj_code, set):
            return filter(lambda x: x.obj_code in obj_code, self.game_objects)
        else:
            return filter(lambda x: x.obj_code == obj_code, self.game_objects)

    def get_friendly_objects(self, player):
        return filter(lambda x: x.owner_id == player.player_id, self.game_objects)
