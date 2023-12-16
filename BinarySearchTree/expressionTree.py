class Node:
    def __init__(self, value, parent, right, left):
        self.value = value
        self.right = right
        self.left = left

class ExpTrees:
    def __init__(self):
         self.root = None
    

    
    def evaluate(self, current):
        if current == None:
            return 
        print("(")
        self.evaluate(current.left)
        print(current.value, end=" ")
        self.evaluate(current.right)
        print(")")

n0 = Node("*", None, None)
n1 = Node("+", None, None)

n2 = Node(-2, None, None)
n3 = Node(22, None, None)
n4 = Node(5, None, None)


et = ExpTrees()
et.root = n0
n0.left = n1
n1.left = n2
n1.right = n3
n0.right = n4 

et.evaluate(et.root)