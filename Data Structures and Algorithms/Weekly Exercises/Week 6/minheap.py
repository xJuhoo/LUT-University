# Week 6: Exercise 2
# Juho Rekonen

# Class for The Min Heap
class MinHeap:
    def __init__(self, A):
        self.heap = A
        n = len(A)
        # Building the min heap directly in the initializing
        for i in range(n // 2 - 1, -1, -1):
            self.heap_down(i)


    def push(self, key):
        self.heap.append(key)
        self.heap_up(len(self.heap) - 1)


    def pop(self):

        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Adjust the min heap when removing the first value
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min = self.heap.pop()
        self.heap_down(0)

        # Return removed value
        return min


    # Printing the min heap again using a one-liner
    def print(self):
        print(' '.join(map(str, self.heap)))


    def heap_up(self, index):
        if index == 0:
            return
        
        parent = (index - 1) // 2 # Rounding down to nearest integer
        if self.heap[parent] > self.heap[index]:
            # Perform swap
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heap_up(parent)


    def heap_down(self, i):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        smallest = i

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heap_down(smallest)


if __name__ == "__main__":
    heap = MinHeap([4, 8, 6, 5, 1, 2, 3])
    heap.print()  # 1 4 2 5 8 6 3
    print(heap.pop())  # 1
    heap.push(9)
    heap.print()  # 2 4 3 5 8 6 9

