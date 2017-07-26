import BoardUtil


class Board:

    def __init__(self):
        self.lands_nodes = BoardUtil.fill_lands_nodes()

    def get_lands_by_node(self, node):
        return [i for i, l in enumerate(self.lands_nodes) if node in l]
