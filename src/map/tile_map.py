from base_map import BaseMap
from src.enum.terrain import *


class TileMap(BaseMap):

    def __init__(self, w, h, moisture_map):

        BaseMap.__init__(self, w, h)
        self.moisture_map = moisture_map

    def initialize(self):
        self.update_map()

    def base_value(self, x, y):
        return DESERT

    def update_map(self):
        map(lambda x: self.update_point(x), self.all_points)

    def update_point(self, point):
        value = moisture_to_tile(self.moisture_map.get_tile(point))
        self.set_tile(point, value)

