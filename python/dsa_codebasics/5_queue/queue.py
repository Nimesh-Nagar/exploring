# Array implementation of Queue without using library 

# to represent Queue
class Queue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.front = self.size = 0 
        self.rear = capacity - 1 
        self.arr = [None] * capacity
        
    # to check queue is full or not 
    def is_full(self):
        return self.size == self.capacity
    
    # to check queue is empty or not 
    def is_empty(self):
        return self.size == 0 
    
    # to enter item in Queue, it updates size and rear . 
    def enQueue(self,item):
        if self.is_full():
            print("Queue Overflow! Cannot enqueue element.")
            return
        else:
            if self.is_empty():
                self.front = self.rear = 0 
            else :
                self.rear = (self.rear + 1) % (self.capacity)
        self.arr[self.rear] = item 
        self.size += 1
        print(f"{item} enqueue into Queue ")
        
    # to remove item from Queue, it updates size and front 
    def deQueue(self):
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue element.")
            return
        else:
            dequeue_item = self.arr[self.front]
            print(f"{dequeue_item} dequeue from Queue")
            self.front = (self.front + 1) % self.capacity
            self.size -= 1 
            
    
    def front_que(self):
        if self.is_empty():
            print("Queue is Empty")
        
        print(f"Front Item is {self.arr[self.front]}")
        
    def rear_que(self)            :
        if self.is_empty():
            print("Queue is Empty")
        
        print(f"Rear Item is {self.arr[self.rear]}") 
                   
    # def size(self):
    #     if self.is_empty():
    #         return 0
    #     elif self.front <= self.rear:
    #         return self.rear - self.front + 1
    #     else:
    #         return self.capacity - self.front + self.rear + 1       
            
if __name__ == "__main__":
    
    queue = Queue(5)
    queue.enQueue(11)
    queue.enQueue(211)
    queue.enQueue(33)
    
    print(queue.arr) 
    print(" ")
    

    queue.front_que()
    queue.rear_que()
    
    queue.deQueue()
    queue.enQueue(35)
    print(queue.arr) 
    
    
    queue.deQueue()
    queue.deQueue()
    # print(queue.arr) 

    
    