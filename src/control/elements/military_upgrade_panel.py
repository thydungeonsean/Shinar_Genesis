from element import Element
from src.constants import DISPLAY_W, DISPLAY_H

from components.border_component import BorderComponent
from components.text_component import TextComponent


class MilitaryUpgradePanel(Element):

    w = 600
    h = 500

    coord = (DISPLAY_W - w) / 2, (DISPLAY_H - h) / 2

    def __init__(self, ui, action, point):

        cls = MilitaryUpgradePanel
        self.action = action
        self.tower_point = point
        Element.__init__(self, ui, cls.w, cls.h, cls.coord, parent='screen', el_id='military_upgrade_panel')
        self.initialize()

    def initialize(self):

        # TODO this is a placeholder panel
        self.add_component(TextComponent(self, 'Upgrade Military'))
        self.add_component(BorderComponent(self))

    def on_click(self):
        self.action.build_tower(self.tower_point)
