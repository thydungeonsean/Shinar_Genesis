from player_game_object import PlayerGameObject
from src.enum.object_codes import TOWER


class Tower(PlayerGameObject):

    def __init__(self, state, coord, player):

        PlayerGameObject.__init__(self, state, coord, player, TOWER)
        self.guarding = False

    def draw(self, surface):
        surface.blit(self.image, self.pixel_coord.int_position)

    def start_defend(self):
        self.guarding = True
        self.state.map.guard_map.log_update(self.owner_id)

    def end_defend(self):
        self.guarding = False
        self.state.map.guard_map.log_update(self.owner_id)

    def raze(self):
        self.state.map.game_object_map.remove_game_object(self)
        print 'tower razed'
        self.end_defend()
