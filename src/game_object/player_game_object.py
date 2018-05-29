from game_object import GameObject
from src.enum.object_codes import *


class PlayerGameObject(GameObject):

    def __init__(self, state, coord, player, obj_code):

        GameObject.__init__(self, state, coord, obj_code, player)

        self.owner_id = self.load_player_id(player)
        self.color = self.load_color(player)
        self.image = self.load_image(self.object_image_name())
        self.change_color(PlayerGameObject.START_COLOR, self.color)

    def draw(self, surface):
        surface.blit(self.image, self.pixel_coord.int_position)

    def object_image_name(self):
        return object_names[self.obj_code]

    def load_player_id(self, player):
        return player.player_id

    def load_color(self, player):
        return player.color

    def update_color(self, new_color):
        self.change_color(self.color, new_color)
