""" Doubly Linked List Code """

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next 
        self.prev = prev

class DoublyLL:
    def __init__(self):
        self.head = None


# Adding a node at the front of the list

    def at_front(self,data):
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(data)

        # 3. Make next of new_node as head and previous as NULL
        new_node.next = self.head
        new_node.prev = None 

        # 4. change prev of head node to new node
        if self.head is not None:
            self.head.prev = new_node
        
        # 5. move the head to point to the new node
        self.head = new_node


# This function prints the contents of
# the linked list starting from the head

# Printing Doubly linked data in forward direction 
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        current = self.head 
        print("", end=" ---> ")
        while current:
            print(current.data, end=" ---> ")
            current = current.next 
        print("\n")

# Printing Doubly linked data in Reverse direction 
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        temp = self.head
        print("", end=" ---> ")
        while temp:
            rev=temp           # copy addr, of temp_head to rev_head 
            temp = temp.next   # copy next addr. till addr become null

        while rev != self.head.prev:
            print(rev.data, end=" ---> ")
            rev = rev.prev
        print("\n")



if __name__ == "__main__":
    
    dll = DoublyLL()
    dll.at_front(4)
    dll.at_front(3)
    dll.at_front(2)
    dll.at_front(1)

    dll.print_forward()
    dll.print_backward()