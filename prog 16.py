# randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

import random

#driver code
no = int(input("How much number you need?\n "))
start = int(input("Enter start: ") )
stop = int(input("Enter stop: ") )

base_list = [x for x in range(start , stop) if ( (x % 5 == 0) & (x % 7 == 0) ) ]
my_list = random.sample(base_list , no)

#display o/p
print(my_list)