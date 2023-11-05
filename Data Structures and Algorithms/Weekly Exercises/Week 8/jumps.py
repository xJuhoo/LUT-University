# Week 8: Exercise 1
# Juho Rekonen

# We can solve this problem in linear time by using a list to keep track of
# the number of ways to reach each level from 0. Then, for each level from 1 to n,
# we calculate the number of ways to reach that level by summing the number of ways
# to reach it from levels a and b below it

def jumps(n, a, b):
    if n == 0:
        return 1

    ways = [0] * (n + 1)
    ways[0] = 1

    # By using the list we only need to iterate through the array once
    for i in range(1, n + 1):
        if i >= a:
            ways[i] += ways[i - a]
        if i >= b:
            ways[i] += ways[i - b]

    # Return the number of ways to reach level n
    return ways[n]


if __name__ == "__main__":
    print(jumps(4, 1, 2)) # 5
    print(jumps(8, 2, 3)) # 4
    print(jumps(11, 6, 7)) # 0
    print(jumps(30, 3, 5)) # 58
    print(jumps(100, 4, 5)) # 1167937

