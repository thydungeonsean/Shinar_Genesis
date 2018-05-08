from src.state.components.input_handler import InputHandler
from src.control.listener import Listener
from pygame.locals import *


def get_strategic_input_handler(state):

    return InputHandler(state,
                        Listener(K_UP, on_press=None),
                        Listener(K_DOWN, on_press=None),
                        Listener(K_LEFT, on_press=None),
                        Listener(K_RIGHT, on_press=None),

                        Listener(K_ESCAPE, on_press=state.quit)
                        )
