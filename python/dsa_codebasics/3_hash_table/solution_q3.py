"""
poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
You have to read this file in python and print every word and its count as show below. 
Think about the best data structure that you can use to solve this problem and 
figure out why you selected that specific data structure.

"""
word_cnt = {}

file = open("poem.txt",'r')
trim = file.read().split() 
print(trim)

for ele in trim:
    if ele in word_cnt:
        word_cnt[ele] += 1
    else:
        word_cnt[ele] = 1
        
print(word_cnt)