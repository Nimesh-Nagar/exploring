"""
Referance           : codebasics YouTube Channel 
code and exercise   : https://github.com/codebasics/data-structures-algorithms-python/tree/master/data_structures/3_LinkedList
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

    # Search by value and insert data after 
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head is None:
            return
        
        #  to save space of temp_head 
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        
        temp = self.head 
        while temp:
            if temp.data == data_after:
                new_node = Node(data_to_insert,temp.next)
                temp.next = new_node
                break

            temp = temp.next

    # Delete data by value
    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:     # iter. using addr.
            if current.next.data == data:
                current.next = current.next.next
                break 

            current = current.next
        

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

if __name__ == "__main__":
   
    # ''' 
    ll = Linkedlist()

    ll.insert_at_begining(6)
    ll.insert_at_begining(88)

    ll.insert_at_end(21)
    ll.insert_at_end(4743)
    ll.insert_at_end(765)

    # ll.insert_values(["Banana","Mango","Apple","Grapes","Orange"])
    # print("Orginal Linked List ")
    # ll.printList()
    # print("Length of Linked List : ",ll.get_length())

    # ll.remove_at(2)
    # # ll.remove_at(-2)  # invalid index
    # ll.printList()

    # print("\nInsert 'Figs' at position 1 ")
    # ll.insert_at(1, "Figs")
    # ll.printList()
    # print("\nInsert 'Strawberry' at position 2 ")
    # ll.insert_at(2, "Strawberry")
    # ll.printList()
    # print("Add 'kiwi' after 'mango' ")
    # ll.insert_after_value("Mango","kiwi")
    # ll.printList()

    # print("Delete 'kiwi' from list ")
    # ll.remove_by_value("kiwi")
    ll.printList()

    '''
    # Exersise Solutions 
    ll = Linkedlist()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.printList()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.printList()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.printList()
    ll.remove_by_value("figs")
    ll.printList()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.printList()

    ''' 
