import pygame
from pygame.locals import *
from src.control.click_handler import ClickHandler


class InputHandler(object):

    LEFT_BUTTON = 1
    RIGHT_BUTTON = 3

    def __init__(self, state, *listeners):

        self.state = state

        self.click_handler = ClickHandler(state)
        self.listeners = []
        self.listeners.extend(listeners)

    def handle(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.end_state()

            elif event.type == KEYDOWN:
                map(lambda x: x.check_key_down(event.key), self.listeners)

            elif event.type == KEYUP:
                map(lambda x: x.check_key_up(event.key), self.listeners)

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == InputHandler.LEFT_BUTTON:
                    self.click_handler.click()

            elif event.type == MOUSEBUTTONUP:
                pass

            elif event.type == MOUSEMOTION:
                pass

    def end_state(self):

        self.state.quit()
