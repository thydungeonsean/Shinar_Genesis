from moisture_map import MoistureMap
from tile_map import TileMap
from src.image.map_image import MapImage


class StrategicMap(object):

    default_river = [(5, 0), (5, 1), (5, 2),
                     (4, 2), (4, 3), (4, 4),
                     (4, 5), (5, 5), (5, 6),
                     (6, 6), (6, 7), (6, 8),
                     (6, 9)]

    def __init__(self, state):

        self.state = state

        self.w = 10
        self.h = 10
        self.river = StrategicMap.default_river[:]
        self.moisture_map = MoistureMap(self.w, self.h, self.river)
        self.tile_map = TileMap(self.w, self.h, self.moisture_map)
        self.map_image = MapImage(self, self.tile_map)

    def initialize(self):
        self.moisture_map.initialize()
        self.tile_map.initialize()
        self.map_image.initialize()

    def draw(self, surface):
        self.map_image.draw(surface)

    def run(self):
        self.map_image.run()
