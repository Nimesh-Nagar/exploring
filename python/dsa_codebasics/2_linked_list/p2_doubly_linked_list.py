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

# Insert at the end of the list 
    def at_end(self,data):
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(data)

        # 3. Make next of new node NULL
        new_node.next = None

        # 4. check if any node is present or not 
        if self.head is None:
            self.head = new_node

        # 5. Traverse to end and add node 
        else:    
            temp = self.head 
            while temp.next != None:
                temp = temp.next

            new_node.prev = temp
            temp.next = new_node
                                    

# Adding Node in Between Two Node (part1) after given node.
    def after_given(self, given_node, data):
        
        # find the given node's data 
        temp = self.head 
        while temp:
            if temp.data == given_node:
                new_node = Node(data)
                new_node.next = temp.next
                new_node.prev = temp
                temp.next = new_node
                if new_node.next is not None:
                    new_node.next.prev = new_node
                break
            else:
                temp = temp.next
        
# Delete Node 
    def del_node(self,del_data):
        itr = self.head 
        while itr:
            if itr.data == del_data:
                if itr.prev == None:            # delete at front 
                    self.head = itr.next 

                elif itr.next != None:          # delete at middle
                    itr.prev.next = itr.next 
                    itr.next.prev = itr.prev 

                elif itr.prev != None:          # dele at end 
                    itr.prev.next = itr.next 
            
            elif itr.next == None and itr.data != del_data:
                print(f"Node with value {del_data} not Found !")

            itr = itr.next
         

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
    print("Adding at front")
    dll.at_front(5)
    dll.at_front(3)
    dll.at_front(2)
    dll.at_front(1)

    dll.print_forward()
    # dll.print_backward()

    # dll.at_end(6)
    # dll.at_end(7)
    # dll.print_forward()    

    print("Adding 22 after 3")
    dll.after_given(3,22) # given data , new node data 
    dll.print_forward()

    print("Deleting Node with data 2 ")
    dll.del_node(2)
    dll.print_forward()   

    print("Deleting Node with data 55 ")
    dll.del_node(55) 
    dll.print_forward()
