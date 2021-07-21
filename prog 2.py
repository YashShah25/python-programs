#compute the factorial of a given numbers.

def get_fac(no):
	if no == 0:
		return 1
	elif( no < 0 ):
		return
	else:
		no *= get_fac(no - 1 )
		return no

#driver code
no=int( input("Enter no: ") )

#display o/p
print("Factorial of {} is {}".format( no , get_fac(no) ) )
