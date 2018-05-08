from base_state import BaseState
from src.control.template.strategic_input_handler import get_strategic_input_handler
from src.map.strategic_map import StrategicMap
from components.display import Display


class StrategicGameState(BaseState):

    def __init__(self, state_manager):  # TODO take map as arg

        BaseState.__init__(self, state_manager)
        self.input_handler = get_strategic_input_handler(self)
        self.map = StrategicMap(self)
        self.screen = None

        self.frame = 0

    def initialize(self):
        self.map.initialize()
        self.screen = Display.get_instance().display

    def handle_input(self):
        self.input_handler.handle()

    def draw_screen(self):
        self.map.draw(self.screen)

    def run(self):
        self.map.run()
        self.frame += 1
        if self.frame >= 120:
            self.frame = 0
