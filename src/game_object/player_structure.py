from game_object import GameObject
from src.enum.object_codes import *


class PlayerStructure(GameObject):

    def __init__(self, state, coord, player, obj_code):

        GameObject.__init__(self, state, coord, obj_code)

        self.owner_id = player.player_id
        self.color = player.color
        self.image = self.load_image(object_names[self.obj_code])
        self.change_color(self.color)

    def draw(self, surface):
        surface.blit(self.image, self.pixel_coord.int_position)
