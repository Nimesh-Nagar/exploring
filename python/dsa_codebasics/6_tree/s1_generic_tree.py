"""
Management hierarchy of a company.
Now extend print_tree function such that it can print either name tree, 
designation tree or name and designation tree.
"""

class TreeNode:
    def __init__(self, name, designation):
        self.name = name 
        self.designation = designation
        self.children = []
        self.parent = None 

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0 
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    

    def print_tree(self,filter):
        space = " " * self.get_level() * 3
        prefix = space + "|---" if self.parent else ""

        if filter == "name":
            print(prefix + self.name)
        elif filter == "designation":
            print(prefix + self.designation)
        else:
            print(prefix + self.name, "=" ,self.designation)

        if self.children:
            for child in self.children:
                child.print_tree(filter)



def build_management_tree():
    root = TreeNode("Nimesh","CEO")

    cto = TreeNode("Chinmay","CTO")
    cto.add_child(TreeNode("Aamir","Application Head"))
    infra = TreeNode("Vishwajeet","Infrastructure Head")
    cto.add_child(infra)

    infra.add_child(TreeNode("Dhaval","Cloud Manager"))
    infra.add_child(TreeNode("Abhijit","App Manager"))

    hr_head = TreeNode("Gels","HR Head")
    hr_head.add_child(TreeNode("Peter","Recruter"))
    hr_head.add_child(TreeNode("Waqas","Policy Manager"))

    root.add_child(cto)
    root.add_child(hr_head)

    # print(hr_head.get_level())

    return root

if __name__ == "__main__":
    root = build_management_tree()
    root.print_tree("name")
    root.print_tree("designation")
    root.print_tree("both")


    