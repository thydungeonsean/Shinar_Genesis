from action_choice_card import ActionChoiceCard
from element import Element
from src.constants import DISPLAY_W, DISPLAY_H


class ActionChoicePanel(Element):

    w = 500 + 10
    h = 400

    coord = (DISPLAY_W - w) / 2, (DISPLAY_H - h) / 2

    def __init__(self, ui, action):

        cls = ActionChoicePanel
        self.action = action
        Element.__init__(self, ui, cls.w, cls.h, cls.coord, parent='screen', el_id='action_choice_panel')
        self.initialize()

    def initialize(self):

        ActionChoiceCard(self.ui, 0, self.action.place_text(), self.action.choose_place_action, self)
        ActionChoiceCard(self.ui, 1, self.action.select_text(), self.action.choose_select_action, self)