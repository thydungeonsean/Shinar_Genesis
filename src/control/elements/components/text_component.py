from element_component import ElementComponent
from src.control.font_draw import FontDraw
import pygame


class TextComponent(ElementComponent):

    def __init__(self, element, text):

        ElementComponent.__init__(self, element)
        self.text = text
        self.surface = pygame.Surface((element.w, element.h))

        self.update()

    def update(self):
        self.surface.fill((0, 10, 200))
        text_image = FontDraw.get_instance().create_fitted_text(self.text, (255, 0, 0), self.element.w,
                                                                self.element.h, transparent=True)
        self.surface.blit(text_image, (0, 0))

    def draw(self, surface):

        surface.blit(self.surface, self.element.screen_coord)
