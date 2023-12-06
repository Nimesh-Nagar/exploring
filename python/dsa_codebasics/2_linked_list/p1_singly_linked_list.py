# Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next 

# Head node 
class LinkedList:
    def __init__(self):
        self.head = None 


# """Insert Data at Begining""" 
    def insert_at_begining(self,data):

        # 1. create new node and put data  
        new_node = Node(data)

        # 2. head value to new_node to link with first node 
        new_node.next = self.head

        # 3. make head point new_node
        self.head = new_node

# """ Insert at the END """
    def insert_at_end(self,data):
        #1. create new node 
        new_node = Node(data)

        #2. if ll empty make new_node head
        if self.head is None:
            self.head = new_node
            return

        #3. travers till last node
        current = self.head
        while current.next:
            current = current.next

        #4. link last node next to new_node
        current.next = new_node

# Find Length of Linked List 
    def get_length(self):
        count = 0
        current = self.head 

        while current:
            count += 1 
            current = current.next
        return count


# """ Insert at any Position """
    def insert_after(self, index, data):
        if index < 0 and index > self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_begining(data)
        
        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                new_node = Node(data,temp.next)  #1. new node |data |take from temp |
                temp.next = new_node             #2. temp node | | take new_node |
                break 

            temp = temp.next
            count += 1

# """ Delete from any Index """ 
    def remove_at(self, index):
        if index < 0  and index > self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0 
        current = self.head
        while current:
            if count == index - 1: 
                current.next = current.next.next
                break 

            current = current.next 
            count +=1 



# This function prints the contents of
# the linked list starting from the head

    def printList(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        current = self.head 
        while current:
            print(current.data, end=" ---> ")
            current = current.next 
        print("NULL")



if __name__ == "__main__":

    ll = LinkedList()
    # ll.printList()
    ll.insert_at_begining(4)
    ll.insert_at_begining(11)
    ll.insert_at_begining(3)
    print("Orginal Linked List : ")
    ll.printList()

    print("\nInsert at end 69 and 'hello' : ")
    ll.insert_at_end(69)
    ll.insert_at_end("hello")
    ll.printList()

    print("\n Insert 35 after position 3")
    ll.insert_after(3,35) # postion, data
    ll.printList()

    print("\n Delete 2nd index linked list")
    ll.remove_at(2)
    ll.printList()

    