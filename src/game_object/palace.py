from game_object import GameObject
from src.enum.object_codes import PALACE


class Palace(GameObject):

    def __init__(self, state, coord, player):

        GameObject.__init__(self, state, coord, PALACE)

        self.owner_id = player.player_id
        self.color = player.color
        self.image = self.load_image('palace')
        self.change_color(self.color)

    def draw(self, surface):
        surface.blit(self.image, self.pixel_coord.int_position)
