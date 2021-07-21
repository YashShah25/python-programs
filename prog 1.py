#divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included)

#Driver code
start = int( input("Enter start: ") )
stop = int( input("Enter stop: ") )
ans = []

for i in range(start , stop):
	if ( ( (i % 7) == 0) & (i % 5) != 0):
		ans.append(i)

#display o/p
print(ans)
