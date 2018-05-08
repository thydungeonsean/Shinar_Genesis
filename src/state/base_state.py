import pygame
from src.constants import FPS


class BaseState(object):

    def __init__(self, state_manager):

        self.state_manager = state_manager
        self.exit_state = False

        self.clock = pygame.time.Clock()

    def main(self):

        while self.running:

            self.handle_input()
            self.run()
            self.update_display()
            self.delay_frame()

    def iniialize(self):
        pass

    @property
    def running(self):
        return not self.exit_state

    def handle_input(self):
        pass

    def run(self):
        pass

    def update_display(self):
        self.draw_screen()
        pygame.display.update()

    def draw_screen(self):
        pass

    def delay_frame(self):

        self.clock.tick(FPS)

    def quit(self):
        self.state_manager.next_state = None
        self.exit_state = True
