#Pattern
#       * * * * * *
#		 * * * * *
#		  * * * *
#		   * * *
#		    * *
#		     *

#user input
n = int(input("Enter no of lines: "))

#main loop
for i in range(0 , n):

	#sab loop for space
	for s in range(0 , i + 1):
		print(" " , end = "")

	#sab loop for *
	for j in range(i , n): print("* " , end = "")

	#used print for new line
	print()
