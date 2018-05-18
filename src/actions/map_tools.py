from src.enum.object_codes import *


def point_has_building(state, point, building_code):

    buildings = state.map.game_object_map.get_objects_with_code(building_code)

    points = [x.coord.int_position for x in buildings]
    return point in points


def point_has_granary(state, point):

    return point_has_building(state, point, GRANARY)
