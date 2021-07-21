# By using list comprehension
# generate a 3*5*8 3D array whose each element is 0.

import pprint

def ThreeD(a, b, c):
	lst = [ [ ['0' for col in range(a) ] for col in range(b) ] for row in range(c) ]
	return lst

#driver code
col1 = 5
col2 = 3
row = 2

# used the pretty printed function
pprint.pprint(ThreeD(col1, col2, row))