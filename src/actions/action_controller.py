from src.enum.actions import *
from src.control.ui_controller import UIController

from action_archive import load_action


class ActionController(object):

    def __init__(self, state):

        self.state = state

        self.action_table = self.init_action_table()

        self.action = None

    @property
    def action_ready(self):
        return self.action is not None

    def init_action_table(self):

        table = {}
        for action_id in test_actions:
            table[action_id] = False

        return table

    def button_clicked(self, action_id):

        print action_names[action_id]

        if self.action_table[action_id]:
            self.deselect_action(action_id)
        else:
            self.clear_actions()
            self.select_action(action_id)

    def deselect_action(self, action_id):

        self.action_table[action_id] = False
        # clear highlight on button etc.
        ui = UIController(self.state)
        ui.clear_action_button(action_id)

        self.action = None
        self.state.map_highlighter.clear_highlight()

    def select_action(self, action_id):

        self.action_table[action_id] = True

        # highlight button etc.
        ui = UIController(self.state)
        ui.highlight_action_button(action_id)

        # set as active action
        self.load_action(action_id)

        # highlight valid_tiles
        self.state.map_highlighter.highlight(self.action)

    def clear_actions(self):

        for action_id in test_actions:
            if self.action_table[action_id]:
                self.deselect_action(action_id)

    def reset(self):
        self.clear_actions()

    def load_action(self, action_id):

        self.action = load_action(action_id, self.state)
