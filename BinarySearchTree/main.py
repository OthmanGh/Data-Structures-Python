#A binary tree with the property that the value of each node's left child is less than or equal to the node's value, and the value of the right child is greater than or equal to the node's value.

class Node:
    def __init__(self, value, parent = None, left = None, right = None):
        self.data = value
        self.parent = parent
        self.left = left
        self.right = right

