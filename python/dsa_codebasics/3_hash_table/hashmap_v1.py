# implementation of Hash-Map or Hash-Table in python

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    #hash function 
    def get_hash(self,key):    
        hash=0
        for char in key:
            hash += ord(char)
        return hash % self.MAX 
    
    # add key value pair in hashmap 
    def add(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    # get value form key 
    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    

ht = HashTable()
print(ht.get_hash('march 6')) # generates hash val. for given key 
ht.add('march 6', 130)
# print(ht.arr)
print(ht.get('march 6')) # get the value at given key

