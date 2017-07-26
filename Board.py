import BoardUtil


class Board:

    def __init__(self):
        self.directions = ["northwest", "north", "northeast", "southeast", "south", "southwest"]
        self.lands_nodes = BoardUtil.fill_lands_nodes()
        self.edges = self.fill_edges()

    def get_lands_by_node(self, node):
        return [i for i, l in enumerate(self.lands_nodes) if node in l]

    def get_node_directions(self, node):
        node_directions = dict()
        for i, l in enumerate(self.lands_nodes):
            if node in l:
                index = l.index(node)
                node_directions[i] = self.directions[index]

        return node_directions

    def fill_edges(self):
        edges = list()
        for nodes in self.lands_nodes:
            for i in range(6):
                if not ({nodes[i], nodes[(i + 1) % 6]} in edges):
                    edges.append({nodes[i], nodes[(i + 1) % 6]})

        return edges
