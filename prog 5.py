#accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

import sys

#driver code
print("write some thing..\n")
str_lines = sys.stdin.readlines()

#display o/p
for lin in str_lines : print( lin.upper() )