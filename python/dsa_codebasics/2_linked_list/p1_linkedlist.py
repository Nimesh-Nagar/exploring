"""
Code Referance : codebasics YouTube Channel 

"""

class Node:

    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next 

#head ----> 
class Linkedlist:

    def __init__(self):
        self.head = None 

    # Inserting Data at BEGINING....
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node    

    # Inserting Data at ...END
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
         

    # Print operation 
    def printList(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ""

        while(itr):
            llstr = llstr + str(itr.data) + "---> "
            itr = itr.next

        print(llstr)

    # Insert list of values 
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    # Find the Length of Linked list   
    def get_length(self):
        count=0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count  
    
    # Removing Data from ANY INDEX 
    def remove_at(self,index):
        if index<0 or index>= self.get_length():
            raise Exception("Invalid Index")
    
        if index==0:
            self.head = self.head.next
            return 
        
        count = 0 
        itr = self.head
        while itr:
            if count == index - 1:  # stop before desired index
                itr.next = itr.next.next
                break 

            itr = itr.next
            count += 1


    # Inserting Data at ANY INDEX
    def insert_at(self, index,data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid INdex")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1: # stop before desired index
                node = Node(data, itr.next) 
                itr.next = node
                break

            itr = itr.next
            count += 1


        

if __name__ == "__main__":
    ll = Linkedlist()

    # ll.insert_at_begining(6)
    # ll.insert_at_begining(88)

    # ll.insert_at_end(21)
    # ll.insert_at_end(4743)
    # ll.insert_at_end(765)

    ll.insert_values(["Banana","Mango","Apple","Grapes","Orange"])
    ll.printList()
    print("Length of Linked List : ",ll.get_length())

    # ll.remove_at(2)
    # # ll.remove_at(-2)  # invalid index
    # ll.printList()

    ll.insert_at(0, "Figs")
    ll.printList()
    ll.insert_at(2, "Strawberry")
    ll.printList()


    

