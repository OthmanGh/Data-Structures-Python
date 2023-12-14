#A binary tree with the property that the value of each node's left child is less than or equal to the node's value, and the value of the right child is greater than or equal to the node's value.

class Node:
    def __init__(self, value, parent = None, left = None, right = None):
        self.data = value
        self.parent = parent
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    
    def add(self, value):
        n = Node(value)

        if self.root == None:
            self.root = n

        else:
            current = self.root
            self.add_helper(n, current)

    def add_helper(self, n, current):
        if current.value > n.value:
            if current.left == None:
                current.left = n
                n.parent = current
                return 
            else:
                return self.add_helper(n, current.left)
            
        else:
            if current.right == None:
                current.right = n
                n.parent = current
                return
            
            else:
                return self.add_helper(n, current.right)
            