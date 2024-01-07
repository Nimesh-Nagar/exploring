# stack implementation using ARRAY without using library 

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity            #max number of elements in array 
        self.stack = [None] * capacity 
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            print("Stack Overflow! Cannot push element.")
        else:
            self.top += 1
            self.stack[self.top] = item
            print(f"Pushed {item} to the stack")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop element.")
            return None
        else:
            popped_item = self.stack[self.top]
            # popped_item = self.stack.pop()
            self.top -= 1
            print(f"Popped {popped_item} from the stack")
            return popped_item

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        else:
            return self.stack[self.top]

    def size(self):
        return self.top + 1

# Example usage:
stack_capacity = 5
stack = Stack(stack_capacity)

stack.push(1)
stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)

# stack.push(6)

print("Top element:", stack.peek())
print("Stack size:", stack.size())

popped_item = stack.pop()
print("Popped item:", popped_item)

popped_item = stack.pop()
print("Popped item:", popped_item)

popped_item = stack.pop()
print("Popped item:", popped_item)

# print(stack.stack)
print("Is the stack empty?", stack.is_empty())
