from military_action import MilitaryAction
from src.enum.actions import CONQUER_ACTION
from map_tools import get_army_movement_options, get_conquered_points, in_player_domain
from src.enum.object_codes import *


class ConquerAction(MilitaryAction):

    def __init__(self, state, player):

        MilitaryAction.__init__(self, state, player, CONQUER_ACTION)

    def place_text(self):
        return 'Raise Army'

    def select_text(self):
        return 'Conquer the land'

    # moving action
    def compute_valid_move_points(self):
        # points in range of selected army
        return get_army_movement_options(self.state, self.selected_army, conquer=True)

    def activate_effect(self, point):

        # if enemy building - attack it
        # else
        # get conquered points
        conquered = get_conquered_points(self.state, point)
        # spread dominion to those points
        map(self.extend_rule, conquered)

        # end action

    def extend_rule(self, point):
        self.state.map.dominion_map.add_dominion(self.player.player_id, point)

    # battle triggering helper methods
    def get_win_effect(self, point, defender):

        def win_effect():
            self.activate_effect(point)
            print 'attacker wins'
            # if defender is garrison, apply correct building conquer interaction
            if defender.is_garrison() and not defender.sallying:
                defender.rout()
                self.conquer_building(defender)
            else:
                defender.rout()

            # end point
            self.complete_action()

        return win_effect

    def conquer_building(self, garrison):

        building = garrison.building
        point = building.coord.int_position

        if building.obj_code in {TOWER, PALACE}:
            building.raze()

        elif building.obj_code == GRANARY:

            if in_player_domain(self.state, point):
                building.capture(self.player)
                self.selected_army.form_garrison(building)
            else:
                building.raze()

        elif building.obj_code == ZIGGURAT:
            if in_player_domain(self.state, point) and not building.under_construction and\
                    self.player.can_add_ziggurat():
                building.capture(self.player)
                self.selected_army.form_garrison(building)
            else:
                building.raze()
