from src.data_structures.vector import Vector
from src.constants import TILE_SIZE
import pygame
from garrison.garrison_generator import load_garrison


class GameObject(object):

    START_COLOR = (127, 127, 127)

    def __init__(self, state, coord, obj_code, player):

        self.obj_code = obj_code
        self.owner_id = None
        self.state = state
        self.coord = Vector(coord)
        self.pixel_coord = Vector()
        self.image = None

        self.garrison = load_garrison(self, player)

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

    def change_color(self, old, new):

        px_array = pygame.PixelArray(self.image)
        px_array.replace(old, new)
        self.color = new

    def get_garrison(self):
        return self.garrison

    def capture(self, new_owner):
        self.owner_id = new_owner.player_id
        self.change_color(self.color, new_owner.color)

    def raze(self):
        self.state.map.game_object_map.remove_game_object(self)
        print 'building razed'

    def end_defend(self):
        pass
