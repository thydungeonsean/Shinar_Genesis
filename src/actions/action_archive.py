from src.enum.actions import *
from plant_action import PlantAction
from harvest_action import HarvestAction
from rule_action import RuleAction
from raid_action import RaidAction
from conquer_action import ConquerAction


actions = {
    PLANT_ACTION: PlantAction,
    HARVEST_ACTION: HarvestAction,
    RAISE_ACTION: PlantAction,
    MOVE_ACTION: PlantAction,
    RULE_ACTION: RuleAction,
    RAID_ACTION: RaidAction,
    CONQUER_ACTION: ConquerAction,
}


def load_action(action_id, state):

    player = state.player_manager.active_player

    return actions[action_id](state, player)
