# accepts a string from the console and prints it in reverse order.

#driver code
str = input("Enter string")

#display o/p
for i in range(len(str) - 1, - 1, - 1):
	print(str[i] , end = "")