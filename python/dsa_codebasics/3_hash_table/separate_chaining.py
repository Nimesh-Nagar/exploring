class Hashtable:
    def __init__(self):
        self.MAX = 10 
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self,key):
        index = self.get_hash(key)
        
        for ele in self.arr[index]:
            if ele[0] == key:
                return ele[1]

    def __setitem__(self,key,val):
        h = self.get_hash(key)

        found = False
        for idx, ele in enumerate(self.arr):
            if len(ele)==2 and ele[0]==key:
                self.arr[h][idx] = (key,val)
                found = True
                break

        if not found:
            self.arr[h].append((key,val))


    def __delitem__(self, key):
        index = self.get_hash(key)
        for idx, ele in enumerate(self.arr):
            if ele[0] == key:
                del self.arr[index]

t = Hashtable() 

t["march 6"] = 120
t["march 8"] = 23
t["march 10"] = 112
t["march 17"] = 10
t["march 6"] = 9

print(t.arr)
print(t["march 17"])
print(t["march 6"])

del t["march 10"]
print(t.arr)