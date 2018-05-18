from player_structure import PlayerStructure
from src.enum.object_codes import GRANARY


class Granary(PlayerStructure):

    def __init__(self, state, coord, player):

        PlayerStructure.__init__(self, state, coord, player, GRANARY)

    def draw(self, surface):
        surface.blit(self.image, self.pixel_coord.int_position)
