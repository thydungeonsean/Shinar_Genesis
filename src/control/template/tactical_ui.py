from src.constants import DISPLAY_W, DISPLAY_H
from src.control.elements.element import Element
from ..ui import UI

from ..elements.components.text_component import TextComponent


def load_tactical_ui(state):

    tac_ui = UI(state)

    base_screen = Element(tac_ui, DISPLAY_W, DISPLAY_H, el_id='screen')
    tac_ui.add_element(base_screen)

    label = Element(tac_ui, 100, 100, coord=(10, 10), parent='screen')
    label.add_component(TextComponent(label, 'battle'))

    # temp for testing
    attacker_win = Element(tac_ui, 200, 100, coord=(300, 200), parent='screen')
    attacker_win.add_component(TextComponent(attacker_win, 'Attacker Victory'))
    attacker_win.on_click = state.attacker_wins

    defender_win = Element(tac_ui, 200, 100, coord=(300, 310), parent='screen')
    defender_win.add_component(TextComponent(defender_win, 'Defender Victory'))
    defender_win.on_click = state.defender_wins

    return tac_ui
