from player_game_object import PlayerGameObject
import pygame
from src.enum.object_codes import object_names


class ConstructedGameObject(PlayerGameObject):

    def __init__(self, state, coord, player, new_construction, obj_id):

        self.under_construction = new_construction
        self.stage = self.set_construction_stage()
        PlayerGameObject.__init__(self, state, coord, player, obj_id)
        self.update_image()

    def set_construction_stage(self):

        if self.under_construction:
            return 1
        else:
            return self.final_stage()

    def final_stage(self):
        raise NotImplementedError

    def object_image_name(self):
        obj_name = object_names[self.obj_code]
        if self.under_construction:
            obj_name = obj_name + '_con' + str(self.stage)

        return obj_name

    def advance_construction(self):

        self.stage += 1
        if self.stage == self.final_stage():
            self.under_construction = False

        self.update_image()

    def update_image(self):
        self.image = self.load_image(self.object_image_name())
        self.change_color(ConstructedGameObject.START_COLOR, self.color)

    def update_color(self, color):

        px_array = pygame.PixelArray(self.image)
        px_array.replace(ConstructedGameObject.START_COLOR, color)
