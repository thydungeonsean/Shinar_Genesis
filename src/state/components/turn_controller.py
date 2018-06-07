from src.control.ui_controller import UIController


class TurnController(object):

    NEED_START = 0
    NEED_END = 1
    IN_PROGRESS = 2

    def __init__(self, state):

        self.state = state
        self.player_manager = self.state.player_manager
        self.turn_event_runner = self.state.turn_event_runner

        self.turn_state = TurnController.NEED_START

        self.run_state = {
            TurnController.NEED_START: self.start_turn,
            TurnController.NEED_END: self.end_turn,
            TurnController.IN_PROGRESS: self.run_turn,
        }

    @property
    def active_player(self):
        return self.player_manager.active_player

    def run(self):

        self.run_state[self.turn_state]()

    def run_turn(self):

        self.active_player.controller.run()

    def start_turn(self):

        # draw players hand
        self.active_player.draw_hand()
        print self.active_player.get_hand()

        # set up active player's displays
        # banner
        ui = UIController(self.state)
        ui.add_player_banner(self.active_player)

        # display player hand
        ui.add_hand_display()

        # pass button
        ui.add_pass_button()

        # turn on player's controller
        self.active_player.activate_controller()

        self.turn_state = TurnController.IN_PROGRESS

    def pass_turn(self):
        print 'pass'
        self.turn_state = TurnController.NEED_END

    def end_turn(self):

        ui_control = UIController(self.state)
        ui_control.close_hand_display()

        # tear down active player's display
        ui = self.state.ui
        ui.remove_element_by_key('player_banner')
        ui.remove_element_by_key('pass_button')

        # deactivate player controller
        self.active_player.deactivate_controller()
        self.state.action_controller.reset()
        self.state.hand_controller.reset()

        # run end of turn sequence
        self.turn_event_runner.run()

        # discard cards left in player's hand
        self.active_player.discard_hand()

        # cycle active player
        self.player_manager.cycle_to_next_player()

        self.turn_state = TurnController.NEED_START

        self.state.screen.fill((0, 0, 0))
