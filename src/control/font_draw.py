import pygame
from src.constants import SCALE
from src.colors import BLACK


class FontDraw(object):

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    def __init__(self):
        self.font = pygame.font.Font('assets/font/oryxtype.ttf', 16)

    def create_text_image(self, text, color, scale=True):
        font_image = self.font.render(text, False, color)
        r = font_image.get_rect()
        adj = pygame.Surface((r.w, r.h-1))
        adj.blit(font_image, (0, -1))
        r = adj.get_rect()

        if scale:
            if SCALE <= 2:

                return pygame.transform.scale(adj, (r.w * SCALE, r.h * SCALE))

            else:
                return pygame.transform.scale(adj, (r.w * 2, r.h * 2))
        else:
            return adj

    def create_fitted_text(self, text, color, final_w, final_h, background=BLACK, transparent=False):

        text = self.create_text_image(text, color)

        w = text.get_width()
        h = text.get_height()

        final_coord = (final_w - w) / 2, (final_h - h) / 2 - 3

        final_image = pygame.Surface((final_w, final_h)).convert()
        final_image.fill(background)
        final_image.blit(text, final_coord)

        if transparent:
            final_image.set_colorkey(background)

        return final_image
