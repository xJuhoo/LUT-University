# Week 9: Exercise 1
# Juho Rekonen

from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n # Number of vertices
        self.adj_list = [[] for i in range(n)] # Creating the adjacency lists

    def add(self, u, v):
        # Check that u and v are within the valid range
        if 0 <= u < self.n and 0 <= v < self.n:
            # Check that the edge does not already exist
            if v not in self.adj_list[u] and u not in self.adj_list[v]:
                self.adj_list[u].append(v)
                self.adj_list[v].append(u)

    def remove(self, u, v):
        # Only remove edges that actually exists
        if v in self.adj_list[u] and u in self.adj_list[v]:
            self.adj_list[u].remove(v)
            self.adj_list[v].remove(u)
    
    # Depth-first search
    def dft(self, start):
        visited = set()
        self._dft_recursive(start, visited)
        print()

    def _dft_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')

        for neighbour in sorted(self.adj_list[vertex]):
            if neighbour not in visited:
                self._dft_recursive(neighbour, visited)

    # Breadth-first search
    def bft(self, start):
        visited = [False] * self.n
        queue = deque([start])
        visited[start] = True

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in sorted(self.adj_list[vertex]):
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print()

if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2), (0, 4), (2, 1),
             (2, 3), (2, 5), (3, 0),
             (3, 5), (4, 5), (5, 1))
    for u, v in edges:
        graph.add(u, v)
        
    graph.dft(0)  # Output: 0 2 1 5 3 4 
    graph.bft(0)  # Output: 0 2 3 4 1 5 

    graph.remove(0, 2)
    graph.remove(2, 5)
    graph.remove(1, 4)

    graph.dft(0)  # Output: 0 3 2 1 5 4 
    graph.bft(0)  # Output: 0 3 4 2 5 1