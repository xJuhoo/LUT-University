# Week 2: Exercise 3
# Juho Rekonen

# The way I'm thinking this problem to run on O(n) time complexity, we must iterate through the list
# from left to right and keep track of the highest number at every index.
# Same way, we must iterate from right to left and keep track of the lowest number at every index.

# Once we have done that, iterating one more time through the list, at every index of the list
# we check whether the highest number on the left side is smaller than the lowest number on the right side.
# If it is, that's a valid splitting point.

def split(A):
    # We need the length of the list for the iterations
    n = len(A)

    # Check the limits
    if n < 1 or n > 10**5:
        return 0

    # Initializing the lists for the highest and lowest numbers
    highest = [A[0]] * n # Indexes from left to right
    lowest = [A[-1]] * n # Indexes from right to left

    # At every index on the list A, we mark the highest number so far
    for i in range(1, n):
        highest[i] = max(highest[i - 1], A[i])

    # And same goes from right to left marking the lowest number so far
    for i in range(n - 2, -1, -1):
        lowest[i] = min(lowest[i + 1], A[i])

    # Calculate the number of valid splitting points
    counter = 0
    for i in range(0, n - 1):
        if highest[i] < lowest[i + 1]:
            counter += 1

    return counter

if __name__ == "__main__":
    print(split([1, 2, 3, 4, 5]))
    print(split([5, 4, 3, 2, 1]))
    print(split([2, 1, 2, 5, 7, 6, 9]))
    print(split([1, 2, 3, 1]))
