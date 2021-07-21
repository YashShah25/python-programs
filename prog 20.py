# By using list comprehension,
# print the list after removing numbers which are divisible by 5 and 7 in list.


def ele(x):
	if ((x%5==0)&(x%7==0)):
		return True
	else:
		return False

#driver code
no = int(input("Enter no. of elements: "))
my_list = []

#to get user i/p
for x in range(0 , no): my_list.append(int(input("Enter element") ) )

#collect even elements
temp = filter(ele , my_list)

#to remove even elements
for i in temp:
	my_list.remove(i)

#display o/p
print(my_list)