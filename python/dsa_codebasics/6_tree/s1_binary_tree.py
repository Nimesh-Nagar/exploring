"""
[17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
"""

class BinaryTree:
    def __init__(self,data:int):
        self.data = data
        self.left = None
        self.right = None 

    def add_child(self,val):
        if val == self.data:
            return 

        # add child to left 
        if val < self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BinaryTree(val)

        # add child to right
        else:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BinaryTree(val) 

    # IN-Order Traversal (Left - Base - Right)
    def in_order_traversal(self):
        elements = []

        # traverse left
        if self.left:
            elements += self.left.in_order_traversal() 
        
        # Base data store 
        elements.append(self.data)

        # traverse right 
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



def build_tree(elements):
    root = BinaryTree(elements[0])

    for ele in range(1, len(elements)):
        root.add_child(elements[ele])
        
    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    num_tree = build_tree(numbers)  
    
    print("In-Order Traversal : ", num_tree.in_order_traversal())
    print("Pre-Order Traversal : ", num_tree.pre_order_traversal())  
    print("Post-Order Traversal : ", num_tree.pre_order_traversal())  

