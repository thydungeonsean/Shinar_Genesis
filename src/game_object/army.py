from player_game_object import PlayerGameObject
from src.enum.object_codes import ARMY


class Army(PlayerGameObject):

    def __init__(self, state, coord, player):

        PlayerGameObject.__init__(self, state, coord, player, ARMY)

        self.roster = []
        self.speed = 10

    def object_image_name(self):
        return 'raider'

    def move(self, point):
        self.coord.set_from_tuple(point)
        self.set_position()
