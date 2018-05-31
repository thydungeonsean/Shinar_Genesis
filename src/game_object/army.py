from player_game_object import PlayerGameObject
from src.enum.object_codes import ARMY


class Army(PlayerGameObject):

    def __init__(self, state, coord, player):

        PlayerGameObject.__init__(self, state, coord, player, ARMY)

        self.roster = []
        self.speed = 10
        self.guarding = False

    def object_image_name(self):
        return 'raider'

    def move(self, point):
        self.coord.set_from_tuple(point)
        self.set_position()

        self.end_defend()

    def rout(self):
        self.remove_army()
        self.end_defend()
        print 'routed'

    def remove_army(self):
        self.state.map.game_object_map.remove_game_object(self)

    def get_garrison(self):
        raise Exception("Army object is being asked for garrison")

    def is_garrison(self):
        return False

    def raze(self):
        raise Exception("can't raze an army")

    def form_garrison(self, building):

        self.remove_army()

    def start_defend(self):
        self.guarding = True
        self.state.map.guard_map.log_update(self.owner_id)

    def end_defend(self):
        self.guarding = False
        self.state.map.guard_map.log_update(self.owner_id)
