from ai_controller import AIController
from human_controller import HumanController


class Player(object):

    AI = 0
    HUMAN = 1

    def __init__(self, player_id, color, ai=False):

        self.player_id = player_id
        self.color = color
        if ai:
            self.controller_id = Player.AI
        else:
            self.controller_id = Player.HUMAN

        self.controller = self.load_controller()

    def load_controller(self):
        if self.controller_id == Player.AI:
            return AIController(self)
        else:
            return HumanController(self)

    def activate_controller(self):
        print str(self.player_id) + ' activated'
        self.controller.activate()
