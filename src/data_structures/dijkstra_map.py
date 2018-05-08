

class DijkstraMap(object):

    def __init__(self, parent_map):

        self.parent_map = parent_map

    def spread(self, match_value):

        edge = set()

        for point in self.parent_map.get_all(match_value):

            self.add_neighbours(point, edge, match_value)

        return edge

    def add_neighbours(self, point, edge, match_value):

        for adj_point in self.get_adj(point, match_value):
            edge.add(adj_point)

    def get_adj(self, (x, y), match_value):

        adj = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

        return filter(lambda x: self.point_is_valid(x, match_value), adj)

    def point_is_valid(self, point, match_value):

        if not self.parent_map.in_bounds(point):
            return False
        if self.parent_map.get_tile(point) == match_value:
            return False
        return self.parent_map.get_tile(point) < match_value

