#sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers.
# The tuples are input by console. The sort criteria is:
#1: Sort based on name;
#2: Then sort based on age;
#3: Then sort by score.
#The priority is that name > age > score.

import sys

#driver code
print("Enter data in format as follow\n name,age,height")
data = sys.stdin.readlines()
new_list = []

#convert lines into list
for sin_data in data:
	temp = sin_data.split(",")
	temp[1] = int(temp[1])
	temp[2] = int(temp[2])
	temp_tpl = tuple(temp)
	new_list.append(temp_tpl)

#sort list of tuple
new_list.sort()

#display o/p
print(new_list)
