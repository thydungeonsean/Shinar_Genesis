from player_game_object import PlayerGameObject
from src.enum.object_codes import PALACE


class Palace(PlayerGameObject):

    def __init__(self, state, coord, player):

        PlayerGameObject.__init__(self, state, coord, player, PALACE)

    def draw(self, surface):
        surface.blit(self.image, self.pixel_coord.int_position)
