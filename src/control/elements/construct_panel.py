from element import Element
from src.constants import DISPLAY_W, DISPLAY_H

from components.border_component import BorderComponent
from components.text_component import TextComponent


class ConstructPanel(Element):

    w = 250
    h = 250

    coord = (DISPLAY_W - w) / 2, (DISPLAY_H - h) / 2

    def __init__(self, ui, action, project):

        cls = ConstructPanel
        self.action = action
        Element.__init__(self, ui, cls.w, cls.h, cls.coord, parent='screen', el_id='build_choice_panel')
        self.initialize()

    def initialize(self):

        self.add_component(TextComponent(self, 'Construct'))
        self.add_component(BorderComponent(self))

    def on_click(self):
        self.action.construct_action()

