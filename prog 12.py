#random even number between 0 and 10 inclusive using random module and list comprehension.

import random

#driver code
start = int(input("Enter start: ") )
stop = int(input("Enter stop: ") )
my_list = [x for x in range(start , stop) if x % 2 == 0]

#display o/p
print(random.sample(my_list , 1) )