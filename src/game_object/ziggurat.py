from player_structure import PlayerStructure
from src.enum.object_codes import ZIGGURAT


class Ziggurat(PlayerStructure):

    def __init__(self, state, coord, player):

        PlayerStructure.__init__(self, state, coord, player, ZIGGURAT)

    def draw(self, surface):
        surface.blit(self.image, self.pixel_coord.int_position)
