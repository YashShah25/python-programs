#print the multiples of 7 between 0 and 100

#Driver code
satrt = int(input("Enter satrt: "))
stop = int(input("Enter stop: "))
ans = []

for i in range(satrt,stop):
	if ( (i % 7) == 0):
		ans.append(i)

#display o/p
print(ans)
