# Week 1: Exercise 2
# Juho Rekonen

# This problem could be done simply in O(N^2) time with one loop iterating through all numbers from 2 to N
# (because 1 is not a prime number) and another loop checking whether the current element is divisible by 
# any of the previous elements (so for example in case of 7, divisibility by 2, 3, 4, 5 and 6 must be checked).

# However that is not a very effective method if the given number N is large. 
# I am using a method called Sieve of Eratosthenes (Eratostheneen seula) because it allows my program to check
# fewer numbers, by finding a prime number and then eliminating all of it's multiples.

# So for example when the first prime number encountered is 2, there is no need to check numbers 4, 6, 8, 10 and so on
# and we can just move onwards to the next "non-eliminated number" which would be 3 in this case.


def primes(N):
    # Checking the corner cases
    if (N <= 1 or N > 10**5):
        return 0
    elif (N == 2):
        return 1

    # First we create an array of numbers where we "expect" them all to be prime numbers
    prime_numbers = [True] * (N + 1)
    counter = 0
    i = 2 # Starting point

    # Now we iterate through the array
    while (i * i <= N):
        # If the value of the element is true, it is a prime number and therefore all of it's
        # multiplies are not
        if (prime_numbers[i] == True):
            for j in range(i * i, N + 1, i): # (i * i means that with for example i = 2, we start eliminating at 4)
                prime_numbers[j] = False
        i += 1

    # Lastly we count the prime numbers
    for i in range(2, N + 1):
        if (prime_numbers[i] == True):
            counter += 1

    return counter


if __name__ == "__main__":
    print(primes(7))
    print(primes(15))
    print(primes(50))
