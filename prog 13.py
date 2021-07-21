# random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.

import random

#driver code
start = int(input("Enter start: ") )
stop = int(input("Enter stop: ") )
my_list = [x for x in range(start , stop) if ( (x % 5 == 0) & (x % 7 == 0) ) ]
op=random.sample(my_list , 1)

#display o/p
print(op)