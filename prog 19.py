#print the list after removing delete even numbers

def even_no(x):
	if (x % 2) != 0:
		return True
	else:
		return False

#driver code
no = int(input("Enter no. of elements: "))
my_list = []

#to get user i/p
for x in range(0 , no): my_list.append(int(input("Enter element") ) )

#collect even elements
temp = filter(even_no , my_list)

#to remove even elements
for i in temp:
	my_list.remove(i)

#display o/p
print(my_list)