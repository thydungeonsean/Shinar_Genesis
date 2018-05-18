from element import Element
from components.text_component import TextComponent
from components.border_component import BorderComponent
from src.constants import *


class PassButton(Element):

    w = 100
    h = 30

    x = (DISPLAY_W / 2) + (DISPLAY_W / 4)
    y = DISPLAY_H - h

    def __init__(self, ui):
        cls = PassButton
        Element.__init__(self, ui, cls.w, cls.h, (cls.x, cls.y), parent='screen', el_id='pass_button')
        self.state = ui.state
        self.initialize()

    def initialize(self):

        text = TextComponent(self, 'Pass')
        self.add_component(text)

        border = BorderComponent(self)
        self.add_component(border)

    def on_click(self):
        self.state.turn_controller.pass_turn()
