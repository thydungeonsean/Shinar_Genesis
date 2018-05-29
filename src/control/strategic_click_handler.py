import pygame
from src.constants import TILE_SIZE


class StrategicClickHandler(object):

    def __init__(self, state):

        self.state = state

    def click(self):

        point = pygame.mouse.get_pos()

        if self.point_over_strategy_map(point):
            if self.state.action_controller.action_ready:
                self.state.action_controller.action.perform_action(self.get_map_coord(point))

    def point_over_strategy_map(self, point):
        return True

    def get_map_coord(self, (x, y)):

        return x / TILE_SIZE, y / TILE_SIZE
