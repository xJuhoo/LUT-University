# Week 5: Exercises 1 - 3
# Juho Rekonen

# A class for a single node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# A class for the Binary Search Tree
class BST:
    def __init__(self):
        self.root = None
        self.mirrored = False # Boolean value specifying if the BST is mirrored or not
    
    # Function to insert new values
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if node is None:
            return Node(key)
        
        # We ignore duplicates by not even checking or doing anything
        # in cases where key == node.key

        # Inserting into a mirrored BST
        if self.mirrored:
            if key > node.key:
                node.left = self._insert(node.left, key)
            elif key < node.key:
                node.right = self._insert(node.right, key)
            
            return node
    
        # Inserting into a non-mirrored BST
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        
        return node

    # Function to search for values
    def search(self, key):
        if self.root is None:
            return False
        else:
            return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None:
            return False
        
        # Checking the mirrored BST first
        if self.mirrored:
            if node.key == key:
                return True
            elif key < node.key:
                return self._search(node.right, key)
            elif key > node.key:
                return self._search(node.left, key)
            
        # And after that a regular non-mirrored BST
        if node.key == key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        elif key > node.key:
            return self._search(node.right, key)
    
    # Preordered traversal where we check:
    # 1st = root
    # 2nd = left child
    # 3rd = right child
    def preorder(self):
        if self.root is None:
            return
        else:
            self._preorder(self.root)
        print()

    def _preorder(self, node):
        if node:
            print(node.key, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)
    
    # Postordered traversal where we check:
    # 1st = left child
    # 2nd = right child
    # 3rd = root
    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.key, end=' ')

    # Inordered traversal where we check:
    # 1st = left child
    # 2nd = root
    # 3rd = right child
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=' ')
            self._inorder(node.right)
    
    # Function to remove values
    def remove(self, key):
        if self.root is None:
            return
        else:
            self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if node is None:
            return node

        # Removing from a mirrored BST
        if self.mirrored:
            if key > node.key:
                node.left = self._remove(node.left, key)
            elif key < node.key:
                node.right = self._remove(node.right, key)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # Nodes with two children
                temp = self._find_min_node(node.right)
                node.key = temp.key
                node.right = self._remove(node.right, temp.key)

            return node

        # Removing from a regular BST
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Nodes with two children
            temp = self._find_min_node(node.left)
            node.key = temp.key
            node.left = self._remove(node.left, temp.key)

        return node
    
    # Function to find the miminum node
    def _find_min_node(self, node):
        current = node

        # Finding min node in a mirrored BST
        if self.mirrored:
            while current.left:
                current = current.left
            return current
    
        # Finding min node in a regular BST
        while current.right:
            current = current.right
        return current

    # Function to perform Breadth First Search
    def breadthfirst(self):
        if self.root is None:
            return
        else:
            self._breadthfirst(self.root)
        print()

    def _breadthfirst(self, node):
        if node is None:
            return
        
        nodes = []
        nodes.append(node)

        while len(nodes) > 0:
            print(nodes[0].key, end=" ")
            node = nodes.pop(0)

            if node.left is not None:
                nodes.append(node.left)

            if node.right is not None:
                nodes.append(node.right)

    # Function to mirror the BST
    def mirror(self):
        self._mirror(self.root)
    
    def _mirror(self, node):
        self.mirrored = not self.mirrored # Flip the boolean value
        if node:

            self._mirror(node.left)
            self._mirror(node.right)

            temp = node
            temp = node.left
            node.left = node.right
            node.right = temp
    
    
if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)
   
    Tree.postorder()        # 1 3 2 4 9 7 6 5 
    Tree.inorder()          # 1 2 3 4 5 6 7 9  
    Tree.breadthfirst()     # 5 1 9 3 7 2 4 6