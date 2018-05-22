

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
