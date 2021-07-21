# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
# make a list whose elements are intersection of the above given lists.

#driver code

#to get user i/p
n1 = int(input("Enter no. of elements in list 1: "))
list1 = []
for x in range(0 , n1): list1.append(int(input("Enter element") ) )
n2 = int(input("Enter no. of elements in list 1: "))
list2 = []
for x in range(0 , n2): list2.append(int(input("Enter element") ) )

new_list = [x for x in list1 if x in list2]

#display o/p
print(new_list)