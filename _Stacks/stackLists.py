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
            raise IndexError("pop from an empty stack")

    def empty(self): # Method to check if the stack is empty
        return len(self.list) == 0
    
    def top(self): # Method to return the element at the top of the stack without removing it
        if not self.empty(): # Check if the stack is not empty
            return self.list[-1]
        else:
            raise IndexError("top from an empty stack")
        

    def insert_at_bottom(self, value):
        # base case 
        if self.empty():
            self.push(value)
            return

        # recursive case :
        temp = self.top()
        self.pop()
        self.insert_at_bottom(value)
        self.push(temp)
  

    def reverse(self):
        if self.empty():
            return
        
        top = self.top()
        self.pop()
        self.reverse()
        self.insert_at_bottom(top)

# Create a stack object
s = Stack()

# Push some elements onto the stack
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.insert_at_bottom(60)
s.reverse()

# Print the element at the top of the stack
#print(s.top())

# Pop and print all elements from the stack
print("Stack : ")
while not s.empty():
    print(s.top())
    s.pop()
print()