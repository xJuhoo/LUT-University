# Week 11: Exercise 1
# Juho Rekonen

import time

# Using Held-Karp algorithm
def salesman(city_map):
    n = len(city_map)
    memo = {}

    # Helper function for dynamic programming
    def dp(mask, last):
        if mask == (1 << n) - 1:
            return city_map[last][0], [last, 0]  # Return cost and path
        
        if (mask, last) in memo:
            return memo[(mask, last)]
        
        result = float('inf')
        best_path = []

        for i in range(1, n):
            if not (mask & (1 << i)):
                cost, path = dp(mask | (1 << i), i)
                cost += city_map[last][i]

                if cost < result:
                    result = cost
                    best_path = [last] + path

        memo[(mask, last)] = result, best_path
        return result, best_path

    # Call the dynamic programming function to get the optimal cost and path
    cost, path = dp(1, 0)  # Start with city 0 and an empty mask

    return path  # Return the optimal path


if __name__ == "__main__":
    cost = 0

    start_time = time.time()
    
    city_map = [
        [ 0, 12, 19, 16, 29, 30, 18, 8, 12, 27],
        [12,  0, 27, 25,  5, 30, 18, 8, 12, 27],
        [19, 27,  0,  8,  4, 30, 18, 8, 12, 27],
        [16, 25,  8,  0, 14, 30, 18, 8, 12, 27],
        [29, 5, 4, 14, 0, 30, 18, 8, 12, 27],
        [ 2, 12, 19, 16, 29, 0, 18, 8, 12, 27],
        [12,  39, 27, 25,  5, 30, 0, 8, 12, 27],
        [19, 27,  9,  8,  4, 30, 18, 0, 12, 27],
        [16, 25,  8,  11, 14, 30, 18, 8, 0, 27],
        [29,  5,  4, 14,  2, 30, 18, 8, 12, 0]
        ]

    path = salesman(city_map)
    
    for i in range(len(city_map)):
        cost += city_map[path[i]][path[(i + 1) % len(city_map)]]
    
    print(path)
    print(cost)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")



