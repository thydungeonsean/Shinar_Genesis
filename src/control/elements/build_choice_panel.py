from element import Element
from src.constants import DISPLAY_W, DISPLAY_H
from src.enum.object_codes import *
from build_choice_card import BuildChoiceCard

from components.border_component import BorderComponent


class BuildChoicePanel(Element):

    w = 600 + 10
    h = 600 + 10

    coord = (DISPLAY_W - w) / 2, (DISPLAY_H - h) / 2

    def __init__(self, ui, action):

        cls = BuildChoicePanel
        self.action = action
        Element.__init__(self, ui, cls.w, cls.h, cls.coord, parent='screen', el_id='build_choice_panel')
        self.initialize()

    def initialize(self):

        c = BorderComponent(self)
        self.add_component(c)

        def build_func(building_id):

            def build():
                self.action.choose_build_action(building_id)
            return build

        BuildChoiceCard(self.ui, 0, 'Begin Palace Construction', build_func(PALACE), self)
        BuildChoiceCard(self.ui, 1, 'Begin Ziggurat Construction', build_func(ZIGGURAT), self)
        BuildChoiceCard(self.ui, 2, 'Construct Tower', build_func(TOWER), self)
        BuildChoiceCard(self.ui, 3, 'Construct Granary', build_func(GRANARY), self)
