from elements.player_banner import PlayerBanner
from elements.pass_button import PassButton
from elements.action_button import ActionButton
from elements.action_panel import ActionPanel

from elements.components.hightlight_component import HighlightComponent

from src.enum.actions import *


class UIController(object):

    # control object to issue commands to the ui

    def __init__(self, state):
        self.state = state
        self.ui = state.ui

    def add_player_banner(self, player):
        banner = PlayerBanner(self.ui, player)
        self.ui.add_element(banner)

    def add_pass_button(self):
        button = PassButton(self.ui)
        self.ui.add_element(button)

    def add_action_panel(self):

        panel = ActionPanel(self.ui)
        self.ui.add_element(panel)

        for i in range(len(test_actions)):
            b = ActionButton(self.ui, test_actions[i], i)
            self.ui.add_element(b)

    def clear_action_button(self, action_id):
        action_button = self.ui.get_element(action_names[action_id])
        action_button.remove_named_component('highlight')

    def highlight_action_button(self, action_id):

        action_button = self.ui.get_element(action_names[action_id])
        highlight = HighlightComponent(action_button)
        action_button.add_named_component(highlight, 'highlight')

