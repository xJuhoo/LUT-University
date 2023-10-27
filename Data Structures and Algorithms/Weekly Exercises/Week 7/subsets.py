# Week 7: Exercise 2
# Juho Rekonen

def subsets(n: int) -> list:
    # Creating the array
    A = [i for i in range(1, n + 1)]

    # Returning the subset combinations
    return [x for x in get_subsets(A) if x]
 
# Function to create subsets
def get_subsets(A):
    # For each element in the array, it's either included or excluded
    # in a subset so possible combinations for n elements is 2^n
    size = 2 ** len(A)

    for i in range(size):
        subset = []

        # For each element we check the binary representation of the element
        # which is either 0 or 1
        for j in range(len(A)):
            
            # In the condition we check whether the j-th bit of i
            # is set to 1. If it is, the j-th element is included in
            # the current subset
            if ((i & (1 << j)) > 0):
                subset.append(A[j])
        yield subset

if __name__ == "__main__":
    print(subsets(1))   # [[1]]
    print(subsets(2))   # [[1], [2], [1, 2]]
    print(subsets(3))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(subsets(4))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
                        #  [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4],
                        #  [2, 3, 4], [1, 2, 3, 4]]
    S = subsets(10)
    print(S[95])    # [6, 7]
    print(S[254])   # [1, 2, 3, 4, 5, 6, 7, 8]
    print(S[826])   # [1, 2, 4, 5, 6, 9, 10]

