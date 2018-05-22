from src.enum.terrain import *
from random import *
from src.game_object.village import Village
from src.game_object.palace import Palace
from src.game_object.granary import Granary
from src.enum.object_codes import *

from map_tools import *


class ScenarioGenerator(object):

    def __init__(self, state):

        self.state = state

    @property
    def tile_map(self):
        return self.state.map.tile_map

    @property
    def game_object_map(self):
        return self.state.map.game_object_map

    @property
    def dominion_map(self):
        return self.state.map.dominion_map

    def populate(self):
        self.place_palaces()
        self.initiate_dominion()

        self.place_granaries()
        self.place_villages()
        # self.blast_farm()

    def place_palaces(self):

        for player in self.state.player_manager.players:
            valid = self.tile_map.get_all_but(RIVER)
            valid = filter(lambda x: x not in self.game_object_map.occupied(), valid)

            p = Palace(self.state, choice(valid), player)
            self.game_object_map.add_game_object(p)

    def place_villages(self):

        valid_coords = self.tile_map.get_all_but({DESERT, RIVER})
        valid_coords = filter(lambda x: x not in self.game_object_map.occupied(), valid_coords)
        size_dist = (1, 2, 2, 3, 3, 3, 4, 4, 5)

        for i in range(3):
            point = choice(valid_coords)
            v = Village(self.state, point, choice(size_dist))
            self.game_object_map.add_game_object(v)
            valid_coords.remove(point)

    def initiate_dominion(self):

        palaces = self.game_object_map.get_objects_with_code(PALACE)

        for point in self.dominion_map.all_points:
            closest_palace = get_closest(point, palaces)

            if closest_palace is not None:
                self.dominion_map.add_dominion(closest_palace.owner_id, point)

    def place_granaries(self):

        for player in self.state.player_manager.players:

            valid = self.tile_map.get_all({FERTILE, PLAINS})
            valid = filter(lambda x: self.dominion_map.point_is_in_player_dominion(x, player), valid)
            valid = filter(lambda x: x not in self.game_object_map.occupied(), valid)

            if valid:
                g = Granary(self.state, choice(valid), player)
                self.game_object_map.add_game_object(g)

    def blast_farm(self):

        for point in self.tile_map.all_points:

            if self.tile_map.get_tile(point) in {FERTILE, PLAINS}:
                self.state.map.farm_map.add_farm(point)
