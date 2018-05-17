

class TurnController(object):

    def __init__(self, state):

        self.state = state
        self.player_manager = self.state.player_manager

    def initialize(self):

        self.start_turn()

    @property
    def active_player(self):
        return self.player_manager.active_player

    def run(self):

        self.active_player.controller.run()

    def start_turn(self):

        # set up active player's displays
        # banner
        # options

        # turn on player's controller
        self.active_player.activate_controller()

        pass
