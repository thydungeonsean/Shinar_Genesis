from military_action import MilitaryAction
from src.enum.actions import DEFEND_ACTION
from map_tools import get_army_defense_points


class DefendAction(MilitaryAction):

    def __init__(self, state, player):

        MilitaryAction.__init__(self, state, player, DEFEND_ACTION)

    def place_text(self):
        return 'Recruit Defenders'

    def select_text(self):
        return 'Mount a Defense'

    def activate_effect(self, point):

        self.selected_army.start_defend()

    # moving action
    def compute_valid_move_points(self):
        # points in range of selected army
        return get_army_defense_points(self.state, self.selected_army)