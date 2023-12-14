#A binary tree with the property that the value of each node's left child is less than or equal to the node's value, and the value of the right child is greater than or equal to the node's value.

class Node:
    def __init__(self, value, parent = None, left = None, right = None):
        self.value = value
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
            

    def search(self, info):
        if self.root == None:
            return False
        
        else:
            current = self.root

            while current != None:

                if current.value == info:
                    return True
                elif current.value > info:
                    current = current.left
                else:
                    current = current.right
            
            return False


    def recursive_search(self, info, current):
        if current == None:
            return False
        
        if current.value == info:
            return True
        
        elif current.value > info:
            return self.recursive_search(info, current.left)
        
        else:
            return self.recursive_search(info, current.right)
        


    def inOrder(self, current):
        if current == None:
            return 
        self.inOrder(current.left)
        print(current.value, end=" ")
        self.inOrder(current.right)

    



# Create an instance of the BST
bst = BST()

# Add values to the BST
bst.add(50)
bst.add(30)
bst.add(70)
bst.add(20)
bst.add(40)
bst.add(60)
bst.add(80)

# Print the tree using in-order traversal
print("In-order traversal:")
bst.inOrder(bst.root)
print()

# Test searching for values
search_value = 40
print(f"Is {search_value} in the BST? {bst.search(search_value)}")

search_value = 55
print(f"Is {search_value} in the BST? {bst.search(search_value)}")

# Test recursive search
search_value = 30
print(f"Is {search_value} in the BST (recursive)? {bst.recursive_search(search_value, bst.root)}")

search_value = 75
print(f"Is {search_value} in the BST (recursive)? {bst.recursive_search(search_value, bst.root)}")
