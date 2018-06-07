from ai_controller import AIController
from human_controller import HumanController
from random import randint
from deck.player_deck import PlayerDeck


class Player(object):

    AI = 0
    HUMAN = 1

    id_state = 1000

    @classmethod
    def assign_player_id(cls):
        p_id = cls.id_state
        cls.id_state += randint(1, 255)
        return p_id

    def __init__(self, player_name, color, ai=False):

        self.name = player_name
        self.player_id = Player.assign_player_id()
        self.color = color
        if ai:
            self.controller_id = Player.AI
        else:
            self.controller_id = Player.HUMAN

        self.controller = self.load_controller()

        self.active_construction = None

        self.deck = PlayerDeck.default_deck()

    def load_controller(self):
        if self.controller_id == Player.AI:
            return AIController(self)
        else:
            return HumanController(self)

    def activate_controller(self):
        print self.name + ' activated'
        self.controller.activate()

    def deactivate_controller(self):
        self.controller.deactivate()

    def advance_construction(self):

        self.active_construction.advance_construction()
        if not self.active_construction.under_construction:
            self.active_construction = None

    def can_add_ziggurat(self):
        # has < 3 ziggurats
        return True

    # deck handle
    def get_hand(self):
        return self.deck.get_hand()

    def draw_hand(self):
        self.deck.draw_hand()

    def discard_hand(self):
        self.deck.discard_hand()
