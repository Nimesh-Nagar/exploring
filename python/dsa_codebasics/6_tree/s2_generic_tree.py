"""
modify print_tree method to take tree level as input. And that should print tree only upto that level.

"""

class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.children = []
        self.parent = None 
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
            
        return level
            
            
    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|---" if self.parent else "" 
            
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    
    def print_tree_lev(self,level):
        if self.get_level() > level:
            return
        
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|---" if self.parent else "" 
        print(prefix + self.data)
        
        if self.children:
            for child in self.children:
                child.print_tree_lev(level)
            
        
def build_location_tree():
    root = TreeNode("Global")
    
    india = TreeNode("India")
    
    guj = TreeNode("Gujarat")
    guj.add_child(TreeNode("Ahmedabad"))
    guj.add_child(TreeNode("Baroda"))
    india.add_child(guj)
    
    ka = TreeNode("Karnataka")
    ka.add_child(TreeNode("Bangeluru"))
    ka.add_child(TreeNode("Mysoor"))
    india.add_child(ka)
    
    usa = TreeNode("USA")
    
    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))
    usa.add_child(nj)
    
    cal = TreeNode("California")
    cal.add_child(TreeNode("San Francisco"))
    cal.add_child(TreeNode("Mountain View"))
    cal.add_child(TreeNode("Palo Alto"))
    usa.add_child(cal)
    
    
    root.add_child(india)
    root.add_child(usa)
    
    return root
    
    

if __name__ == "__main__":
    root = build_location_tree()
    root.print_tree()
    root.print_tree_lev(2)
    