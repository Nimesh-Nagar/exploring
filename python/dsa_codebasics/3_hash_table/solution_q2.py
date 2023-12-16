"""
nyc_weather.csv contains new york city weather for first few days in the month of January. 
Write a program that can answer following,
  (a) What was the temperature on Jan 9?
  (b) What was the temperature on Jan 4?
Figure out data structure that is best for this problem

"""

dict = {}

file = open('nyc_weather.csv','r')

for line in file:
    trim = line.split(',')
    day = trim[0]
    try:
        temp = int(trim[1])
        dict[day] = temp
    except:  
        print("Invalid Temperatue ignore the ROW")
        
print(dict)      
print(dict['Jan 9'])
print(dict['Jan 4'])
