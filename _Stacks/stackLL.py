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
        # Initialize an empty stack with the head set to None
        self.head = None

    def push(self, value):
        # Push (add) a new element onto the stack
        # Create a new node with the given value and update the head
        n = Node(value, self.head)
        self.head = n

    def pop(self):
        # Pop (remove) the top element from the stack
        if not self.empty():
            # Update the head to point to the next node, effectively removing the top element
            self.head = self.head.next

    def empty(self):
        # Check if the stack is empty
        return self.head == None
    
    def top(self):
        # Return the data of the top element in the stack
        return self.head.data
    
# Create a stack object
s = Stack()

#print(s.empty())

# Push some elements onto the stack
s.push(10)
s.push(30)
s.push(50)
s.push(70)

# print(s.top())
# s.pop()
# print(s.top())

# Print the elements at the top of the stack in a LIFO order
while not s.empty():
    print(s.top(), end=" -> ")
    s.pop()
print()

# Output: 70 -> 50 -> 30 -> 10 ->




