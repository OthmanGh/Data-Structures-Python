# Node class represents an element in the queue
class Node:
    def __init__(self, data, next_node):
        self.data = data  # Data of the node
        self.next = next_node  # Reference to the next node in the queue

# Queue class represents a queue data structure
class Queue:
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None  # Points to the rear of the queue

    # Enqueue: Add a new element to the rear of the queue
    def enqueue(self, data):
        # Create a new node with the given data
        new_node = Node(data, None)

        if self.front is None:
            # If the queue is empty, set both front and rear to the new node
            self.front = self.rear = new_node
        else:
            # If the queue is not empty, add the new node to the rear and update the rear
            self.rear.next = new_node
            self.rear = new_node

    # Dequeue: Remove an element from the front of the queue
    def dequeue(self):
        if not self.empty():
            # If the queue is not empty, move the front to the next node (remove from the front)
            self.front = self.front.next
        else:
            print("Queue is empty....")

    # IsEmpty: Check if the queue is empty
    def empty(self):
        return self.front is None

    # Peek: Return the value at the front of the queue without removing it
    def peek(self):
        if not self.empty():
            return self.front.data
        else:
            print("Queue is empty....")
            return

# Create an instance of the Queue class
my_queue = Queue()

# Enqueue some values to the queue
my_queue.enqueue(30)
my_queue.enqueue(40)
my_queue.enqueue(50)
my_queue.enqueue(60)

# Dequeue and print elements until the queue is empty
while not my_queue.empty():
    print(my_queue.peek(), end=" -> ")
    my_queue.dequeue()

# Print "None" to indicate an empty queue
print("None")
