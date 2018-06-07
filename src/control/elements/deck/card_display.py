from ..element import Element
from ..components.border_component import BorderComponent
from ..components.text_component import TextComponent
from src.enum.actions import *


class CardDisplay(Element):

    w = 200
    h = 100

    buffer = 10

    x = buffer
    base_y = buffer

    def __init__(self, ui, action_id, i):

        self.action_id = action_id
        self.action_name = action_names[action_id]
        self.hand_pos = i
        cls = CardDisplay
        Element.__init__(self, ui, cls.w, cls.h, (cls.x, self.get_y_coord(i)), parent='hand_display',
                         el_id=self.get_card_element_id())
        self.initialize()

    def initialize(self):

        text = TextComponent(self, self.action_name)
        self.add_component(text)

        border = BorderComponent(self)
        self.add_component(border)

    def get_card_element_id(self):

        action = self.action_name
        hand_pos = str(self.hand_pos)
        return '-'.join((action, hand_pos))

    @staticmethod
    def get_y_coord(i):

        return CardDisplay.base_y + i * CardDisplay.h + i * CardDisplay.buffer

    def on_click(self):

        self.ui.state.hand_controller.click_card(self.hand_pos)
