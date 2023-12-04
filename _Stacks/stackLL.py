# Implement Stack using LinkedList

class Node:
    def __init__(self, value, next = None):
        self.data = value
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        # create node data : 
        n = Node(value, self.head)
        self.head = n

    def pop(self):
        if not self.empty():
            self.head = self.head.next

    def empty(self):
        return self.head == None
    
    def top(self):
        return self.head.data

s = Stack()

#print(s.empty())

s.push(10)
s.push(30)
s.push(50)
s.push(70)

# print(s.top())
# s.pop()
# print(s.top())

while not s.empty():
    print(s.top(), end=" -> ")
    s.pop()
print()