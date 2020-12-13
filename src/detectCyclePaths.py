
class CyclicGraph:
    def __init__(self, edges=None):
        if edges is None:
            edges = []
        self.graph = edges
        self.cycles = []

    def find_all_cycles(self):
        # global graph
        # global cycles
        for edge in self.graph:
            for node in edge:
                self.find_new_cycles([node])
        for cy in self.cycles:
            path = [str(node) for node in cy]
            s = ",".join(path)
            print(s)

    def find_new_cycles(self, path):
        start_node = path[0]
        # next_node = None
        # sub = []

        # visit each edge and each node of each edge
        for edge in self.graph:
            node1, node2 = edge
            if start_node in edge:
                if node1 == start_node:
                    next_node = node2
                else:
                    next_node = node1
                if not self.visited(next_node, path):
                    # neighbor node not on path yet
                    sub = [next_node]
                    sub.extend(path)
                    # explore extended path
                    self.find_new_cycles(sub);
                elif len(path) > 2 and next_node == path[-1]:
                    # cycle found
                    p = self.rotate_to_smallest(path);
                    inv = self.invert(p)
                    if self.is_new(p) and self.is_new(inv):
                        self.cycles.append(p)

    #  rotate cycle path such that it begins with the smallest node
    def invert(self, path):
        return self.rotate_to_smallest(path[::-1])

    def rotate_to_smallest(self, path):
        n = path.index(min(path))
        return path[n:] + path[:n]

    def visited(self, node, path):
        return node in path

    def is_new(self, path):
        return path not in self.cycles


if __name__ == '__main__':
    # graph = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4], [2, 6], [4, 6], [8, 7], [8, 9], [9, 7]]
    graph = {(1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (2, 6), (4, 6), (8, 7), (8, 9), (9, 7)}
    graph_obj = CyclicGraph(graph)
    graph_obj.find_all_cycles()