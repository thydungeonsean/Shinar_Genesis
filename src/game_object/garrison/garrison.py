from src.enum.object_codes import GARRISON


class Garrison(object):

    def __init__(self, building, player):

        self.obj_id = GARRISON
        self.building = building
        self.state = building.state
        self.player = player

    def rout(self):
        print 'garrison routed'

    def is_garrison(self):
        return True
