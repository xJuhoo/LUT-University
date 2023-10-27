# Week 7: Exercise 3
# Juho Rekonen

def queen(n, m):
    # We call the solutions function with starting column 0 and
    # three dictionaries that keep track of occupied rows, forward
    # diagonals and backward diagonals
    return solutions(n, 0, {}, {}, {}, m)

# Function to calculate recursively all possible solutions
def solutions(n, column, horizontal, diaForward, diaBackward, m):
    # If all queens have been placed
    if m == 0:
        return 1
    
    # If we reach the end of the grid before all queens have been
    # placed, there are no solutions
    if column == n:
        return 0

    total_solutions = 0

    for row in range(n):
        # Check if current row and diagonals are not occupied (i.e, if 
        # the grid[row][column] is available)
        if (
            row not in horizontal
            and (row + column) not in diaForward
            and (row - column) not in diaBackward
        ):
            
        # Conditions met, place a dot and recursively call the function
            horizontal[row] = True
            diaForward[row + column] = True
            diaBackward[row - column] = True

            # In the function call we reduce the remaining queens (m) by 1
            total_solutions += solutions(n, column + 1, horizontal, diaForward, diaBackward, m - 1)

            # Backtracking by removing the dot
            del horizontal[row]
            del diaForward[row + column]
            del diaBackward[row - column]

    total_solutions += solutions(n, column + 1, horizontal, diaForward, diaBackward, m)

    return total_solutions

if __name__ == "__main__":
    print(queen(4, 4))  # Output: 2
    print(queen(4, 2))  # Output: 44
    print(queen(6, 4))  # Output: 982
    print(queen(7, 2))  # Output: 700
    print(queen(8, 8))  # Output: 92
