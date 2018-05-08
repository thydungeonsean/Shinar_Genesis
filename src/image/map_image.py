import pygame
from src.constants import *
from src.colors import *
from src.enum.terrain import *


class MapImage(object):

    WATER_SPEED = 30

    def __init__(self, parent_map, tile_map):

        self.parent_map = parent_map
        self.tile_map = tile_map
        self.image = None
        self.river_colors = {}

    def initialize(self):
        self.render_map()

    def render_map(self):

        w = self.tile_map.w * TILE_SIZE
        h = self.tile_map.h * TILE_SIZE

        self.image = pygame.Surface((w, h)).convert()

        self.fluctuate_river_colors()

        for point in self.tile_map.all_points:
            self.render_tile(point)

    def render_tile(self, (x, y)):

        t = self.tile_map.get_tile((x, y))
        if t == DESERT:
            col = desert
        elif t == PLAINS:
            col = plains
        elif t == FERTILE:
            col = fertile
        elif t == RIVER:
            col = self.river_colors[(x, y)]
        else:
            col = (0, 0, 0)

        pygame.draw.rect(self.image, col, (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def fluctuate_river_colors(self):

        for point in self.tile_map.get_all({RIVER, DESERT}):
            self.river_colors[point] = fluctuate_river()

    def draw(self, surface):

        surface.blit(self.image, (0, 0))

    def run(self):

        if self.parent_map.state.frame % MapImage.WATER_SPEED == 0:
            self.fluctuate_river_colors()
            self.render_map()
