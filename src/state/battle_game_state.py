from base_state import BaseState
from components.frame_counter import FrameCounter
from components.display import Display

from src.control.template.tactical_input_handler import load_tactical_input_handler
from src.control.template.tactical_ui import load_tactical_ui

from random import randint


class BattleGameState(BaseState):

    def __init__(self, state_manager, strategic_state, attacker, defender, attack_win_func, defender_win_func):

        self.strategic_state = strategic_state

        self.attacker = attacker
        self.defender = defender

        self.attacker_win_func = attack_win_func
        self.defender_win_func = defender_win_func

        BaseState.__init__(self, state_manager)
        self.ui = load_tactical_ui(self)
        self.input_handler = load_tactical_input_handler(self)
        self.screen = None

        self.frame_counter = FrameCounter(120)

        # instant coin flip battle
        self.instant = False

    @property
    def frame(self):
        return self.frame_counter.frame

    def initialize(self):
        self.screen = Display.get_instance().display
        self.screen.fill((0, 0, 0))
        if self.instant:
            if randint(0, 1) == 0:
                self.attacker_wins()
            else:
                self.defender_wins()

    def handle_input(self):
        self.input_handler.handle()

    def draw_screen(self):
        self.ui.draw(self.screen)

    def run(self):
        self.ui.run()
        self.frame_counter.run()

    def attacker_wins(self):

        self.attacker_win_func()
        self.complete_battle()

    def defender_wins(self):
        self.defender_win_func()
        self.complete_battle()

    def complete_battle(self):

        self.state_manager.next_state = self.strategic_state
        self.strategic_state.reset()
        self.exit_state = True
