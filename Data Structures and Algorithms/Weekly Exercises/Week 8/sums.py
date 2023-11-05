# Week 8: Exercise 2
# Juho Rekonen

# To solve this program efficiently, using a database is needed, where rows contains
# the size of the current array and columns contains the sum of elements in corresponding array
def sums(array):
    # We need both the sum and the length of the array for iterations
    arrSum = sum(array)
    n = len(array)

    # Creating the database with every value dp[i][j] being False, so once
    # a sum can be created, the values are changed to True
    dp = [[False for i in range(arrSum + 1)]
          for i in range(n + 1)]

    # Database starts with row and column indexes 0, where the 0th row 
    # (i.e., arrays with size of 0) can just be ignored and left to False
    # However the value dp[0][0] must be True so we can start counting the sums 
    # from there.
    dp[0][0] = True

    # Filling the database
    for i in range(1, n + 1): # Iterating through all elements in the array
        for j in range(arrSum + 1): # Iterating over all possible sums

        # We check if there is a subset of elements from the first i - 1 
        # elements that can form a sum equal to j
            if dp[i - 1][j]:
                dp[i][j] = True

                # This also means that we can form a sum of j + array[1 - 1]
                # by including the current element in the subset
                dp[i][j + array[i - 1]] = True

    # To get all the possible distinct sums, we count the number of 
    # True values in the last row starting from value 1
    return sum(1 for value in dp[n][1:] if value)

if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2])) # 121
