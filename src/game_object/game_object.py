from src.data_structures.vector import Vector
from src.constants import TILE_SIZE
import pygame


class GameObject(object):

    def __init__(self, state, coord, obj_code):

        self.obj_code = obj_code
        self.state = state
        self.coord = Vector(coord)
        self.pixel_coord = Vector()
        self.image = None

        self.set_position()

    def run(self):
        pass

    def draw(self, surface):
        pass

    def set_position(self):
        x, y = self.coord.position
        x *= TILE_SIZE
        y *= TILE_SIZE
        self.pixel_coord.set_position(x, y)

    def load_image(self, id):
        i = pygame.image.load(''.join(('assets/', id, '.png'))).convert()
        i.set_colorkey((255, 255, 255))

        return i

    def change_color(self, c):

        px_array = pygame.PixelArray(self.image)
        px_array.replace((127, 127, 127), c)
