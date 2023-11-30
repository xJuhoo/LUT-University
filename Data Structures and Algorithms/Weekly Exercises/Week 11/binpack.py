# Week 11: Exercise 2
# Juho Rekonen

def binpack(items, S):
    # Sort items in non-increasing order
    items = sorted(items, reverse=True)

    # Initialize bins
    bins = [[]]

    # Iterate through each item
    for item in items:
        # Try to place the item in the first bin where it fits
        placed = False
        for bin_ in bins:
            if sum(bin_) + item <= S:
                bin_.append(item)
                placed = True
                break

        # If the item couldn't be placed in any existing bin, create a new bin
        if not placed:
            bins.append([item])

    return bins

if __name__ == "__main__":
    items = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
    B = 10

    bins = binpack(items, B)

    for i in range(len(bins)):
        print(f"bin {i+1}: {bins[i]}")


