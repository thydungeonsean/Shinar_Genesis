from src.enum.object_codes import GARRISON


class Garrison(object):

    def __init__(self, building, player):

        self.obj_id = GARRISON
        self.building = building
        self.state = building.state
        self.player = player

        self.sallying = False

    @property
    def point(self):
        return self.building.coord.int_position

    def rout(self):
        self.building.end_defend()
        self.sallying = False
        print 'garrison routed'

    def is_garrison(self):
        return True

    def sally_forth(self):
        self.sallying = True
