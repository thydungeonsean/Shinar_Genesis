from components.display import Display
from battle_game_state import BattleGameState


class StateManager(object):

    def __init__(self, initial):

        Display.get_instance()
        self.current_state = initial(self)
        self.next_state = None

    def initialize(self):
        self.current_state.initialize()

    @property
    def running(self):
        return self.current_state is not None

    def main(self):

        while self.running:

            self.initialize()
            self.current_state.main()

            self.current_state = self.load_next_state()

    def load_next_state(self):

        return self.next_state

    def assign_next_state(self, next_state):

        self.next_state = next_state

    def create_battle(self, strategic_state, attacker, defender, attacker_win, defender_win):

        self.next_state = BattleGameState(self, strategic_state, attacker, defender, attacker_win, defender_win)
