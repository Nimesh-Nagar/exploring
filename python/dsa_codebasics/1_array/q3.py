
max = int(input("Enter Largest number --> "))
odd_numbers = []

for ele in range(1,max):
    if ele%2 != 0:
        odd_numbers.append(ele)

print(odd_numbers)