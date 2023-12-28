class Hashtable:
    def __init__(self):
        self.MAX = 10 
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        
        if self.arr[h] is None:
            return
        
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

# implementation of Lineaar Probing Technique for collision avoidance 
    # def __setitem__(self, key, val):
    #     h = self.get_hash(key)
        
    #     if self.arr[h] is None:
    #         self.arr[h] = (key,val)
        
    #     else:
    #         new_h = self.find_slot(key, h)
    #         self.arr[new_h] = (key,val)
    #     # print(self.arr)
        
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]
        # return list(range(index, len(self.arr))).extend(range(0, index))
    
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")
    
    def __setitem__(self,key,value):
        
        index = self.get_hash(key)
        
        if index is None:
            self.arr[index] = (key,value)
            
        else:
            while self.arr[index] != None:
                index += 1
                if index >= self.MAX:
                    index = 0 
            self.arr[index] = (key, value)
        
        
    # Deleting element from HashTable
    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
        # print(self.arr)
                
            

if __name__ == "__main__":
    t = Hashtable()
    
    print(t.arr)
    t["march 6"] = 120
    t["march 8"] = 23
    t["march 10"] = 112
    t["march 17"] = 10
    
    t["march 6"] = 180
    t["march 8"] = 122
    t["march 10"] = 32
    t["march 17"] = 10
    t["feb 22"] = 1
    t["feb 25"] = 23
    
    # t["feb 28"] = 56
    print(t.arr)
    
    print(t["march 6"] )
    
    del t["march 10"]
    print(t.arr)

    