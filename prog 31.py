# Pattern
#	             *
#	          *  *
#          *  *  *
#       *  *  *  *
#  *   *   *  *  *

#driver code
n = int(input("Enter no of lines: "))

for i in range(0 , n):

	for s in range(i , n): print(" " , end = "")

	for j in range(0 , i + 1): print("*" , end = "")

	#used print for new line
	print()
