from src.constants import DISPLAY_W, DISPLAY_H
from src.control.elements.element import Element
from ..ui import UI
from src.control.elements.components.text_component import TextComponent
from src.control.elements.player_banner import PlayerBanner


def load_strategic_ui(state):

    s_ui = UI(state)

    base_screen = Element(s_ui, DISPLAY_W, DISPLAY_H, el_id='screen')
    s_ui.add_element(base_screen)

    # e1 = PlayerBanner(s_ui, '1')
    # s_ui.add_element(e1)

    return s_ui
