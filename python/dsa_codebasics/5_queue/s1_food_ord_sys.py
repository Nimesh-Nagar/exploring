from collections import deque
import time
import threading

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
    
order_queue = Queue()

def place_ord(ords):
    
    for item in ords:
        print(f"Placing Order : {item}")
        order_queue.enqueue(item) 
        time.sleep(0.5)
       
    

def serve_ord():
        
    servered = order_queue.size() 
    time.sleep(1)
    while servered != 0:      
        print(order_queue.dequeue())
        servered = order_queue.size()
        time.sleep(2)

    # time.sleep(1)
    # while True:
    #     order = order_queue.dequeue()
    #     print("Now serving: ",order)
    #     time.sleep(2)
        
        
    
if __name__ == "__main__":
    
    
    orders = ['pizza','samosa','pasta','biryani','burger']
   
    t1 = threading.Thread(target=place_ord, args=(orders,))
    t2 = threading.Thread(target=serve_ord)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    
    