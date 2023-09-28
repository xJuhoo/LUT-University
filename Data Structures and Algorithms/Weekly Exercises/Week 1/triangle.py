# Week 1: Exercise 3
# Juho Rekonen

# To get an understanding on how to solve this problem, I had to look up
# "triangle inequality theorem" on Wikipedia.
# https://en.wikipedia.org/wiki/Triangle_inequality

# Which states that in case of any triangle, must apply that the length of two of the sides
# must be greater or equal to the third side. This applies for any two sides of the triangle.

def triangle(a, b, c):
    # First we check if any of the sides is negative (automatically False)
    if (a < 0 or b < 0 or c < 0):
        return False
    
    # Else we check the triangle inequality excluding the "equal" part because
    # in that case it's really no longer a triangle but just two lines.
    if (a + b > c and b + c > a and a + c > b):
        return True
    else:
        return False



if __name__ == "__main__":
    print(triangle(3, 5, 4))
    print(triangle(-1, 2, 3))
    print(triangle(5, 9, 14))
    print(triangle(30, 12, 29))
