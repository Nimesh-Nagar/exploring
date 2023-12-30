from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, value):
        self.buffer.appendleft(value)
        
    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty !")
            return
        
        return self.buffer.pop()
        
    def is_empty(self):
        return len(self.buffer) == 0 
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]
    
def create_binary_num(num):

    num_q = Queue()
    num_q.enqueue("1")

    for i in range(num):
        front = num_q.front()
        print(f" {front} ")
        num_q.enqueue(front + "0")
        num_q.enqueue(front + "1")

        num_q.dequeue()
    
if __name__ == "__main__":
    
    create_binary_num(10)
