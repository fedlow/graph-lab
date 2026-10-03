class AdjacencyMatrixGraph:
    def __init__(self):
        self.vertices = []
        self.index = {}
        self.matrix = []

    def add_vertex(self, v):
        if v in self.index:
            return
        self.index[v] = len(self.vertices)
        self.vertices.append(v)
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * len(self.vertices))

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        i, j = self.index[u], self.index[v]
        self.matrix[i][j] = 1

    def __repr__(self):
        header = "     " + " ".join(f"{v:>3}" for v in self.vertices)
        rows = [header]
        for i, v in enumerate(self.vertices):
            row = " ".join(f"{x:>3}" for x in self.matrix[i])
            rows.append(f"{v:>3}  {row}")
        return "\n".join(rows)


def build_matrix_from_edges(edges):
    g = AdjacencyMatrixGraph()
    for u, v in edges:
        g.add_edge(u, v)
    return g