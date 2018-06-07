from elements.player_banner import PlayerBanner
from elements.pass_button import PassButton
# hand
from elements.deck.hand_display import HandDisplay
from elements.deck.card_display import CardDisplay

from elements.action_choice_panel import ActionChoicePanel
from elements.build_choice_panel import BuildChoicePanel
from elements.construct_panel import ConstructPanel
from elements.military_upgrade_panel import MilitaryUpgradePanel

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

    # def clear_action_button(self, action_id):
    #     action_button = self.ui.get_element(action_names[action_id])
    #     action_button.remove_named_component('highlight')
    #
    # def highlight_action_button(self, action_id):
    #
    #     action_button = self.ui.get_element(action_names[action_id])
    #     highlight = HighlightComponent(action_button)
    #     action_button.add_named_component(highlight, 'highlight')

    def highlight_card(self, action_id, hand_pos):
        card = self.ui.get_element(self.get_action_card_element_id(action_id, hand_pos))
        highlight = HighlightComponent(card)
        card.add_named_component(highlight, 'highlight')

    def clear_card_highlight(self, action_id, hand_pos):
        card = self.ui.get_element(self.get_action_card_element_id(action_id, hand_pos))
        card.remove_named_component('highlight')

    @staticmethod
    def get_action_card_element_id(action_id, hand_pos):
        action = action_names[action_id]
        hand_pos = str(hand_pos)
        return '-'.join((action, hand_pos))

    #############################################################################
    # HAND DISPLAY
    #################
    def add_hand_display(self):

        panel = HandDisplay(self.ui)
        self.ui.add_element(panel)

        hand = self.state.player_manager.active_player.get_hand()

        for i in range(len(hand)):
            b = CardDisplay(self.ui, hand[i], i)
            self.ui.add_element(b)

    def close_hand_display(self):
        self.ui.remove_element_by_key('hand_display')

    # military actions
    def open_action_choice_panels(self, action):

        def adder():
            action_choices = ActionChoicePanel(self.ui, action)
            self.ui.add_element(action_choices)

        self.ui.queue_element(adder)

    def close_action_choice_panels(self):

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

    def close_build_choice_panels(self):

        self.ui.dequeue_element_by_key('build_choice_panel')

    def open_military_upgrade_panel(self, action, point):

        def adder():
            upgrade = MilitaryUpgradePanel(self.ui, action, point)
            self.ui.add_element(upgrade)

        self.ui.queue_element(adder)

    def close_military_upgrade_panel(self):
        self.ui.dequeue_element_by_key('military_upgrade_panel')
