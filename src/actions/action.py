from src.enum.actions import *
from src.constants import DEV_MODE_ACTION_COMPLETION


class Action(object):

    def __init__(self, state, player, action_id):

        # TODO player is an unnecessary parameter here?

        self.state = state
        self.player = player
        self.action_id = action_id
        self.action_name = action_names[action_id]
        self.valid_points = None

        self.initialize_action()

    def initialize_action(self):
        self.compute_valid_points()

    def deinitialize_action(self):
        pass

    def compute_valid_points(self):

        self.valid_points = set(filter(lambda x: self.point_is_valid(x), self.state.map.tile_map.all_points))

    def point_is_valid(self, (x, y)):
        return True

    def perform_action(self, point):
        if point in self.valid_points:
            print self.action_name + ' performed successfully at ' + str(point)

    def highlight_tiles(self):
        self.state.action_controller.highlight_tiles()

    def null_action(self, point):
        pass

    def complete_action(self):

        if not DEV_MODE_ACTION_COMPLETION:

            self.state.turn_controller.pass_turn()
