import pygame
from pygame.locals import *


class InputHandler(object):

    def __init__(self, state, *listeners):

        self.state = state

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

    def end_state(self):

        self.state.quit()
