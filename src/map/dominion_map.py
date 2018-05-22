from base_map import BaseMap
import pygame
from src.constants import TILE_SIZE


class DominionMap(BaseMap):

    def __init__(self, w, h, state):

        self.state = state
        BaseMap.__init__(self, w, h)
        self.tiles = {}
        self.needs_update = True
        self.edges = {}

    def run(self):

        if self.needs_update:
            self.update_edges()

    def initialize(self):
        for o_id in self.state.player_manager.get_player_ids():
            self.tiles[o_id] = pygame.Surface((TILE_SIZE, TILE_SIZE)).convert()
            self.tiles[o_id].fill(self.state.player_manager.get_player(o_id).color)
            self.tiles[o_id].set_alpha(80)

    def base_value(self, x, y):
        return None

    def draw(self, surface):

        for point in self.edges.iterkeys():
            self.draw_tile(point, surface)

    def draw_tile(self, (x, y), surface):
        px = x * TILE_SIZE
        py = y * TILE_SIZE
        surface.blit(self.tiles[self.get_tile((x, y))], (px, py))

    def add_dominion(self, owner_id, point):
        self.set_tile(point, owner_id)
        self.needs_update = True

    def point_is_in_player_dominion(self, point, player):

        player_id = player.player_id
        return self.get_tile(point) == player_id

    def update_edges(self):

        self.edges.clear()

        for player_id in self.state.player_manager.get_player_ids():

            players_dominion = self.get_all(player_id)
            edges = self.find_edge(players_dominion)
            for e in edges:
                self.edges[e] = 1

        self.needs_update = False

    def find_edge(self, area):
        area_set = set(area)
        return filter(lambda x: self.not_surrounded(x, area_set), area)

    def not_surrounded(self, point, area):
        adj = self.get_adj(point)
        return len(adj.intersection(area)) != 4

    def get_adj(self, (x, y)):

        return {(x-1, y), (x+1, y), (x, y-1), (x, y+1)}
