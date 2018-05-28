from element import Element
from components.border_component import BorderComponent
from components.text_component import TextComponent


class BuildChoiceCard(Element):

    w = 300
    h = 300

    buffer = 10

    def __init__(self, ui, i, text, func, parent):

        cls = BuildChoiceCard
        Element.__init__(self, ui, cls.w, cls.h, self.get_coord(i), parent=parent)
        self.text = text
        self.on_click = func

        self.initialize()

    def get_coord(self, i):
        y = i / 2
        x = i - y * 2
        return x * BuildChoiceCard.w + x * BuildChoiceCard.buffer, y * BuildChoiceCard.h + y * BuildChoiceCard.buffer

    def initialize(self):

        text = TextComponent(self, self.text)
        self.add_component(text)

        border = BorderComponent(self)
        self.add_component(border)
