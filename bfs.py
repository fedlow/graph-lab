from collections import deque


def bfs(graph, start):
    visited = set()
    order = []
    q = deque([start])
    visited.add(start)

    while q:
        v = q.popleft()
        order.append(v)
        for nxt in graph.neighbors(v):
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)

    return order