# Use a list comprehension to square each odd number in a list.

#driver code
list_numb = input("Enter list..\n")
temp = list_numb.split(",")
new_list = [x for x in temp if int(x) % 2 != 0]

#display o/p
print(new_list)