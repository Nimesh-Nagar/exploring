"""
nyc_weather.csv contains new york city weather for first few days in the month of January. 
Write a program that can answer following,
    - What was the average temperature in first week of Jan
    - What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem

"""

arr=[]
file = open('nyc_weather.csv','r')

# trim = file.read().split("\n")
# for elements in range(1,len(trim)):
#     print(trim[elements])

for line in file:
    trim = line.split(",")
    try:
        temperature = int(trim[1])
        arr.append(temperature)
    except:
        print("invalid temp ignore ROW")
        
print("average temperature : ",sum(arr[0:7])/len(arr[0:7]))

print("maximum temperature : ",max(arr[:]))

