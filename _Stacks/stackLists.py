# Implementing Stack data structure using lists

class Stack:
    def __init__(self): # Constructor to initialize an empty list as the stack
        self.list = []

    def push(self, data): # Method to push (add) an element to the top of the stack
        self.list.append(data)
    
    def pop(self): # Method to pop (remove) the element from the top of the stack
        if not self.empty(): # Check if the stack is not empty
            self.list.pop()
        else:
            print("Stack is empty...")
            return None

    def empty(self): # Method to check if the stack is empty
        return len(self.list) == 0
    
    def top(self): # Method to return the element at the top of the stack without removing it
        if not self.empty(): # Check if the stack is not empty
            return self.list[-1]
        else:
            print("Stack is empty...")
            return -1
        
# Create a stack object
s = Stack()

# Push some elements onto the stack
s.push(10)
s.push(5)
s.push(2)
s.push(0)

# Print the element at the top of the stack
print(s.top())

# Pop and print all elements from the stack
while not s.empty():
    print(s.top(), end=" -> ")
    s.pop()

# The stack is now empty, attempting to get the top element will print a message
print() 
print(s.top()) # Stack is empty...
