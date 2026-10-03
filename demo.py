from directed_graph import DirectedGraph
from bfs import bfs
from adjacency_matrix import build_matrix_from_edges
from adjacency_list import build_list_from_edges


print("=== 1. DirectedGraph ===")
g = DirectedGraph()
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
for u, v in edges:
    g.add_edge(u, v)
print(g)

print("=== 2. BFS от A ===")
print(f"Порядок обхода: {bfs(g, 'A')}")

print("=== 3. Матрица смежности ===")
m = build_matrix_from_edges(edges)
print(m)
m.add_edge("E", "A")
print("\nПосле add_edge('E', 'A'):")
print(m)

print("=== 4. Список смежности ===")
adj = build_list_from_edges(edges)
print(adj)
adj.add_edge("E", "A")
print("\nПосле add_edge('E', 'A'):")
print(adj)