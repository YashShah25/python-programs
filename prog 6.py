#accepts a sentence and calculate the number of uppercase letters and lowercase letters.

#driver code
str = input("Enter String..\n")
lo = 0
upp = 0

for temp in str:
	if temp.isupper() : upp += 1

	elif temp.islower() : lo += 1

#display o/p
print("upper case: ",upp)
print("lower case: ",lo)