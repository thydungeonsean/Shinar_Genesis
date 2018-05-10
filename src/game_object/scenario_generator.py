from src.enum.terrain import *
from random import *
from village import Village
from palace import Palace
from src.enum.object_codes import *


class ScenarioGenerator(object):

    def __init__(self, state):

        self.state = state

    @property
    def tile_map(self):
        return self.state.map.tile_map

    @property
    def game_object_map(self):
        return self.state.map.game_object_map

    def populate(self):
        self.place_palaces()
        self.place_villages()
        self.initiate_dominion()

    def place_palaces(self):

        valid = self.tile_map.get_all_but(RIVER)
        valid = filter(lambda x: x not in self.game_object_map.occupied(), valid)

        p1 = self.state.players[0]
        p = Palace(self.state, choice(valid), p1)
        self.game_object_map.add_game_object(p)

    def place_villages(self):

        valid_coords = self.tile_map.get_all_but({DESERT, RIVER})
        size_dist = (1, 2, 2, 3, 3, 3, 4, 4, 5)

        for i in range(3):
            point = choice(valid_coords)
            v = Village(self.state, point, choice(size_dist))
            self.game_object_map.add_game_object(v)
            valid_coords.remove(point)

    def initiate_dominion(self):

        palaces = self.game_object_map.get_objects_with_code(PALACE)
        coords = [x.coord.int_position for x in palaces]
        print coords

