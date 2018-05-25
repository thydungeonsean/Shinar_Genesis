from element import Element
from components.border_component import BorderComponent
from components.text_component import TextComponent


class ActionChoiceCard(Element):

    w = 250
    h = 400

    buffer = 10

    def __init__(self, ui, i, text, func, parent):

        cls = ActionChoiceCard
        Element.__init__(self, ui, cls.w, cls.h, self.get_coord(i), parent=parent)
        self.text = text
        self.on_click = func

        self.initialize()

    def get_coord(self, i):

        return i * ActionChoiceCard.w + i * ActionChoiceCard.buffer, 0

    def initialize(self):

        text = TextComponent(self, self.text)
        self.add_component(text)

        border = BorderComponent(self)
        self.add_component(border)
