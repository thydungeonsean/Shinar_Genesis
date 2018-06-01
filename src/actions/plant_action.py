from action import Action
from src.enum.actions import PLANT_ACTION
from map_tools import *


class PlantAction(Action):

    def __init__(self, state, player):

        Action.__init__(self, state, player, PLANT_ACTION)

    def compute_valid_points(self):

        granaries = get_friendly_buildings_of_type(self.state, GRANARY)
        points = get_coords_from_objects(granaries)
        self.valid_points = set(points)

    def perform_action(self, point):

        if point in self.valid_points:

            connected_farms = get_connected_farms(self.state, point, exclude_connectors=False)
            edge = get_edge(connected_farms)
            planting = plant_edge(self.state, edge, connected_farms)

            map(lambda x: self.plant(x), planting)

            # end point
            self.complete_action()

    def plant(self, point):

        self.state.map.farm_map.add_farm(point)

