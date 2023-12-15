# implementation of Hash-Map or Hash-Table using standard operators in python
# https://docs.python.org/3/library/operator.html 
# how hash table works and also dictionary in python


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    #hash function 
    def get_hash(self,key):    
        hash=0
        for char in key:
            hash += ord(char)
        return hash % self.MAX 
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    # delete item function
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None 

ht = HashTable()

#like in dic. we use in these case also. we implementewd dictionary ;) 
ht['march 6'] = 130
ht['march 1'] = 22 
ht['feb 22'] = 29

print(ht.arr)
print(ht['march 1']) 

del ht['march 6']
print(ht.arr)



