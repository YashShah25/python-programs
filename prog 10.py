#divisible by 7 and between a given range 0 and n.

#driver code
no = int(input("n: ") )
ans = []
for i in range(0 , no):
	if ( (i % 7) == 0):
		if( (i % 5) != 0):
			ans.append(i)

#display o/p
print(ans)