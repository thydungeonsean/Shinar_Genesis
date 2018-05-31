from src.enum.actions import *
from plant_action import PlantAction
from harvest_action import HarvestAction
from rule_action import RuleAction
from raid_action import RaidAction
from defend_action import DefendAction
from conquer_action import ConquerAction
from build_aciton import BuildAction


actions = {
    PLANT_ACTION: PlantAction,
    HARVEST_ACTION: HarvestAction,
    RAISE_ACTION: PlantAction,
    MOVE_ACTION: PlantAction,
    RULE_ACTION: RuleAction,
    RAID_ACTION: RaidAction,
    DEFEND_ACTION: DefendAction,
    CONQUER_ACTION: ConquerAction,
    BUILD_ACTION: BuildAction,
}


def load_action(action_id, state):

    player = state.player_manager.active_player

    return actions[action_id](state, player)
