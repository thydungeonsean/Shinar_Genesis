from src.enum.object_codes import *
from src.data_structures.flood_fill import flood
from src.enum.terrain import *


#########################################
# getting buildings
####################
def get_friendly_buildings_of_type(state, building_code):

    buildings = state.map.game_object_map.get_objects_with_code(building_code)
    buildings = filter_friendly_objects(state, buildings)

    return buildings


def get_friendly_palaces(state):

    palaces = get_friendly_buildings_of_type(state, PALACE)

    return filter(lambda x: not x.under_construction, palaces)


def filter_friendly_objects(state, objects):

    player_id = state.player_manager.active_player.player_id

    return filter(lambda x: x.owner_id == player_id, objects)


def get_coords_from_objects(objects):

    return [x.coord.int_position for x in objects]


def get_friendly_armies(state):
    armies = state.map.game_object_map.get_objects_with_code(ARMY)
    return filter_friendly_objects(state, armies)


def enemy_building_occupied(state, point):
    obj = state.map.game_object_map.get_at(point)
    if not obj:
        return False
    obj = obj[0]
    if obj.obj_code != ARMY:
        player_id = state.player_manager.active_player.player_id
        return obj.owner_id != player_id
    return False


def friendly_occupied(state, point):

    obj = state.map.game_object_map.get_at(point)
    if not obj:
        return False
    obj = obj[0]
    player_id = state.player_manager.active_player.player_id
    return obj.owner_id == player_id


def friendly_building_occupied(state, point):
    obj = state.map.game_object_map.get_at(point)
    if not obj:
        return False
    obj = obj[0]
    if obj.obj_code == ARMY:
        return False
    else:
        obj_id = obj.owner_id
        player_id = state.player_manager.active_player.player_id
        return obj_id == player_id


def enemy_occupied(state, point):

    obj = state.map.game_object_map.get_at(point)
    if not obj:
        return False
    obj = obj[0]
    player_id = state.player_manager.active_player.player_id
    return obj.owner_id != player_id


def enemy_palace(state, point):

    player_id = state.player_manager.active_player.player_id
    palaces = state.map.game_object_map.get_objects_with_code(PALACE)
    palaces = filter(lambda x: x.owner_id != player_id, palaces)
    coords = get_coords_from_objects(palaces)
    return point in coords


##############################################
# valid placement functions
###############################
def in_bounds(state, point):
    return state.map.tile_map.in_bounds(point)


def in_player_domain(state, point):
    dominion_map = state.map.dominion_map
    return dominion_map.point_is_in_player_dominion(point, state.player_manager.active_player)


def has_terrain(state, point, valid_terrain):
    terrain = state.map.tile_map.get_tile(point)
    return terrain in valid_terrain


def unoccupied(state, point):
    return point not in state.map.game_object_map.occupied()


def has_farm(state, point):
    return state.map.farm_map.is_farm(point)


#############################################3
# HARVEST
#############
def get_connected_farms(state, point, exclude_connectors=True):

    edge = [point]
    touched = set(edge)

    while edge:
        edge = flood(edge, get_valid_connected_farm_func(state), touched)
        touched.update(edge)

    if exclude_connectors:
        # remove any village or granary points
        connections = filter(lambda x: point_is_farm_connecting(state, x), touched)
        touched = touched.difference(connections)

    return touched


def get_valid_connected_farm_func(state):

    def valid_connected_farm(point):
        # point in active player domain
        if not in_bounds(state, point) or not in_player_domain(state, point):
            return False
        # point is farm or point is village or granary
        return has_farm(state, point) or point_is_farm_connecting(state, point)

    return valid_connected_farm


def point_is_farm_connecting(state, point):

    granaries = state.map.game_object_map.get_objects_with_code(GRANARY)
    villages = state.map.game_object_map.get_objects_with_code(VILLAGE)

    points = get_coords_from_objects(granaries)
    points.extend(get_coords_from_objects(villages))

    return point in points


def get_edge(group):

    return filter(lambda x: not_surrounded(x, group), group)


def not_surrounded(point, group):

    adj = get_adj(point)
    return len(adj.intersection(group)) != 4


def get_adj((x, y)):

    return {(x-1, y), (x+1, y), (x, y-1), (x, y+1)}


##############################################
# PLANT
#############
def plant_edge(state, edge, touched):

    return flood(edge, get_valid_planting_func(state), touched)


def get_valid_planting_func(state):

    farm_map = state.map.farm_map

    def valid_for_planting(point):
        # point in active player domain
        if not in_bounds(state, point) or not in_player_domain(state, point):
            return False
        # point is not farm
        if farm_map.is_farm(point):
            return False
        # point is farmable
        if not has_terrain(state, point, {PLAINS, FERTILE}):
            return False

        return unoccupied(state, point)

    return valid_for_planting


