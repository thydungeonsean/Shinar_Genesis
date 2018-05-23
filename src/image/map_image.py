import pygame
from src.constants import *
from src.colors import *
from src.enum.terrain import *


class MapImage(object):

    WATER_SPEED = 30

    def __init__(self, parent_map, tile_map):

        self.parent_map = parent_map
        self.tile_map = tile_map
        self.farm_map = parent_map.farm_map
        self.dominion_map = parent_map.dominion_map
        self.image = None
        self.river_colors = {}

        self.farm_image = self.create_farm_image()

    def initialize(self):
        self.create_map_image()
        self.render_map()

    def create_map_image(self):

        w = self.tile_map.w * TILE_SIZE
        h = self.tile_map.h * TILE_SIZE

        self.image = pygame.Surface((w, h)).convert()

    def render_map(self):
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

        if (x, y) in self.dominion_map.edges:
            self.draw_border((x, y))

    def fluctuate_river_colors(self):

        for point in self.tile_map.get_all({RIVER}):
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

        self.image.blit(self.farm_image, (px, py))

    def create_farm_image(self):

        img = pygame.image.load('assets/farm.png').convert()
        img.set_colorkey(WHITE)
        return img

    def update(self, tiles):

        for tile in tiles:
            self.render_tile(tile)

    def draw_border(self, point):

        img_code = self.dominion_map.edges[point]
        color = self.dominion_map.get_color(point)
        img = self.dominion_map.edge_tile_map.load_border_image(img_code, color)

        x, y = point
        px = x * TILE_SIZE
        py = y * TILE_SIZE

        img.draw(self.image, (px, py))
