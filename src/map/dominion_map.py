from base_map import BaseMap
import pygame
from src.constants import TILE_SIZE


class DominionMap(BaseMap):

    def __init__(self, w, h, state):

        self.state = state
        BaseMap.__init__(self, w, h)
        self.tiles = {}

    def initialize(self):
        for o_id in self.state.player_manager.get_player_ids():
            self.tiles[o_id] = pygame.Surface((TILE_SIZE, TILE_SIZE)).convert()
            self.tiles[o_id].fill(self.state.player_manager.get_player(o_id).color)
            self.tiles[o_id].set_alpha(100)

    def base_value(self, x, y):
        return None

    def draw(self, surface):

        for point in self.get_all_but(None):
            self.draw_tile(point, surface)

    def draw_tile(self, (x, y), surface):
        px = x * TILE_SIZE
        py = y * TILE_SIZE
        surface.blit(self.tiles[self.get_tile((x, y))], (px, py))

    def add_dominion(self, owner_id, point):
        self.set_tile(point, owner_id)
