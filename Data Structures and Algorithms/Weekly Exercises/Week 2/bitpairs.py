# Week 2: Exercise 2
# Juho Rekonen

# This problem is really easy to solve with time complexity O(n^2) with the following algorithm:

# def pairs(s):
    # counter = 0
    # for i in range(len(s)):
        # for j in range(i + 1, len(s)):
            # if s[i] == "1" and s[j] == "1":
                # counter += (j - i)
        
    # return counter

# The way I think the algorithm could be made more efficient is if we would assume that 
# every 1 bit in the string would be at index 0. This is so that we could get the total distance
# moved. We could still keep track of the amount of 1 bits encountered and the distance
# between same occurences. What would change however is the way we count up the sum of the distances.

# So lets have the "100101" for example. Here are the steps
# At index 0, we find a 1. Sum += 0 * 0 - 0 (encountered 1's so far * current index - distance)
# At index 3, we find another 1. Sum += 1 * 3 - 0 = 3 (increment encountered 1 bits)
# At index 5, we find the last 1. Sum += 2 * 5 - 3 = 7
# So after three 1 bits, the total sum is 0 + 3 + 7 = 10. 
# Alright that could work!


def pairs(s):

    n = len(s)
    # Checking the limit
    if n > 10**5:
        return 0
    
    # Initializing all the values
    sum_of_distances = 0
    encounters = 0
    current_distance = 0

    for i in range(0, n):
        # At each index we check if a 1 bit is found
        if s[i] == "1":
            # Perform the calculation for the sum
            sum_of_distances += encounters * i - current_distance

            # Increment encountered 1 bits by 1
            encounters += 1

            # Distance increases the amount of indexes moved from 0
            current_distance += i

    # Return the sum of all distances
    return sum_of_distances

if __name__ == "__main__":
    print(pairs("100101"))
    print(pairs("101"))
    print(pairs("100100111001"))
