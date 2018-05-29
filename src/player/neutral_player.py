from src.colors import WHITE


class NeutralPlayer(object):

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    def __init__(self):

        self.name = 'Neutral'
        self.player_id = 0
        self.color = WHITE
