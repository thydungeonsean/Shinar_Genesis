

class PlayerController(object):

    def __init__(self, player):
        self.player = player
        self.active = False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def run(self):
        pass
