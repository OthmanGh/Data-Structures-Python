# Implement Stack using LinkedList

# Node class represents individual nodes in the linked list

class Node:
    def __init__(self, value, next = None):
        # Initialize node with data and a reference to the next node
        self.data = value
        self.next = next

# Stack class represents a stack implemented using a linked list
class Stack:
    def __init__(self):
        # Initialize an empty stack with the top set to None
        self.top = None

    def push(self, value):
        # Push (add) a new element onto the stack
        # Create a new node with the given value and update the top
        n = Node(value, self.top)
        self.top = n

    def pop(self):
        # Pop (remove) the top element from the stack
        if not self.empty():
            # Update the top to point to the next node, effectively removing the top element
            self.top = self.top.next

    def empty(self):
        # Check if the stack is empty
        return self.top == None
    
    def peek(self):
        # Return the data of the top element in the stack
        return self.top.data
    
# Create a stack object
s = Stack()

#print(s.empty())

# Push some elements onto the stack
s.push(10)
s.push(30)
s.push(50)
s.push(70)

# print(s.peek())
# s.pop()
# print(s.peek())

# Print the elements at the top of the stack in a LIFO order
while not s.empty():
    print(s.peek(), end=" -> ")
    s.pop()
print()

# Output: 70 -> 50 -> 30 -> 10 ->




