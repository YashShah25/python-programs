# print this list after removing all duplicate values with original order reserved.

#driver code
my_list = []

#to get user i/p
no = int(input("Enter no. of elements: "))
for x in range(0 , no): my_list.append(int(input("Enter element") ) )

temp_list = []
for i in my_list:
	if i not in temp_list:
		temp_list.append(i)

my_list.clear()

for j in range(len(temp_list) - 1, - 1, - 1):
	my_list.append(temp_list[j])

#display o/p
print(my_list)
