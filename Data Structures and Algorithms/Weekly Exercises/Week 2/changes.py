# Week 2: Exercise 1
# Juho Rekonen

# It's pretty simple task to solve this problem efficiently in O(n) time
# by iterating through the list only once and making changes on the way

def changes(A):
    # We are going to be iterating through the list so we need the length
    n = len(A)

    # Here we check that the amount of numbers falls into the given range
    if n < 1 or n > 10**5:
        return 0
    
    counter = 0

    for i in range(1, n):
        # Here we check if the adjacent elements are equal
        if A[i] == A[i - 1]:
            # We can't just substitute any number here because in some cases
            # it wouldn't make a change at all (for example always substituting number 5,
            # we could have multiple 5's in the list so they wouldn't change).

            # But from the limits we know that 0 can't exist in the list
            # So let's substitute that
            A[i] = 0
            counter += 1

    return counter



if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))
    print(changes([1, 2, 3, 4, 5]))
    print(changes([1, 1, 1, 1, 1]))
