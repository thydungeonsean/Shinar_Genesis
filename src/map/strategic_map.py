from dominion_map import DominionMap
from farm_map import FarmMap
from moisture_map import MoistureMap
from river_generator import RiverGenerator
from src.game_object.game_object_map import GameObjectMap
from src.image.map_image import MapImage
from src.map.scenario_generation.scenario_generator import ScenarioGenerator
from tile_map import TileMap


class StrategicMap(object):

    default_river = [(5, 0), (5, 1), (5, 2),
                     (4, 2), (4, 3), (4, 4),
                     (4, 5), (5, 5), (5, 6),
                     (6, 6), (6, 7), (6, 8),
                     (6, 9)]

    def __init__(self, state):

        self.state = state

        self.w = 30
        self.h = 24
        self.dominion_map = DominionMap(self.w, self.h, self.state)
        self.river = RiverGenerator(self).generate_river()
        self.moisture_map = MoistureMap(self.w, self.h, self.river)
        self.tile_map = TileMap(self.w, self.h, self.moisture_map)
        self.farm_map = FarmMap(self)
        self.map_image = MapImage(self, self.tile_map)

        self.game_object_map = GameObjectMap(self.state, self.tile_map)

        self.scenario_generator = ScenarioGenerator(self.state)

    def initialize(self):
        self.moisture_map.initialize()
        self.tile_map.initialize()
        self.dominion_map.initialize()
        self.map_image.initialize()

        self.game_object_map.initialize()
        self.scenario_generator.populate()

    def draw(self, surface):
        self.map_image.draw(surface)
        self.game_object_map.draw(surface)

    def run(self):
        self.dominion_map.run()
        self.farm_map.run()
        self.map_image.run()
        self.game_object_map.run()
