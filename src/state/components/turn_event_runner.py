from random import sample, choice
from src.data_structures.flood_fill import flood
from src.enum.object_codes import VILLAGE
from src.enum.terrain import FERTILE, PLAINS


class TurnEventRunner(object):

    FARMABLE = {PLAINS, FERTILE}

    def __init__(self, state):

        self.state = state
        self.map = state.map

    def run(self):

        # active player passively expands domain
        self.passive_domain_spread()

        # all villages plant and harvest passively
        self.run_villages()

        # advance flood timer
        self.state.flood_timer.advance()

        # if time for flood, run flood
        if self.state.flood_timer.flood_happens():
            self.state.flood_timer.reset()
            # do the flood
        else:
            # dry the lands
            pass

    def passive_domain_spread(self):

        active_player = self.state.player_manager.active_player

        # get edges players domain
        dominion = self.map.dominion_map
        domain = set(dominion.get_all(active_player.player_id))

        # get edges of their domain
        border = dominion.find_edge(domain)

        # flood one step out from edges
        possible = flood(border, self.get_valid_expansion_func(), domain)

        min_spread = 5  # TODO have this affected by factors
        k = min((len(possible), min_spread))
        if not k:
            return

        # choose random sample of egde and expand domain
        tiles = sample(possible, k)
        map(lambda x: self.expand(active_player.player_id, x), tiles)

    def get_valid_expansion_func(self):

        def valid(point):

            # in bounds and not claimed
            domain = self.map.dominion_map
            if not domain.in_bounds(point):
                return False
            if point in self.map.game_object_map.occupied():
                return False

            return domain.get_tile(point) is None

        return valid

    def expand(self, player_id, point):

        self.map.dominion_map.add_dominion(player_id, point)

    def run_villages(self):

        game_objects = self.map.game_object_map
        villages = game_objects.get_objects_with_code(VILLAGE)

        for village in villages:

            self.run_village(village)

    def run_village(self, village):

        # get surrounding farmable tiles
        # check if all are farms
        # if all farms, harvest all and 1) add resources to neutral village OR
        #                               2) add resources to controlling player
        # else
        # grab all fertile tiles
        # if any, add farm to all of them
        # else grab a random plains tile and farm it

        village_farmland = self.get_village_farmland(village)
        if self.harvest_ready(village_farmland):
            self.village_harvest(village, village_farmland)
        else:
            self.village_plant(village_farmland)

    def get_village_farmland(self, village):

        x, y = village.coord.int_position
        adj = [(x+1, y), (x-1, y), (x+1, y+1), (x-1, y-1),
               (x, y+1), (x, y-1), (x+1, y-1), (x-1, y+1)]

        return filter(lambda x: self.farmable_by_village(village, x), adj)

    def farmable_by_village(self, village, point):

        tile_map = self.map.tile_map
        if not tile_map.in_bounds(point):
            return False

        if tile_map.get_tile(point) not in TurnEventRunner.FARMABLE:
            return False

        if village.is_neutral():
            village_domain = None
        else:
            village_domain = village.owner_id

        # TODO make sure no building or army there either
        return self.map.dominion_map.get_tile(point) == village_domain

    def harvest_ready(self, farmland):

        farm_map = self.map.farm_map
        for point in farmland:
            if not farm_map.is_farm(point):
                return False
        return True

    def village_harvest(self, village, farmland):

        for farm in farmland:
            self.map.farm_map.remove_farm(farm)
            # TODO have resources be applied to appropriate recipients

    def village_plant(self, farmland):

        unplanted = filter(lambda x: not self.map.farm_map.is_farm(x), farmland)
        fertile = filter(lambda x: self.map.tile_map.get_tile(x) == FERTILE, unplanted)
        if fertile:
            map(self.map.farm_map.add_farm, fertile)
        else:
            assert(len(unplanted) > 0)
            new_field = choice(unplanted)
            self.map.farm_map.add_farm(new_field)
