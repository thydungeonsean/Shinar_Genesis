import pygame
from src.colors import BLACK, WHITE
from src.constants import TILE_SIZE


class BorderImage(object):

    initialized = False

    base_images = [{}, {}, {}, {}]

    @classmethod
    def init(cls):

        for i in range(4):
            cls.load_border_images(i)

    @classmethod
    def load_border_images(cls, i):

        seg_size = TILE_SIZE/2

        sheet = pygame.image.load('assets/border.png')
        rect = pygame.Rect((0, 0), (seg_size, seg_size))

        a = pygame.Surface((seg_size, seg_size))
        a.blit(sheet, (0, 0), rect)
        cls.base_images[i]['a'] = a

        rect.topleft = (seg_size, 0)
        b = pygame.Surface((seg_size, seg_size))
        b.blit(sheet, (0, 0), rect)
        cls.base_images[i]['b'] = b

        rect.topleft = (seg_size*2, 0)
        c = pygame.Surface((seg_size, seg_size))
        c.blit(sheet, (0, 0), rect)
        cls.base_images[i]['c'] = c

        for r in range(i):

            for k in ('a', 'b', 'c'):

                cls.base_images[i][k] = pygame.transform.rotate(cls.base_images[i][k], -90)

    def __init__(self, img_code):

        if not BorderImage.initialized:
            BorderImage.init()

        self.img_code = img_code

        self.surface = self.initialize_image()
        self.color = BLACK

    def draw(self, surface, point):

        surface.blit(self.surface, point)

    def recolor(self, new_color):

        px_array = pygame.PixelArray(self.surface)
        px_array.replace(self.color, new_color)

        self.color = new_color

    def initialize_image(self):

        img = pygame.Surface((TILE_SIZE, TILE_SIZE)).convert()
        img.fill(WHITE)

        point = [(0, 0), (TILE_SIZE/2, 0), (TILE_SIZE/2, TILE_SIZE/2), (0, TILE_SIZE/2)]

        for i in range(4):
            k = self.img_code[i]
            if k == '-':
                pass
            else:
                img.blit(BorderImage.base_images[i][k], point[i])

        img.set_colorkey(WHITE)
        img.set_alpha(200)

        return img
