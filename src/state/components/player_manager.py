

class PlayerManager(object):

    def __init__(self, state, *players):

        self.state = state
        self.players = list(players)

    def get_player(self, owner_id):

        return filter(lambda x: x.player_id == owner_id, self.players)[0]

    def get_player_ids(self):

        return [x.player_id for x in self.players]

    @property
    def active_player(self):
        return self.players[0]
