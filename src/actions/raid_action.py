from military_action import MilitaryAction
from src.enum.actions import RAID_ACTION
from map_tools import get_raided_points


class RaidAction(MilitaryAction):

    def __init__(self, state, player):

        MilitaryAction.__init__(self, state, player, RAID_ACTION)

    def place_text(self):
        return 'Muster Raiders'

    def select_text(self):
        return 'Send a Raid'

    def activate_effect(self, point):

        # get raided points
        raided = get_raided_points(self.state, point)
        # raid points
        map(self.raid_point, raided)
        # end action

    def raid_point(self, point):
        # remove farm at point
        self.state.map.farm_map.remove_farm(point)
