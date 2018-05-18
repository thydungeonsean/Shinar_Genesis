from action import Action
from src.enum.actions import PLANT_ACTION
from map_tools import *


class PlantAction(Action):

    def __init__(self, state, player):

        Action.__init__(self, state, player, PLANT_ACTION)

    def point_is_valid(self, point):
        return point_has_granary(self.state, point)
