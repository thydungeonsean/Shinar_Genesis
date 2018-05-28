from constructed_game_object import ConstructedGameObject
from src.enum.object_codes import ZIGGURAT


class Ziggurat(ConstructedGameObject):

    def __init__(self, state, coord, player, new_construction=True):

        ConstructedGameObject.__init__(self, state, coord, player, new_construction, ZIGGURAT)

    def draw(self, surface):
        surface.blit(self.image, self.pixel_coord.int_position)

    def final_stage(self):
        return 3
