

def flood(edge, valid_func, touched_set):

    new_edge = set()

    for point in edge:
        add_neighbours(point, new_edge, valid_func, touched_set)

    return list(new_edge)


def add_neighbours(point, edge, valid_func, touched_set):
    for adj_point in get_adj(point, valid_func, touched_set):
        edge.add(adj_point)


def get_adj((x, y), valid_func, touched_set):
    adj = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    return filter(lambda x: point_is_valid(x, valid_func, touched_set), adj)


def point_is_valid(point, valid_func, touched_set):

    if point in touched_set:
        return False
    return valid_func(point)
