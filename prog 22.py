# By using list comprehension
# print the list after removing the 0th,4th,5th numbers from list.

#driver code

indx = []
my_list = []

#to get user i/p
no = int(input("Enter no. of elements: "))
for x in range(0 , no): my_list.append(int(input("Enter element") ) )

#remove element
my_list=[x for (i,x) in enumerate(my_list) if i not in (0,4,5)]

#display o/p
print(my_list)