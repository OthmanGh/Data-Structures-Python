# A linked list is a linear data structure used in computer science to organize and store data. Unlike arrays, which use contiguous memory locations to store elements, a linked list consists of nodes where each node contains data and a reference (or link) to the next node in the sequence.

# Basic Operations : 
#     - Insertion
#     - Searching
#     - Deletion
#     - Creating a Linked List
#     - Deleting a Linked List
#     - Printing a Linked List


class Node:
    def __init__(self, value, next):
        self.data = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def push_front(self,value):
        n = Node(value, None)

        if self.head == None: # list is empty 
            self.head = self.tail = n
            self.length = 1

        else:
            n.next = self.head
            self.head = n
            self.length  +=1
    

    def push_back(self, value):
        n = Node(value, None)

        if self.head == None:
            self.head = self.tail = n
            self.length = 1

        else:
            self.tail.next = n
            self.tail = n
            self.length =1

    def printList(self):
        if self.head == None:
            print("List is empty....")

        else:
            temp = self.head
            while(temp != None):
                print(f"{temp.data}", end=" -> ")
                temp = temp.next

            print("None")

myList = LinkedList()


myList.push_back(40)
myList.push_front(10)
myList.push_front(30)
myList.push_back(50)
myList.push_front(20)
myList.push_back(60)

myList.printList()