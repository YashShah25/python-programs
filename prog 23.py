# By using list comprehension
# print the list after removing the value 24 in "the list is :",

#driver code
no = int(input("Enter no. of elements: "))
my_list = []

#to get user i/p
for x in range(0 , no): my_list.append(int(input("Enter element") ) )
rem = int(input("Which element you want to remove?\n"))

#remove ele.
new_list = [x for (i , x) in enumerate(my_list) if x != rem]
print(new_list)