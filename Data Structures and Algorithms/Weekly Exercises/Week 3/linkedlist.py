# Week 3: Exercise 1 - 3
# Juho Rekonen

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Function to append values to the end of the list
    def append(self, data):
        new_node = Node(data)
        # Check if any nodes exists yet
        if not self.head:
            self.head = new_node
            return
        
        # In case we already have some nodes, just append the current node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node


    # Function to insert new values
    def insert(self, data, index):
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        # In case of any other position than i = 0
        current = self.head
        for _ in range(index - 1):
            if current:
                current = current.next
            else:
                return None

        if current:
            new_node.next = current.next
            current.next = new_node
        else:
            return None
    

    # Function to delete values from given position
    def delete(self, index):
        if index == 0:
            if self.head:
                data = self.head.data
                self.head = self.head.next
                return data
            else:
                return None

        current = self.head
        for _ in range(index - 1):
            if current is None or current.next is None:
                return None
            current = current.next

        if current is None or current.next is None:
            return None

        data = current.next.data
        current.next = current.next.next
        return data
    

    # Function to get the index of the data given
    def index(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1
    

    # Function to swap two values at indeces i and j
    def swap(self, i, j):
        # If the indeces are the same, no changes are needed
        if i == j:
            return

        # Then we have to find the data values at positions i and j
        node_i = self.head
        for _ in range(i):
            if node_i is None:
                return
            node_i = node_i.next

        node_j = self.head
        for _ in range(j):
            if node_j is None:
                return
            node_j = node_j.next

        # Then again must be checked that the values exists
        if not node_i or not node_j:
            return

        # Swap the data of nodes at positions i and j
        node_i.data, node_j.data = node_j.data, node_i.data


    # Function to sort the linked list in ascending order
    def isort(self):
        # If the list is empty or only has 1 element, it's already sorted
        if not self.head or not self.head.next:
            return

        sorted_head = None # Initialize the head of the sorted list
        current = self.head # Using a current node to traverse the linked list

        while current:
            next_node = current.next

            # Check if the sorted list is empty or if the current node is less than the 
            # first node of the sorted list. If it is, we simply insert the current node at the
            # beginning of the sorted list
            if sorted_head is None or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current

            # In cases where the current node is more than the node in the sorted list
            # we use a temporary node to search the correct position for the current node
            # and insert into it.
            else:
                temp = sorted_head # Locating the insertion point
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                # Insertion
                current.next = temp.next
                temp.next = current

            current = next_node

        self.head = sorted_head

    # Function to print the Linked List
    def print(self):
        current = self.head
        while current:
            if current.next is None:
                print(current.data)
            else:
                print(current.data, end=" -> ")
            current = current.next

if __name__ == "__main__":
    L = LinkedList()
    L.append(1)
    L.append(3)
    L.print()           # 1 -> 3
    L.insert(10, 1)
    L.insert(15, 0)
    L.print()           # 15 -> 1 -> 10 -> 3
    L.delete(0)
    L.print()           # 1 -> 10 -> 3
