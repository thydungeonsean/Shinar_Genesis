from state.state_manager import StateManager
from state.strategic_game_state import StrategicGameState


def main():

    game = StateManager(StrategicGameState)
    game.main()
