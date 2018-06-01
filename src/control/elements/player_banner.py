from element import Element
from components.text_component import TextComponent
from src.constants import *
from components.border_component import BorderComponent


class PlayerBanner(Element):

    w = 100
    h = 30

    x = (DISPLAY_W / 2) + (DISPLAY_W / 4)
    y = 0

    def __init__(self, ui, player):

        cls = PlayerBanner
        Element.__init__(self, ui, cls.w, cls.h, (cls.x, cls.y), 'screen', 'player_banner')
        self.text = player.name
        self.color = player.color
        self.initialize()

    def initialize(self):

        text = TextComponent(self, self.text, self.color)
        self.add_component(text)

        border = BorderComponent(self)
        self.add_component(border)
