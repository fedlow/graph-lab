class DirectedGraph:
    def __init__(self):
        self.vertices = set()
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices.add(v)
            self.adj[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self.adj[u]:
            self.adj[u].append(v)

    def neighbors(self, v):
        return self.adj.get(v, [])

    def __repr__(self):
        lines = [f"{v}: {self.adj[v]}" for v in sorted(self.adj)]
        return "DirectedGraph(\n  " + "\n  ".join(lines) + "\n)"