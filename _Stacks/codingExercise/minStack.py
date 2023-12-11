# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

        return None
    
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

        else:
            pass
        

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1
        

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return -1
        

# Test Case 1
min_stack_1 = MinStack()
min_stack_1.push(5)
min_stack_1.push(2)
min_stack_1.push(7)
print("Top:", min_stack_1.top())  # Output should be 7
print("Min:", min_stack_1.getMin())  # Output should be 2
min_stack_1.pop()
print("Top:", min_stack_1.top())  # Output should be 2
print("Min:", min_stack_1.getMin())  # Output should be 2

# Test Case 2
min_stack_2 = MinStack()
min_stack_2.push(3)
min_stack_2.push(1)
min_stack_2.push(4)
min_stack_2.push(2)
print("Top:", min_stack_2.top())  # Output should be 2
print("Min:", min_stack_2.getMin())  # Output should be 1
min_stack_2.pop()
min_stack_2.pop()
print("Top:", min_stack_2.top())  # Output should be 1
print("Min:", min_stack_2.getMin())  # Output should be 1
