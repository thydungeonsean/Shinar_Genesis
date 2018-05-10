import pygame
from src.constants import *
from src.colors import *
from src.enum.terrain import *
from random import randint


class MapImage(object):

    WATER_SPEED = 30

    num_farm_patterns = 3
    farm_patterns = []

    def __init__(self, parent_map, tile_map):

        self.parent_map = parent_map
        self.tile_map = tile_map
        self.farm_map = parent_map.farm_map
        self.image = None
        self.river_colors = {}

        self.generate_farm_patterns()

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

        if (x, y) in self.farm_map.farms:
            self.draw_farm((x, y))

    def fluctuate_river_colors(self):

        for point in self.tile_map.get_all({RIVER, DESERT}):
            self.river_colors[point] = fluctuate_river()

    def draw(self, surface):

        surface.blit(self.image, (0, 0))

    def run(self):

        if self.parent_map.state.frame % MapImage.WATER_SPEED == 0:
            self.fluctuate_river_colors()
            self.render_map()

    def draw_farm(self, (x, y)):
        px = x * TILE_SIZE
        py = y * TILE_SIZE

        for sx, sy in MapImage.farm_patterns[self.farm_map.farms[(x, y)]]:
            pygame.draw.line(self.image, farm, (px+sx, py+sy), (px+sx, py+sy+randint(2, 3)))

    def generate_farm_patterns(self):

        for i in range(MapImage.num_farm_patterns):
            pattern = []
            for i in range(randint(30, 50)):
                sx = randint(0, TILE_SIZE)
                sy = randint(0, TILE_SIZE)
                pattern.append((sx, sy))

            MapImage.farm_patterns.append(pattern)
