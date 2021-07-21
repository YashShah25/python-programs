#shuffle and print the list

import random

#driver code
lis = input("enter elements of list..\n")
suff_list = []
suff_list = lis.split(',')
random.shuffle(suff_list)

#driver code
print(suff_list)