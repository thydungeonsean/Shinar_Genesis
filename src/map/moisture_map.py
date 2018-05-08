from base_map import BaseMap
from src.data_structures.dijkstra_map import *


class MoistureMap(BaseMap):

    river_bed = 5

    def __init__(self, w, h, river):

        self.river = river
        BaseMap.__init__(self, w, h)

    def initialize(self):
        self.spread_moisture()

    def base_value(self, x, y):
        if (x, y) in self.river:
            return MoistureMap.river_bed
        else:
            return 0

    def spread_moisture(self):

        d_map = DijkstraMap(self)
        for i in range(5, 2, -1):
            edge = d_map.spread(i)
            map(lambda x: self.set_tile(x, i-1), edge)
