# Week 1: Exercise 1
# Juho Rekonen

# Function to sort the given array
def isort(A):
    for i in range(1, len(A)):
        j = i - 1
        while j >= 0 and A[j] > A[j + 1]:
            # Here we perform the swap
            A[j], A[j + 1] = A[j + 1], A[j]
            # This swap might affect the order of the previous element so we have to check that aswell
            # For example A = [1, 2, 3, 7, 2], after swapping 7 and 2, we have to go back to values 3 and 2 to swap them
            j -= 1

if __name__ == "__main__":
    A = [4, 3, 6, 2, 9, 7, 1, 8, 5]
    isort(A)
    print(A)
