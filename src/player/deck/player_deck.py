from random import shuffle
from src.enum.actions import *


class PlayerDeck(object):

    HAND_SIZE = 4

    @classmethod
    def default_deck(cls):
        deck = cls([PLANT_ACTION, PLANT_ACTION, HARVEST_ACTION, RULE_ACTION, RAID_ACTION, BUILD_ACTION, CONQUER_ACTION,
                    ])
        # deck = cls([PLANT_ACTION,PLANT_ACTION,PLANT_ACTION,PLANT_ACTION,PLANT_ACTION,PLANT_ACTION,BUILD_ACTION,])
        return deck

    def __init__(self, start_deck=[]):

        self.deck = start_deck
        self.discard = []
        self.hand = []

        shuffle(self.deck)

    # API
    def draw_hand(self):
        self.draw_cards(PlayerDeck.HAND_SIZE)

    def discard_hand(self):
        self.discard.extend(self.hand)
        del self.hand[:]

    def shuffle_deck(self):
        temp = self.deck
        self.deck = self.discard
        self.discard = temp

        shuffle(self.deck)
        print 'shuffling deck'

    def get_hand(self):
        return self.hand

    def remove_card(self, card):
        self.hand.remove(card)

    # PRIVATE
    def draw_card(self):
        card = self.deck.pop()
        self.hand.append(card)

    def draw_cards(self, n):

        if n > len(self.deck):
            n = len(self.deck)

        for i in range(n):
            self.draw_card()

        if not self.deck:
            self.shuffle_deck()
