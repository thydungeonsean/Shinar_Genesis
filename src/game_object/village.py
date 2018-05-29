from player_game_object import PlayerGameObject
from src.enum.object_codes import VILLAGE
from src.constants import TILE_SIZE
import pygame
from src.player.neutral_player import NeutralPlayer


class Village(PlayerGameObject):

    o = 10
    hut_pos = ((o, o), (TILE_SIZE-o, o), (o, TILE_SIZE-o), (TILE_SIZE-o, TILE_SIZE-o), (TILE_SIZE/2, TILE_SIZE/2))

    def __init__(self, state, coord, size):

        PlayerGameObject.__init__(self, state, coord, NeutralPlayer.get_instance(), VILLAGE)
        self.size = size
        self.happiness = 80

        self.hut_image = pygame.Surface((3, 3)).convert()
        self.hut_image.fill((255, 255, 255))
        self.hut_rect = self.hut_image.get_rect()

    def grow(self, n):
        self.size += n
        if self.size > 5:
            self.size -= 5  # colonize n - 5

    def shrink(self, n):
        self.size -= n
        if self.size <= 0:
            pass  # disband village

    def draw(self, surface):

        pos = self.pixel_coord.int_position

        for i in range(self.size):
            self.draw_hut(pos, i, surface)

    def draw_hut(self, (x, y), i, surface):

        hx, hy = Village.hut_pos[i]
        x += hx
        y += hy

        self.hut_rect.center = (x, y)

        surface.blit(self.hut_image, self.hut_rect)

    def update_color(self, color):
        pass

    def change_color(self, old, new):
        pass

    def object_image_name(self):
        return None

    def load_image(self, id):
        pass
