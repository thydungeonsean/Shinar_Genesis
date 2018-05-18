from element import Element
from src.constants import *


class ActionPanel(Element):

    n = 4
    buffer = 10

    w = 200 + buffer * 2
    h = ((100+buffer) * n) + (n+1 * buffer)

    x = DISPLAY_W - w
    y = (DISPLAY_H - h) / 2
    coord = x, y

    def __init__(self, ui):

        cls = ActionPanel
        Element.__init__(self, ui, cls.w, cls.h, cls.coord, el_id='action_panel')
