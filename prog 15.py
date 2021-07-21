#write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.import random

import random

#driver code
no = int(input("How much number you need?\n "))
start = int(input("Enter start: ") )
stop = int(input("Enter stop: ") )

lis = [x for x in range(start , stop) if x % 2 != 0]
li = random.sample(lis , no)

#display o/p
print(li)