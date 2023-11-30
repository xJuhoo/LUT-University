# Week 10: Exercise 2
# Juho Rekonen

# We are using the Floyd-Warshall algorithm to find all shortest paths
# between vertices with non-existent paths valued at -1

class Graph:
    def __init__(self, n):
        self.n = n # Number of vertices
        self.graph = [[float("inf")] * n for _ in range(n)] # Creating the matrix
        # Initialize the diagonal to have values 0
        for i in range(n):
            self.graph[i][i] = 0

    def add(self, u, v, w):
        if 0 <= u < self.n and 0 <= v < self.n:
            self.graph[u][v] = w
    
    def remove(self, u, v):
        # Only remove edges that actually exists
        if self.graph[u][v]:
            self.graph[u][v] = float('inf')
    
    # The function to return the n * n matrix
    def all_paths(self):
        distance = [row[:] for row in self.graph]

        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])
        
        # Search for non-existent paths
        for i in range(self.n):
            for j in range(self.n):
                if distance[i][j] == float('inf'):
                    distance[i][j] = -1

        return distance

if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
             (2, 3, 1), (2, 5, 2), (3, 0, 6),
             (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in edges:
        graph.add(u, v, w)

    M = graph.all_paths()
    for weights in M:
        for weight in weights:
            print(f"{weight:3d}", end="")
        print()
    # Output:
    #   0 12  7  8  9  9
    #  -1  0 -1 -1 -1 -1
    #   7  5  0  1 16  2
    #   6  8 13  0 15  2
    #  -1  7 -1 -1  0  1
    #  -1  6 -1 -1 -1  0
