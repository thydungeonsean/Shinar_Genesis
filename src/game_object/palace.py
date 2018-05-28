from constructed_game_object import ConstructedGameObject
from src.enum.object_codes import PALACE


class Palace(ConstructedGameObject):

    def __init__(self, state, coord, player, new_construction=True):

        ConstructedGameObject.__init__(self, state, coord, player, new_construction, PALACE)

    def draw(self, surface):
        surface.blit(self.image, self.pixel_coord.int_position)

    def final_stage(self):
        return 2
