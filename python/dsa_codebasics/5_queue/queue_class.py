from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, value):
        self.buffer.appendleft(value)
        
    def dequeue(self):
        return self.buffer.pop()
        
    def is_empty(self):
        return len(self.buffer) == 0 
    
    def size(self):
        return len(self.buffer)
    
if __name__ == "__main__":
    
    q = Queue()
    
    print("Enque data in Queue")
    q.enqueue({
    'company': 'Tata',
    'timestamp': '15 dec, 11.01 AM',
    'price': 131.10
    })
    
    q.enqueue({
    'company': 'Tata',
    'timestamp': '15 dec, 11.02 AM',
    'price': 132
    })
    
    q.enqueue({
    'company': 'Tata',
    'timestamp': '15 dec, 11.03 AM',
    'price': 135.22
    })
        
    print(q.buffer)
    print( f" Size of Queue :- {q.size()}" )
    
    print("\nDequeue Data from Queue ")
    print(q.dequeue())
    print(q.dequeue())
    
    print("\n")
    print(q.buffer)
    
    