"""
Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
    reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
"""


from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self,val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
        
    def peek(self):                 
        return self.container[-1]           # returns Top-most value from stack
        
    def is_empty(self):
        return len(self.container) == 0     # returns True is stack is empty
    
    def size(self):
        return len(self.container)          # returns length of stack 
    
        
    def reverse_string(self,str):
        self.push(str)
        data = self.container[-1]
        
        rev = ""
        for ch in data:
            rev = ch + rev
        return rev

        # return data[::-1] # string slicing
        
def rev_str(str):
    stack = Stack()
    stack.push(str)
    
    rstr = ""
    for ch in stack.peek():
        rstr = ch + rstr
        
    return rstr 

if __name__ == "__main__":
    
    s = Stack()
    s.push("Nimesh")
    s.push("Nagar")
    
    print(s.reverse_string("We will conquere COVID-19"))
    print(rev_str("nimesh"))
    
    