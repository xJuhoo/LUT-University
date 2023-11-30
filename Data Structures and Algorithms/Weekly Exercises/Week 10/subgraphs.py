# Week 10: Exercise 1
# Juho Rekonen

from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def add(self, u, v):
        # Check that u and v are within the valid range
        if 0 <= u < self.n and 0 <= v < self.n:
            # Check that the edge does not already exist
            if v not in self.graph[u] and u not in self.graph[v]:
                self.graph[u].append(v)
                self.graph[v].append(u)

    def remove(self, u, v):
        # Only remove edges that actually exists
        if v in self.graph[u] and u in self.graph[v]:
            self.graph[u].remove(v)
            self.graph[v].remove(u)

    # Using depth-first search to traverse the graph
    # and count the number of sub-graphs
    def dfs(self, node, visited):
        visited.add(node)
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)

    def subgraphs(self):
        visited = set()
        subgraph_count = 0

        for node in range(self.n):
            if node not in visited:
                subgraph_count += 1
                self.dfs(node, visited)

        return subgraph_count


if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 4), (2, 1),
             (2, 5), (3, 0),
             (5, 1))
    for u, v in edges:
        graph.add(u, v)

    print(graph.subgraphs())  # Output: 2

    more_connections = ((0, 2), (2, 3),
                        (3, 5), (4, 5))
    for u, v in more_connections:
        graph.add(u, v)

    print(graph.subgraphs())  # Output: 1
