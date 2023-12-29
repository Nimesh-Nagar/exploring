# STACK Data structure . LIFO (Last-In First-Out) 
"""
Using list as stack in python is not recommended as List is a Dynamic array.
Recommended approch is to use collections.deque . Deques support thread-safe, 
memory efficient appends and pops from either side of the deque with approximately 
the same O(1) performance in either direction. 

"""
# stack = []

# stack.append('A')
# stack.append('B')
# stack.append('C')

# print(f"Inital STACK ---> {stack} ")

# print("Pop Operation on STACK ")
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print(stack.pop()) # it will create erros as stack is empty 

## Implementation of STACK using deque
from collections import deque

stack = deque()
stack.append("A")
stack.append("B")
stack.append("C")

print(stack)
stack.pop()
print(stack)
