# Week 10: Exercise 3
# Juho Rekonen

# To find the minimal cost spanning tree we are going to
# use Kruskal's algorithm
class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [] # Storing the edges so we can rearrange them later
    
    def add(self, u, v, w):
        # Check that u and v are within the valid range
        if 0 <= u < self.n and 0 <= v < self.n:
            # Check if the undirected edge already exists. If it does,
            # update the weight
            for i, (x, y, _) in enumerate(self.edges):
                if (x, y) == (u, v) or (x, y) == (v, u):
                    self.edges[i] = (u, v, w)
                    return
            # If the edge doesn't exist, we add it
            self.edges.append((u, v, w))
    
    def print(self):
        for edge in self.edges:
            print(edge)
    
    def remove(self, u, v):
        # Removing an edge is done by constructing a new list for edges 
        # by excluding all edges where the destination vertex is v or u
        # This way by for example removing an edge (0, 1), also the edge
        # (1, 0) is removed
        self.edges = [(x, y, w) for x, y, w in self.edges if (x, y) != (u, v) and (y, x) != (u, v)]
    
    # Kruskal's algorithm for minimum spanning tree
    def min_expense(self):
        # Sort edges by weight
        self.edges.sort(key=lambda x: x[2])
        parent = [i for i in range(self.n)] # Array to keep track of the representative elements
        rank = [0] * self.n # Array to keep track of the "height" of each element

        # Helper function to find the representative element (root) 
        # of each disjoint set
        def find_set(vertex):
            if parent[vertex] != vertex:
                parent[vertex] = find_set(parent[vertex])
            return parent[vertex]
        
        # Another helper function to union the sets, which elements
        # u and v belong.
        def merge_sets(u, v):
            root_u = find_set(u)
            root_v = find_set(v)

            if root_u != root_v:
                if rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v
                elif rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                else:
                    parent[root_u] = root_v
                    rank[root_v] += 1

        # Initialize the minimum weight
        min_weight = 0
        # Iterating over sorted edges
        for edge in self.edges:
            # For each edge (u, v, w) we check if including it in the current set of edges 
            # would create a cycle, by checking if u and v belong to different sets
            u, v, w = edge
            if find_set(u) != find_set(v):
                min_weight += w
                # If they don't create a cycle, perform the union operation to
                # merge the sets
                merge_sets(u, v)
        
        return min_weight

if __name__ == "__main__":
    graph = Graph(6)

    connections = (( 1,  2, 17), ( 4,  6, 14), ( 2,  5, 15),
                ( 3,  4,  3), ( 0,  5, 18), ( 3,  5,  8),
                ( 2,  0,  9), ( 0,  2, 19), ( 0,  1, 10),
                ( 1,  0, 13), ( 4,  1, 12), ( 5,  1,  3))

    for u, v, w in connections:
        graph.add(u, v, w)

    print(graph.min_expense()) # 42

    graph.remove(3, 4)
    graph.remove(1, 0)
    graph.remove(4, 1)

    print(graph.min_expense()) # 44
