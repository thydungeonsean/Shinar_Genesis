from base_map import BaseMap
from src.image.border_edge_tile_map import BorderEdgeTileMap
from src.enum.object_codes import PALACE
from src.data_structures.flood_fill import flood


class DominionMap(BaseMap):

    def __init__(self, w, h, state):

        self.state = state
        BaseMap.__init__(self, w, h)
        self.tiles = {}
        self.needs_update = True
        self.edges = {}
        self.edge_tile_map = BorderEdgeTileMap(self)

    def initialize(self):
        self.update_edges()

    def run(self):

        if self.needs_update:

            self.sanitize_dominion()

            self.update_edges()
            self.state.map.map_image.render_map()
            # if dominion is updated in anyway, we need to refresh all defense zones
            self.state.map.guard_map.refresh_guard_zones()

    def base_value(self, x, y):
        return None

    def add_dominion(self, owner_id, point):
        self.set_tile(point, owner_id)
        self.needs_update = True

    def point_is_in_player_dominion(self, point, player):

        player_id = player.player_id
        return self.get_tile(point) == player_id

    def get_color(self, point):
        player = self.state.player_manager.get_player(self.get_tile(point))
        return player.color

    def update_edges(self):

        self.edges.clear()

        for player_id in self.state.player_manager.get_player_ids():

            players_dominion = self.get_all(player_id)
            dominion_set = set(players_dominion)
            edges = self.find_edge(players_dominion)
            for e in edges:
                self.edges[e] = self.get_edge_code(e, dominion_set)

        self.needs_update = False

    def find_edge(self, area):
        area_set = set(area)
        return filter(lambda x: self.not_surrounded(x, area_set), area)

    def not_surrounded(self, point, area):
        adj = self.get_adj(point)
        overlap = len(adj.intersection(area))
        off_map = len(filter(lambda x: not self.in_bounds(x), adj))

        return overlap + off_map != 4

    def get_adj(self, (x, y)):

        return {(x-1, y), (x+1, y), (x, y-1), (x, y+1)}

    def get_edge_code(self, (x, y), player_dominion):

        adj = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
        open_edges = [self.is_border(p, player_dominion) for p in adj]
        code = []
        for corner in range(4):

            a = open_edges[corner-1]
            b = open_edges[corner]

            if a and b:
                code.append('c')
            elif a:
                code.append('a')
            elif b:
                code.append('b')
            else:
                code.append('-')

        return ''.join(code)

    def is_border(self, point, player_dominion):

        if not self.in_bounds(point):
            return False
        return point not in player_dominion

    def sanitize_dominion(self):

        for player_id in self.state.player_manager.get_player_ids():

            self.sanitize_player_domain(player_id)

    def sanitize_player_domain(self, player_id):

        # get all palaces coords
        palaces = self.state.map.game_object_map.get_objects_with_code(PALACE)
        palaces = filter(lambda x: x.owner_id == player_id, palaces)
        palace_coords = [p.coord.int_position for p in palaces]

        # flood players domain from those coords

        edge = palace_coords
        touched = set(palace_coords)
        while edge:
            edge = flood(edge, lambda x: self.valid_domain(player_id, x), touched)
            touched.update(edge)
        palace_domain = touched

        # get all their domain
        total_domain = set(self.state.map.dominion_map.get_all(player_id))

        stranded = total_domain.difference(palace_domain)
        if stranded:
            map(self.strand, stranded)

    def valid_domain(self, player_id, point):

        domain = self.state.map.dominion_map
        if not domain.in_bounds(point):
            return False
        return domain.get_tile(point) == player_id

    def strand(self, point):
        self.set_tile(point, None)
