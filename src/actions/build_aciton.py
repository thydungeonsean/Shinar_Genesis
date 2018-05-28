from action import Action
from src.enum.actions import BUILD_ACTION
from src.control.ui_controller import UIController
from map_tools import get_valid_build_points

from src.game_object.building_menu import *


class BuildAction(Action):

    CHOOSING = 0
    PLACING = 1

    def __init__(self, state, player):

        cls = BuildAction
        self.action_state = cls.CHOOSING
        Action.__init__(self, state, player, BUILD_ACTION)

        self.perform_state_action = {
            cls.CHOOSING: self.choose_action,
            cls.PLACING: self.perform_place_action
        }

        self.selected_building = None

    def initialize_action(self):

        # open options
        self.open_panels()

        self.valid_points = set()

    def deinitialize_action(self):

        self.close_panels()

    def perform_action(self, point):

        if point in self.valid_points:
            self.perform_state_action[self.action_state](point)

    def choose_action(self):
        pass

    # choice panel handles
    def choose_build_action(self, obj_code):
        self.selected_building = obj_code
        self.action_state = BuildAction.PLACING
        self.close_panels()
        self.valid_points = self.compute_valid_points()
        self.highlight_tiles()

    # panel controllers
    def open_panels(self):

        ui = UIController(self.state)
        ui.open_build_choice_panels(self.player, self)

    def close_panels(self):

        ui = UIController(self.state)
        ui.close_build_choice_panels(self)

    def compute_valid_points(self):
        return get_valid_build_points(self.state, self.selected_building)

    # build action
    def perform_place_action(self, point):
        building = buildings[self.selected_building](self.state, point, self.player)
        self.state.map.game_object_map.add_game_object(building)

        if self.selected_building in {ZIGGURAT, PALACE}:
            self.player.active_construction = building

    def construct_action(self):

        self.player.advance_construction()


