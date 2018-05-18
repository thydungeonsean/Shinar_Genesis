from src.enum.actions import *
from plant_action import PlantAction


actions = {
    PLANT_ACTION: PlantAction,
    HARVEST_ACTION: PlantAction,
    RAISE_ACTION: PlantAction,
    MOVE_ACTION: PlantAction,
}


def load_action(action_id, state):

    player = state.player_manager.active_player

    return actions[action_id](state, player)
