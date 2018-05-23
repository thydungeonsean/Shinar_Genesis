from src.data_structures.flood_fill import flood
from random import randint
from src.enum.terrain import *


def get_closest(point, palace_list):

    ranking = []

    for palace in palace_list:

        palace_coord = palace.coord.int_position
        dist = get_distance(point, palace_coord)
        ranking.append((dist, palace))

    ranking.sort(key=lambda x: x[0])

    if ranking[0][0] == ranking[1][0]:
        return None  # equidistant
    else:
        return ranking[0][1]


def get_distance((ax, ay), (bx, by)):

    return abs(ax - bx) + abs(ay - by)


def get_starting_zone(state, palace, zone_size):

    edge = [palace.coord.int_position]
    zone = []
    touched = set()

    tries = 0

    while len(zone) < zone_size:

        zone.extend(edge)
        touched.update(edge)

        edge = flood(edge, get_expansion_func(state, palace), touched)

        tries += 1
        if tries > 100:
            break

    return zone


def get_expansion_func(state, palace):

    terrain_map = state.map.tile_map

    def valid_func((x, y)):

        if not terrain_map.in_bounds((x, y)):
            return False

        dist = get_distance(palace.coord.int_position, (x, y))
        if dist < 4:
            return True

        chance = 60

        terrain = terrain_map.get_tile((x, y))
        if terrain == DESERT:
            chance -= 20
        elif terrain == PLAINS:
            chance += 10
        elif terrain == FERTILE:
            chance += 20
        elif terrain == RIVER:
            chance += 5

        return randint(1, 100) <= chance

    return valid_func
