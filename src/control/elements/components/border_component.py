from element_component import ElementComponent
from src.colors import *
import pygame


class BorderComponent(ElementComponent):

    def __init__(self, element, color=WHITE):

        ElementComponent.__init__(self, element)
        self.rect = pygame.Rect((10, 10), (element.w, element.h))
        self.color = color

    def draw(self, surface):
        self.rect.topleft = self.element.screen_coord
        pygame.draw.rect(surface, self.color, self.rect, 1)
