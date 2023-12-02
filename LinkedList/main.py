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
        self.length = 0