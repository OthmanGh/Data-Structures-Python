#A binary tree with the property that the value of each node's left child is less than or equal to the node's value, and the value of the right child is greater than or equal to the node's value.


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.right = right
        self.left = left

class BST:
    def __init__(self):
        self.root = None


my_tree = BST()

print(my_tree.root)