import pygame
from src.constants import TILE_SIZE
from src.colors import *
from random import randint


class MapHighlighter(object):

    def __init__(self, state):

        self.state = state
        self.highlights = []
        self.defense_highlights = []

        self.highlight_surf = pygame.Surface((TILE_SIZE, TILE_SIZE)).convert()
        self.highlight_surf.fill(WHITE)
        self.highlight_surf.set_alpha(120)

        self.defense_highlight_surf = pygame.Surface((TILE_SIZE, TILE_SIZE)).convert()
        self.defense_highlight_surf.fill((0, 220, 220))
        self.defense_highlight_surf.set_alpha(120)

    def run(self):
        r = randint(200, 255)
        self.highlight_surf.fill((r, r, r))

    def draw(self, surface):
        map(lambda x: self.draw_highlight(surface, x), self.highlights)
        map(lambda x: self.draw_defense_highlight(surface, x), self.defense_highlights)

    def draw_highlight(self, surface, (x, y)):
        px = x * TILE_SIZE
        py = y * TILE_SIZE
        surface.blit(self.highlight_surf, (px, py))

    def draw_defense_highlight(self, surface, (x, y)):
        px = x * TILE_SIZE
        py = y * TILE_SIZE
        surface.blit(self.defense_highlight_surf, (px, py))

    def highlight(self, action):
        self.highlights = [x for x in action.valid_points]

    def clear_highlight(self):
        del self.highlights[:]

    def update_defense_highlight(self):
        self.defense_highlights = [x for x in self.state.map.guard_map.get_guarded_points()]
