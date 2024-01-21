"""
Implementation of Binary Search Tree(BST).
It has specific order. i.e. Left-side of tree contatins elements less than the current elements &
Right-side contains elements greater than the current element.  

[17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
"""


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 
    
    def add_child(self, data):
        #check the val for duplication, BST does not have dupicate data
        if data == self.data:
            return 
        
        if data < self.data:
            #add data in left sub-tree
            if self.left:
                self.left.add_child(data) # recursively call add_child method as data is present. 
            else: 
                self.left = BinarySearchTree(data)   # when no data is present new tree node is created
        
        else:
            # add data in right sub-tree 
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    # IN-Order Traversal Method (Left - Base - Right)
    def in_order_traversal(self):
        elements = []

        # visit Left tree
        if self.left:
            elements += self.left.in_order_traversal() 

        # visit Base node
        elements.append(self.data)

        # visit Right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    

    # Pre-Order Traversal (Base - Left - Right)
    def pre_order_traversal(self):
        elements = []

        # Base 
        elements.append(self.data)

        # Traverse Left
        if self.left:
            elements += self.left.pre_order_traversal()

        # Traverse Right
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements 
    
    # Post-Order Traversal (Left - Right - Base)
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    
    def search(self,val):
        if val == self.data:
            return True 
        
        if val < self.data:
            # val might be in left sub-tree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # val might be in right sub-tree 
            if self.right:
                return self.right.search(val)
            else:
                return False 

    # Find min , max values from Tree         
    def find_min(self):
        if self.left is None:
            return self.data
        
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        
        return self.right.find_max()

    # Deleting Node from Tree 
    def delete_node(self,value):
        if value < self.data:
            if self.left: 
                self.left  = self.left.delete_node(value)

        elif value > self.data:
            if self.right:
                self.right = self.right.delete_node(value)

        else:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            
            if self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val 
            self.right = self.right.delete_node(min_val)
        
        return self


# to create a complete tree from values
def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root    





if __name__ == "__main__":

    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)
    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    num_tree = build_tree(numbers)
    
    print("In-Order : ",num_tree.in_order_traversal()) # [1, 4, 9, 17, 18, 20, 23, 34]
    print(num_tree.search(22))           # True or False 

    print("Pre-Order : ",num_tree.pre_order_traversal())
    print("Post-Order : ", num_tree.post_order_traversal())

    num_tree.delete_node(20)
    print("After Deleting Node 20 : ",num_tree.pre_order_traversal())

    num_tree.delete_node(9)
    print("After Deleting Node 9 : ",num_tree.pre_order_traversal())

