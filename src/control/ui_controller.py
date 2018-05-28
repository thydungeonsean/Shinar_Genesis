from elements.player_banner import PlayerBanner
from elements.pass_button import PassButton
from elements.action_button import ActionButton
from elements.action_panel import ActionPanel

from elements.action_choice_panel import ActionChoicePanel
from elements.build_choice_panel import BuildChoicePanel
from elements.construct_panel import ConstructPanel

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

    # military actions
    def open_action_choice_panels(self, action):

        def adder():
            action_choices = ActionChoicePanel(self.ui, action)
            self.ui.add_element(action_choices)

        self.ui.queue_element(adder)

    def close_action_choice_panels(self, action):

        self.ui.dequeue_element_by_key('action_choice_panel')

    # build action
    def open_build_choice_panels(self, player, action):

        if player.active_construction is not None:

            def adder():
                construct = ConstructPanel(self.ui, action, player.active_construction)
                self.ui.add_element(construct)

        else:

            def adder():
                build_choices = BuildChoicePanel(self.ui, action)
                self.ui.add_element(build_choices)

        self.ui.queue_element(adder)

    def close_build_choice_panels(self, action):

        self.ui.dequeue_element_by_key('build_choice_panel')
