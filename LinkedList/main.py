# A linked list is a linear data structure used in computer science to organize and store data. Unlike arrays, which use contiguous memory locations to store elements, a linked list consists of nodes where each node contains data and a reference (or link) to the next node in the sequence.

# Basic Operations : 
#     - Insertion
#     - Searching
#     - Deletion
#     - Creating a Linked List
#     - Deleting a Linked List
#     - Printing a Linked List


class Node :
    def __init__(self, value, next): # constructor
        self.data = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # *  Implementation of adding nodes at the beginning, ending && pos : 

    def push_front(self, value):
        n = Node(value, None)

        # If List is empty : 
        if self.head == None:
            self.head = self.tail = n
            self.length = 1

        else:
            n.next = self.head
            self.head = n
            self.length +=1 


    def push_back(self, value):
        n = Node(value, None)

        # If List is empty : 
        if self.head == None:
            self.head = self.tail = n
            self.length = 1

        else:
            self.tail.next = n 
            self.tail = n
            self.length += 1


    def insert(self, pos, value):
        if pos < 0 or pos > self.length: # If pos val out of range
            print("invalid index value")
            return

        if pos == 0: # add at the beginning 
            self.push_front(value)
        
        elif pos == self.length: # add at the end
            self.push_back(value)

        else: # otherwise : 
            temp = self.head # Get a copy of the head pointer
            n = Node(value, None) # Create a new node with the given value and a None next pointer
            counter = 0

            while(counter < pos - 1): # Traverse the list until reaching the node before targeted position
                temp = temp.next
                counter += 1            
            
            # Insert the new node in between the current node and the next node
            n.next = temp.next 
            temp.next = n
            
            self.length +=1   # update list length val


    # *  Implementation of deleting nodes at the beginning, ending && pos : 
    
    def pop_front(self): # This func takes Constant time O(1)
        if self.head == None:
            print("List is empty....")

        else:
            self.head = self.head.next
            self.length -= 1

    def pop_back(self): # This func takes Linear time O(n)
        if self.head == None:
            print("List is empty....")

        else:
            temp =self.head

            while temp.next.next != None: # Travers the list until reaching the node before targeted position
                temp = temp.next

            temp.next = None
            self.tail = temp
            self.length -= 1


    def pop(self, pos):
        if pos < 0 or pos >= self.length: # If pos val out of range
            print("invalid index value")
            return
        
        if pos == 0:
            self.pop_front()
        elif pos == self.length - 1:
            self.pop_back()
        
        else:
            temp = self.head
            counter = 0

            while(counter < pos - 1): # Traverse the list until reaching the node before specified node
                temp = temp.next
                counter +=1

            temp.next = temp.next.next
            self.length -= 1


    def reverse(self):
        c = self.head
        prev = None

        while(c != None):
            next = c.next
            c.next = prev

            # update : 
            prev = c
            c = next

        self.head = prev
        


    # * Printing Linked List Func : 

    def printLL(self):
        # Check if list is empty : 
        if self.head == None:
            print("List is empty....")
        
        else:
            temp = self.head
            while(temp != None):
                print(f"{temp.data}", end=" -> ")
                temp = temp.next
            print("None")
            print("Length of list : ", self.length)

myList = LinkedList()
# myList.push_front(12)
# myList.insert(1, 56)
# myList.insert(2, 76)
# myList.printLL()

# #myList.pop(0)
# myList.pop(3) # node containing 11 deleted

myList.push_back(10)
myList.push_back(20)
myList.push_back(30)
myList.push_back(40)



myList.reverse()
myList.printLL()

# myList.push_front(30)
# myList.push_back(40)
# myList.push_front(20)
# myList.push_back(50)
# myList.push_front(10)

# myList.insert(3, 60)
# myList.insert(4, 70)

# myList.pop_front()
# myList.pop_back()
# myList.pop_back()
# myList.pop(2)
# myList.printLL()