from src.enum.object_codes import ARMY, TOWER
from src.data_structures.flood_fill import flood


class GuardMap(object):

    def __init__(self, strat_map):

        self.map = strat_map
        self.state = strat_map.state

        self.zones_to_update = set()

        self.guard_zones = None

        self.needs_update = True

    def initialize(self):
        self.initialize_guard_zones()

    def initialize_guard_zones(self):

        self.guard_zones = {}

        for player_id in self.state.player_manager.get_player_ids():
            self.guard_zones[player_id] = set()
            self.zones_to_update.add(player_id)

    def log_update(self, player_id):

        self.needs_update = True
        self.zones_to_update.add(player_id)

    def run(self):

        if self.needs_update:
            self.update()

    def update(self):

        for player_id in self.zones_to_update:
            self.update_guard_zones(player_id)

        self.zones_to_update.clear()
        self.needs_update = False

    def get_player_guards(self, player_id):

        player_objects = self.map.game_object_map.get_friendly_objects(player_id)
        possible_guard = {ARMY, TOWER}
        player_objects = filter(lambda x: x.obj_code in possible_guard, player_objects)

        return filter(lambda x: x.guarding, player_objects)

    def update_guard_zones(self, player_id):

        self.guard_zones[player_id].clear()

        active_guards = self.get_player_guards(player_id)

        if active_guards:

            for guard in active_guards:

                # get all tiles in guard range of guard
                tiles = self.get_guarded_tiles(guard)
                self.guard_zones[player_id].update(tiles)

        self.state.map_highlighter.update_defense_highlight()

    def get_guarded_tiles(self, guard):

        player_id = guard.owner_id

        def valid_func(point):
            return self.valid_guard_tile(player_id, point)

        touched = set()
        edge = [guard.coord.int_position]

        guard_range = 4
        if guard.obj_code == TOWER:
            guard_range = 2

        for i in range(guard_range):
            edge = flood(edge, valid_func, touched)
            touched.update(edge)

        return touched

    def valid_guard_tile(self, player_id, point):

        if not self.map.dominion_map.in_bounds(point):
            return False

        return self.map.dominion_map.get_tile(point) == player_id

    # API
    def point_is_guarded(self, point, safe_player_id):

        player_ids = filter(lambda x: x != safe_player_id, self.state.player_manager.get_player_ids())

        for player_id in player_ids:
            if point in self.guard_zones[player_id]:
                return True
        return False

    def get_nearest_guard(self, point):

        player_id = self.map.dominion_map.get_tile(point)

        active_guards = self.get_player_guards(player_id)
        if len(active_guards) == 1:
            guard = active_guards[0]
        else:
            guard = sorted(active_guards, key=lambda x: self.nearest(point, x.coord.int_position))[0]

        if guard.obj_code == TOWER:
            guard = guard.get_garrison()

        return guard

    def nearest(self, (ax, ay), (bx, by)):

        return abs(ax - bx) + abs(ay - by)

    def get_guarded_points(self):

        for zone in self.guard_zones.itervalues():
            for point in zone:
                yield point

    def refresh_guard_zones(self):
        for player_id in self.state.player_manager.get_player_ids():
            self.log_update(player_id)

    def sally_nearest_guard(self, point):

        guard = self.get_nearest_guard(point)
        if guard.is_garrison():
            if point != guard.point:
                guard.sally_forth()

        return guard
