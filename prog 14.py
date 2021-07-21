#generate a list with 5 random numbers between 100 and 200 inclusive.

import random

#driver code
no = int(input("How much number you need?\n "))
start = int(input("Enter start: ") )
stop = int(input("Enter stop: ") )

my_list = []
for i in range(0 , no) :
	my_list.append(random.randrange(start , stop))

#display o/p
print(my_list)
