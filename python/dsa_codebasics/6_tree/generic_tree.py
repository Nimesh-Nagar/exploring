"""
Tree data structure: https://www.geeksforgeeks.org/tree-data-structure/ 

codebasics
https://www.youtube.com/watch?v=4r_XR9fUPhQ&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=9
"""

#
class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.children = []
        self.parent = None 
        
    def add_child(self, child):
        child.parent = self         # child is instance of treenode class it will have parent property 
        self.children.append(child)
        
    def get_level(self):
        level = 0 
        p = self.parent
        while p:
            level += 1
            p = p.parent
            
        return level 
    
        
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3 
        prefix = spaces + "|---" if self.parent else ""
        print(prefix + self.data)
        
        if len(self.children) > 0:   
            for child in self.children:
                child.print_tree()
        
        
def build_product_tree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("MacBook"))
    laptop.add_child(TreeNode("Asus"))
    laptop.add_child(TreeNode("Thinkpad"))
    
    cellphone  = TreeNode("CellPhone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Pixel"))
    cellphone.add_child(TreeNode("vivo"))
    
    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root
    
if __name__ == "__main__":
    root = build_product_tree()
    # print(root.get_level())
    root.print_tree()
    pass 


    