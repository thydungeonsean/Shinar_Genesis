from action import Action
from src.control.ui_controller import UIController
from map_tools import get_army_placement_points, get_friendly_armies, get_coords_from_objects, get_army_movement_options
from src.game_object.army import Army


class MilitaryAction(Action):

    CHOOSING = 0
    PLACING = 1
    SELECTING = 2
    MOVING = 3

    def __init__(self, state, player, action_id):

        cls = MilitaryAction
        self.action_state = cls.CHOOSING
        Action.__init__(self, state, player, action_id)

        self.perform_state_action = {
            cls.CHOOSING: self.choose_action,
            cls.SELECTING: self.perform_select_action,
            cls.MOVING: self.perform_move_action,
            cls.PLACING: self.perform_place_action
        }

        self.selected_army = None

    def initialize_action(self):

        # open options
        self.open_panels()

        self.valid_points = set()

    def deinitialize_action(self):

        self.close_panels()

    def perform_action(self, point):

        if point in self.valid_points:
            self.perform_state_action[self.action_state](point)

    def choose_action(self, point):
        print 'choosing'

    # choice panel handles
    def choose_place_action(self):
        self.action_state = MilitaryAction.PLACING
        self.close_panels()
        self.valid_points = self.compute_valid_placement_points()
        self.highlight_tiles()

    def choose_select_action(self):
        self.action_state = MilitaryAction.SELECTING
        self.close_panels()
        self.valid_points = self.compute_valid_selection_points()
        self.highlight_tiles()

    # panel controllers
    def open_panels(self):

        ui = UIController(self.state)
        ui.open_action_choice_panels(self)

    def close_panels(self):

        ui = UIController(self.state)
        ui.close_action_choice_panels(self)

    # placing action
    def compute_valid_placement_points(self):

        spawn_points = get_army_placement_points(self.state)

        return set(spawn_points)

    def perform_place_action(self, point):
        # add army to point
        army = self.get_army(point)
        self.state.map.game_object_map.add_game_object(army)

    def get_army(self, point):
        return Army(self.state, point, self.player)

    # selecting action
    def compute_valid_selection_points(self):
        armies = get_friendly_armies(self.state)

        return get_coords_from_objects(armies)

    def perform_select_action(self, point):

        # get army at point
        army = self.state.map.game_object_map.get_at(point)[0]

        # select it
        self.selected_army = army

        self.action_state = MilitaryAction.MOVING
        self.valid_points = self.compute_valid_move_points()
        self.highlight_tiles()

    # moving action
    def compute_valid_move_points(self):
        # points in range of selected army
        return get_army_movement_options(self.state, self.selected_army)

    def perform_move_action(self, point):

        # move army to point
        self.selected_army.move(point)

        # trigger battle if necessary

        # trigger action effect
        self.activate_effect(point)

        # end action

    def activate_effect(self, point):
        pass

    # ui dressing
    def place_text(self):
        return 'Place'

    def select_text(self):
        return 'Select'
