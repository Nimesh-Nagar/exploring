"""
Implement hash table where collisions are handled using linear probing. 
We learnt about linear probing in the video tutorial.
Take the hash table implementation that uses chaining and modify methods to use linear probing. 
Keep MAX size of arr in hashtable as 10.

"""
class HashTable:

    def __init__ (self, size):
        self.MAX = size
        self.arr = [ [] for _ in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    
