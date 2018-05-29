from action import Action
from src.control.ui_controller import UIController
from map_tools import *
from src.game_object.army import Army
from src.enum.object_codes import ARMY


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
            cls.CHOOSING: self.null_action,
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
        ui.close_action_choice_panels()

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

        # trigger battle if necessary
        if self.battle_is_triggered(point):  # battle is triggered

            # move army to point
            self.selected_army.move(point)

            print 'battle initiated'
            defender = self.get_defending_army(point)
            win_effect, lose_effect = self.get_battle_win_loss_effects(point, defender)

            self.state.initiate_battle(self.selected_army, None, win_effect, lose_effect)

        else:
            # move army to point
            self.selected_army.move(point)
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

    # battle triggering helper methods
    def battle_is_triggered(self, point):
        return enemy_occupied(self.state, point)  # or self.state.map.defend_map.point_defended(point)

    def get_battle_win_loss_effects(self, point, defender):

        win_effect = self.get_win_effect(point, defender)

        def lose_effect():
            print 'defender wins'
            self.selected_army.rout()
            # if defender intercepted, move them to this point
            # end action

        return win_effect, lose_effect

    def get_win_effect(self, point, defender):

        def win_effect():
            self.activate_effect(point)
            print 'attacker wins'
            defender.rout()
            # end action

        return win_effect

    def get_defending_army(self, point):

        obj = self.state.map.game_object_map.get_at(point)
        obj = filter(lambda x: x.owner_id != self.player.player_id, obj)[0]
        if obj.obj_code == ARMY:
            return obj
        else:
            return obj.get_garrison()
