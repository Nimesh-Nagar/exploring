expenses = [2200,2350,2600,2130,2190]

a = expenses[1]-expenses[0]
print(a)

sum=0
for exp in range(3):
    sum=sum+expenses[exp]
print(sum)    

print(2000 in expenses)

expenses.append(1980)
print(expenses)        

expenses[3] = expenses[3]-200 
print(expenses)

