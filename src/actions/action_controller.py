from src.enum.actions import *
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
        for action_id in action_names.keys():
            table[action_id] = False

        return table

    def select_action(self, action_id):

        self.action_table[action_id] = True

        # set as active action
        self.load_action(action_id)

        # highlight valid_tiles
        self.highlight_tiles()

    def deselect_action(self, action_id):

        if self.action_table[action_id]:
            self.action_table[action_id] = False

            self.action.deinitialize_action()
            self.action = None
            self.clear_tile_highlights()

    def load_action(self, action_id):

        self.action = load_action(action_id, self.state)

    def highlight_tiles(self):

        self.state.map_highlighter.highlight(self.action)

    def clear_tile_highlights(self):
        self.state.map_highlighter.clear_highlight()

    def reset(self):
        # called at end of turn process

        for action_id in action_names.keys():
            if self.action_table[action_id]:
                self.deselect_action(action_id)
