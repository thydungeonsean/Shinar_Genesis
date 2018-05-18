from element_component import ElementComponent
from src.colors import *
import pygame


class HighlightComponent(ElementComponent):

    def __init__(self, element, color=HIGHLIGHT):

        ElementComponent.__init__(self, element)
        self.rect = pygame.Rect((0, 0), (element.w, element.h))
        self.color = color

    def draw(self, surface):
        self.rect.topleft = self.element.screen_coord
        pygame.draw.rect(surface, self.color, self.rect, 1)
