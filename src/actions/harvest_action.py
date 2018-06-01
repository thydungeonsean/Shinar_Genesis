from action import Action
from map_tools import *
from src.enum.actions import HARVEST_ACTION


class HarvestAction(Action):

    def __init__(self, state, player):

        Action.__init__(self, state, player, HARVEST_ACTION)

    def compute_valid_points(self):

        granaries = get_friendly_buildings_of_type(self.state, GRANARY)
        points = get_coords_from_objects(granaries)
        self.valid_points = set(points)

    def perform_action(self, point):

        if point in self.valid_points:
            connected_farms = get_connected_farms(self.state, point, exclude_connectors=True)
            # harvest connected farms
            map(self.harvest, connected_farms)

            # end of action wrap up
            self.complete_action()

    def harvest(self, point):
        self.state.map.farm_map.remove_farm(point)

