from military_action import MilitaryAction
from src.enum.actions import CONQUER_ACTION
from map_tools import get_army_movement_options, get_conquered_points


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
        print 'conquer ' + str(point)

        # if enemy building - attack it
        # else
        # get conquered points
        conquered = get_conquered_points(self.state, point)
        # spread dominion to those points
        map(self.extend_rule, conquered)

        # end action

    def extend_rule(self, point):
        self.state.map.dominion_map.add_dominion(self.player.player_id, point)
