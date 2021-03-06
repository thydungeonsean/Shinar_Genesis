from src.state.components.input_handler import InputHandler
from src.control.listener import Listener
from src.control.strategic_click_handler import StrategicClickHandler
from pygame.locals import *


def load_strategic_input_handler(state):

    input = InputHandler(state,
                        Listener(K_UP, on_press=None),
                        Listener(K_DOWN, on_press=None),
                        Listener(K_LEFT, on_press=None),
                        Listener(K_RIGHT, on_press=None),

                        Listener(K_ESCAPE, on_press=state.quit)
                        )

    input.click_handler = StrategicClickHandler(state)

    return input
