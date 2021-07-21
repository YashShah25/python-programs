#generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included)

#driver code
stop = int( input("Enter stop: ") )
ans = {}

for i in range( 1 , stop + 1 ):
	ans[i] = i * i

#display o/p
print(ans)