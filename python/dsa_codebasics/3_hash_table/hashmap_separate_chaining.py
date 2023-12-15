# Collision aviodance technique "separate chaining" or "chaining"

class Hashtable:
    def __init__(self):
        self.MAX = 100 
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)

        return hash
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx, ele in enumerate(self.arr[h]):
            if len(ele)==2 and ele[0]==key:
                self.arr[h][idx] = (key,val)
                found = True
                break

        if not found:
            self.arr[h].append((key,val))


t = Hashtable()

t["march 6"] = 120
t["march 6"] = 78
t["march 8"] = 67
t["march 11"] = 20
t["march 15"] = 450

print(t["march 6"])

