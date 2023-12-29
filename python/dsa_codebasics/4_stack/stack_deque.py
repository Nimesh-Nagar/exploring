from collections import deque 

class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
        
    def peek(self):                 
        return self.container[-1]           # returns last value in stack
        
    def is_empty(self):
        return len(self.container) == 0     # returns True is stack is empty
    
    def size(self):
        return len(self.container)          # returns length of stack 
    

if __name__ == "__main__":
    
    s = Stack()
    s.push(5)
    s.push(29)
    
    print(s.peek())
    
    
    # print(s.size())
    print(s.is_empty())
    