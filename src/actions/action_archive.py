from src.enum.actions import *
from plant_action import PlantAction
from harvest_action import HarvestAction
from rule_action import RuleAction


actions = {
    PLANT_ACTION: PlantAction,
    HARVEST_ACTION: HarvestAction,
    RAISE_ACTION: PlantAction,
    MOVE_ACTION: PlantAction,
    RULE_ACTION: RuleAction,
}


def load_action(action_id, state):

    player = state.player_manager.active_player

    return actions[action_id](state, player)
