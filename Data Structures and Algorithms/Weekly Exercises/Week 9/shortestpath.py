# Week 9: Exercise 2
# Juho Rekonen

from collections import defaultdict

# We are going to use Dijkstra's algorithm to find the shortest path
class Graph:
    def __init__(self, n):
        self.vertices = n
        self.graph = defaultdict(list)

    def add(self, u, v, w):
        # Check that u and v are within the valid range
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            # Check that the edge does not already exist
            if v not in self.graph[u]:
                self.graph[u].append((v, w))

    def remove(self, u, v):
        # Removing an edge is done by constructing a new list for vertex u 
        # by excluding all edges where the destination vertex (x) is v
        self.graph[u] = [(x, w) for x, w in self.graph[u] if x != v]

    # Function to find the shortest path
    def shortest_path(self, start, end):
        # Initialize the array of distances with infinity for all vertices
        # So {key: value} pairs are {vertex: distance}
        distances = {vertex: float('infinity') for vertex in range(self.vertices)}
        distances[start] = 0

        # Initialize the parent array to track the shortest path
        parent = {vertex: None for vertex in range(self.vertices)}

        # Priority queue to store vertices and their distances
        priority_queue = [(0, start)]

        while priority_queue:

            distance, vertex = min(priority_queue)
            priority_queue.remove((distance, vertex))

            for neighbour, weight in self.graph[vertex]:
                distance = distances[vertex] + weight

                # If the new distance is smaller than the current stored distance
                # we update the distance and the parent
                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    parent[neighbour] = vertex
                    priority_queue.append((distance, neighbour))

        # Reconstruct the shortest path
        path = []
        current = end
        while current is not None:
            path.insert(0, current)
            current = parent[current]
        
        if distances[end] == float('infinity'):
            print("-1")
        else:
            print(" ".join(map(str, path)))


if __name__ == "__main__":
    graph = Graph(10)
    edges = ((0, 1, 25), (0, 2, 6), (1, 3, 10),
             (1, 4, 3), (2, 3, 7), (2, 5, 25),
             (3, 4, 12), (3, 5, 15), (3, 6, 4),
             (3, 7, 15), (3, 8, 20), (4, 7, 2),
             (5, 8, 2), (6, 7, 8), (6, 8, 13),
             (6, 9, 15), (7, 9, 5), (8, 9, 1))
    for u, v, w in edges:
        graph.add(u, v, w)

    graph.shortest_path(0, 9)   # Output: 0 2 3 6 7 9
    graph.remove(3, 6)
    graph.remove(5, 6)
    graph.shortest_path(0, 9)   # Output: 0 2 3 5 8 9
