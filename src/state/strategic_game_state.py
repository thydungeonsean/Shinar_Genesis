from base_state import BaseState

from src.control.template.strategic_ui import load_strategic_ui
from src.control.template.strategic_input_handler import get_strategic_input_handler
from src.actions.action_controller import ActionController
from src.map.strategic_map import StrategicMap

from components.display import Display
from components.frame_counter import FrameCounter
from components.turn_controller import TurnController
from components.map_highlighter import MapHighlighter

from src.player.player import Player
from components.player_manager import PlayerManager


class StrategicGameState(BaseState):

    def __init__(self, state_manager):  # TODO take map as arg

        BaseState.__init__(self, state_manager)
        self.action_controller = ActionController(self)
        self.ui = load_strategic_ui(self)
        self.input_handler = get_strategic_input_handler(self)
        self.screen = None

        self.map = StrategicMap(self)
        self.player_manager = PlayerManager(self, Player('Player 1', (200, 0, 0)), Player('Player 2', (0, 0, 200)))
        self.turn_controller = TurnController(self)
        self.map_highlighter = MapHighlighter(self)

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
        self.map_highlighter.draw(self.screen)
        self.ui.draw(self.screen)

    def run(self):
        self.ui.run()
        self.map.run()
        self.map_highlighter.run()
        self.turn_controller.run()
        self.frame_counter.run()
