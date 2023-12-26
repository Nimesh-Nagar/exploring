class Hashtable:
    def __init__(self):
        self.MAX = 10 
        self.arr = [[None] for _ in range(self.MAX)]

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
            
    # implementation of Lineaar Probing Technique for collision avoidance 
    def __setitem__(self,key,val):
        h = self.get_hash(key)

        for idx, ele in enumerate(self.arr[h]):
            if len(ele) == 2 and ele[0] == key:
                # self.arr[h][idx] = (key, val)
                return

        # Linear probing
        index = (h + 1) % self.MAX
        while index != h:
            if not self.arr[index]:
                self.arr[index].append((key, val))
                return
            index = (index + 1) % self.MAX

        # If no empty slot is found, raise an error or resize the hashtable
        raise ValueError("Hashtable is full, unable to insert new key-value pair.")
            
        
            

if __name__ == "__main__":
    t = Hashtable()
    
    t["march 6"] = 120
    t["march 8"] = 23
    t["march 10"] = 112
    t["march 17"] = 10

    print(t.arr)