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
                player_domain = self.get_player_domain()
                edge = get_edge(player_domain)
                new_edge = get_rule_edge(self.state, edge, player_domain)
                new_domain = self.get_new_domain_points(new_edge)
                map(lambda x: self.extend_rule(x), new_domain)

                # end action
            self.state.map.map_image.render_map()

    def get_player_domain(self):

        return set(self.state.map.dominion_map.get_all(self.player.player_id))

    def extend_rule(self, point):
        self.state.map.dominion_map.add_dominion(self.player.player_id, point)

    def get_new_domain_points(self, edge):

        new_domain = []
        base_chance = 50

        for point in edge:

            chance = base_chance

            if self.state.map.dominion_map.get_tile(point) is not None:
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
