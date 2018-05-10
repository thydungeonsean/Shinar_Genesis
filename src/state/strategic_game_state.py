from base_state import BaseState
from src.control.template.strategic_input_handler import get_strategic_input_handler
from src.map.strategic_map import StrategicMap
from components.display import Display
from components.frame_counter import FrameCounter

from src.player.player import Player


class StrategicGameState(BaseState):

    def __init__(self, state_manager):  # TODO take map as arg

        BaseState.__init__(self, state_manager)
        self.input_handler = get_strategic_input_handler(self)
        self.screen = None

        self.map = StrategicMap(self)
        self.players = [Player(1, (200, 0, 0)), Player(2, (0, 200, 0))]

        self.frame_counter = FrameCounter(120)

    @property
    def frame(self):
        return self.frame_counter.frame

    def initialize(self):
        self.map.initialize()
        self.screen = Display.get_instance().display

    def handle_input(self):
        self.input_handler.handle()

    def draw_screen(self):
        self.map.draw(self.screen)

    def run(self):
        self.map.run()
        self.frame_counter.run()
