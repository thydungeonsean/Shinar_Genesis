from src.constants import DISPLAY_W, DISPLAY_H
import pygame


class Display(object):

    instance = None

    @classmethod
    def get_instance(cls):

        if cls.instance is None:
            cls.instance = cls()

        return cls.instance

    def __init__(self):

        pygame.init()
        self.display = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
