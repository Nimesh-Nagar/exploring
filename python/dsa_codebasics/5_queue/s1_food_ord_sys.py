from collections import deque
import time
import threading

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
    
q = Queue()

def place_ord(ords):
    
    for item in ords:
        print(f"Placing Order : {item}")
        q.enqueue(item) 
        time.sleep(0.5)
       
    

def serve_ord():
        
    servered = q.size() 
    time.sleep(1)
    while servered != 0:      
        print(q.dequeue())
        servered = q.size()
        time.sleep(2)

    
if __name__ == "__main__":
    
    
    orders = ['pizza','samosa','pasta','biryani','burger']
   
    t1 = threading.Thread(target=place_ord, args=(orders,))
    t2 = threading.Thread(target=serve_ord)
    
    t1.start()
    # time.sleep(1)
    t2.start()
    
    t1.join()
    t2.join()
    
    
    