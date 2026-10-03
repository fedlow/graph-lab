class AdjacencyListGraph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self.adj[u]:
            self.adj[u].append(v)

    def __repr__(self):
        lines = [f"{v}: {self.adj[v]}" for v in sorted(self.adj)]
        return "AdjacencyListGraph(\n  " + "\n  ".join(lines) + "\n)"


def build_list_from_edges(edges):
    g = AdjacencyListGraph()
    for u, v in edges:
        g.add_edge(u, v)
    return g