##############################################
# RULE
###########
def get_rule_edge(state, edge, touched):

    return flood(edge, get_valid_rule_func(state), touched)


def get_valid_rule_func(state):

    def valid_for_rule(point):

        if not in_bounds(state, point):
            return False
        return unoccupied(state, point)

    return valid_for_rule


####################################################
# MILITARY
####################3
def get_army_placement_points(state):

    palaces = get_coords_from_objects(get_friendly_buildings_of_type(state, PALACE))
    towers = get_coords_from_objects(get_friendly_buildings_of_type(state, TOWER))

    spawners = palaces
    spawners.extend(towers)

    spawn_points = flood(spawners, get_valid_spawn_func(state), set(spawners))
    return spawn_points


def get_valid_spawn_func(state):

    def valid_spawn(point):
        if not in_bounds(state, point) or not in_player_domain(state, point):
            return False
        if has_terrain(state, point, {RIVER}):
            return False
        return unoccupied(state, point)

    return valid_spawn


def get_army_movement_options(state, army, conquer=False):

    touched = set()
    edge = [army.coord.int_position]

    for i in range(army.speed):
        edge = flood(edge, get_valid_movement_func(state, conquer), touched)
        touched.update(edge)

    touched = filter(lambda x: not has_terrain(state, x, {RIVER}), touched)

    return list(touched)


def get_valid_movement_func(state, conquer):

    def valid_movement(point):
        if not in_bounds(state, point):
            return False
        if enemy_building_occupied(state, point):
            return conquer

        return not friendly_occupied(state, point)

    return valid_movement


#########################################
# Military effects

def get_raided_points(state, point):

    def valid(p):
        return in_bounds(state, p)

    edge = [point]
    touched = set()

    for i in range(5):
        edge = flood(edge, valid, touched)
        touched.update(edge)

    raided = filter(lambda x: has_farm(state, x) and not in_player_domain(state, x), touched)
    return raided


def get_conquered_points(state, point):

    def valid(p):
        if not in_bounds(state, p):
            return False
        return not enemy_palace(state, p)

    edge = [point]
    touched = set()

    for i in range(4):
        edge = flood(edge, valid, touched)
        touched.update(edge)

    branch_points = adj_to_player_domain(state, touched)
    if not branch_points:
        return []
    if len(branch_points) == len(touched):
        return branch_points

    else:

        def valid_in_range(p):
            return p in touched

        edge = branch_points
        conquered = set()
        while edge:
            edge = flood(edge, valid_in_range, conquered)
            conquered.update(edge)

        return conquered


def adj_to_player_domain(state, touched):

    return filter(lambda x: in_player_domain(state, x) or adj_in_player_domain(state, x)
                  , touched)


def adj_in_player_domain(state, (x, y)):

    adj = get_adj((x, y))
    for a in adj:
        if in_bounds(state, a) and in_player_domain(state, a):
            return True
    return False


############################################################################
# BUILD ACTION
##################
def get_valid_build_points(state, building_id):

    dominion_map = state.map.dominion_map
    domain = dominion_map.get_all(state.player_manager.active_player.player_id)

    building_points = filter(lambda x: not_adj_to_building(state, x) and not has_terrain(state, x, {RIVER}), domain)

    if building_id == PALACE:
        building_points = palace_buffer(state, building_points)
    elif building_id == GRANARY:
        building_points = filter(lambda x: has_terrain(state, x, {FERTILE, PLAINS}), building_points)

    return building_points


def not_adj_to_building(state, (x, y)):

    adj = [(x, y), (x+1, y), (x-1, y), (x, y+1), (x, y-1),
           (x+1, y+1), (x-1, y+1), (x+1, y-1), (x-1, y-1)]

    for point in adj:
        if not in_bounds(state, point):
            pass
        if friendly_building_occupied(state, point):
            return False
    return True


def palace_buffer(state, points):

    palaces = state.map.game_object_map.get_objects_with_code(PALACE)
    player_id = state.player_manager.active_player.player_id

    palaces = filter(lambda x: x.owner_id == player_id, palaces)

    # TODO palace buffer value here
    points = filter(lambda x: min_dist_from_palaces(palaces, 5, x), points)

    return points


def get_dist((ax, ay), (bx, by)):

    return abs(ax-bx) + abs(ay-by)


def min_dist_from_palaces(palaces, min_dist, point):

    for p in palaces:
        p_coord = p.coord.int_position
        if get_dist(p_coord, point) <= min_dist:
            return False

    return True
