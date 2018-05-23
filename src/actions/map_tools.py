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


def filter_friendly_objects(state, objects):

    player_id = state.player_manager.active_player.player_id

    return filter(lambda x: x.owner_id == player_id, objects)


def get_coords_from_objects(objects):

    return [x.coord.int_position for x in objects]


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

    dominion = state.map.dominion_map
    farm_map = state.map.farm_map

    def valid_connected_farm(point):
        # point in active player domain
        if not dominion.in_bounds(point) or \
                not dominion.point_is_in_player_dominion(point, state.player_manager.active_player):
            return False
        # point is farm or point is village or granary
        return farm_map.is_farm(point) or point_is_farm_connecting(state, point)

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

    dominion = state.map.dominion_map
    farm_map = state.map.farm_map
    terrain = state.map.tile_map
    obj_map = state.map.game_object_map

    def valid_for_planting(point):
        # point in active player domain
        if not dominion.in_bounds(point) or \
                not dominion.point_is_in_player_dominion(point, state.player_manager.active_player):
            return False
        # point is not farm
        if farm_map.is_farm(point):
            return False
        # point is farmable
        if terrain.get_tile(point) not in {PLAINS, FERTILE}:
            return False

        return point not in obj_map.occupied()

    return valid_for_planting


##############################################
# RULE
###########
def get_rule_edge(state, edge, touched):

    return flood(edge, get_valid_rule_func(state), touched)


def get_valid_rule_func(state):

    terrain = state.map.tile_map
    obj_map = state.map.game_object_map

    def valid_for_rule(point):

        if not terrain.in_bounds(point):
            return False
        return point not in obj_map.occupied()

    return valid_for_rule
