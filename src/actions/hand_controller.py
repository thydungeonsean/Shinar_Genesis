from src.enum.actions import *
from src.control.ui_controller import UIController


HAND_SIZE = 4


class HandController(object):

    def __init__(self, state):

        self.state = state
        self.action_controller = state.action_controller

        self.card_selection_table = {x: False for x in range(HAND_SIZE)}

        self.selected_card_handle = None

    @property
    def active_hand(self):
        return self.state.player_manager.active_player.get_hand()

    def click_card(self, hand_pos):

        action_id = self.active_hand[hand_pos]
        print action_names[action_id]

        if self.card_selection_table[hand_pos]:
            self.deselect_card(hand_pos)
        else:
            self.deselect_all_cards()
            self.select_card(hand_pos)

    def select_card(self, hand_pos):

        self.card_selection_table[hand_pos] = True
        action_id = self.active_hand[hand_pos]

        # highlight card etc.
        ui = UIController(self.state)
        ui.highlight_card(action_id, hand_pos)
        # TODO just grab carddisplay object and call highlight on it

        self.action_controller.select_action(action_id)

    def deselect_card(self, hand_pos):

        self.card_selection_table[hand_pos] = False
        action_id = self.active_hand[hand_pos]

        # clear highlight on card
        ui = UIController(self.state)
        ui.clear_card_highlight(action_id, hand_pos)
        # TODO grab card display object and call highlight_off on it

        self.action_controller.deselect_action(action_id)

    def deselect_all_cards(self):
        print 'here'
        for i in range(len(self.active_hand)):
            if self.card_selection_table[i]:
                self.deselect_card(i)

    def reset(self):
        self.deselect_all_cards()
