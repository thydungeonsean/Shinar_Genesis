from element import Element
from components.border_component import BorderComponent
from components.text_component import TextComponent
from src.enum.actions import *


class ActionButton(Element):

    w = 200
    h = 100

    buffer = 10

    x = buffer
    base_y = buffer

    def __init__(self, ui, action_id, i):

        self.action_id = action_id
        self.action_name = action_names[action_id]
        cls = ActionButton
        Element.__init__(self, ui, cls.w, cls.h, (cls.x, self.get_y_coord(i)), parent='action_panel',
                         el_id=self.action_name)

        self.initialize()

    def initialize(self):

        text = TextComponent(self, self.action_name)
        self.add_component(text)

        border = BorderComponent(self)
        self.add_component(border)

    @staticmethod
    def get_y_coord(i):

        return ActionButton.base_y + i * ActionButton.h + i * ActionButton.buffer

    def on_click(self):

        self.ui.state.action_controller.button_clicked(self.action_id)
