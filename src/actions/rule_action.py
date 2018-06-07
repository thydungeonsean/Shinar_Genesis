from action import Action
from src.enum.actions import RULE_ACTION
from map_tools import *
from random import randint


class RuleAction(Action):

    def __init__(self, state, player):

        Action.__init__(self, state, player, RULE_ACTION)

    def compute_valid_points(self):

        palaces = get_friendly_palaces(self.state)
        points = get_coords_from_objects(palaces)
        self.valid_points = set(points)

    def perform_action(self, point):

        if point in self.valid_points:

            for i in range(2):
                palace_domain = self.get_palace_domain(point)
                edge = get_edge(palace_domain)
                new_edge = get_rule_edge(self.state, edge, palace_domain)
                new_domain = self.get_new_domain_points(new_edge)
                map(lambda x: self.extend_rule(x), new_domain)

            self.state.map.map_image.render_map()
            # end action
            self.complete_action()

    def get_palace_domain(self, palace):

        edge = [palace]
        touched = set()

        while edge:
            edge = flood(edge, self.valid_domain, touched)
            touched.update(edge)

        return touched

    def valid_domain(self, point):

        dom = self.state.map.dominion_map

        if not dom.in_bounds(point):
            return False

        return dom.get_tile(point) == self.player.player_id

    def extend_rule(self, point):
        self.state.map.dominion_map.add_dominion(self.player.player_id, point)

    def get_new_domain_points(self, edge):

        new_domain = []
        base_chance = 50

        for point in edge:

            chance = base_chance

            if self.state.map.dominion_map.get_tile(point) is not None:

                # TODO if guarded, can't expand here

                chance -= 25

            terrain = self.state.map.tile_map.get_tile(point)
            if terrain == DESERT:
                chance -= 20
            elif terrain == PLAINS:
                chance += 10
            elif terrain == FERTILE:
                chance += 20
            elif terrain == RIVER:
                chance += 5

            if randint(1, 100) <= chance:
                new_domain.append(point)

        return new_domain
