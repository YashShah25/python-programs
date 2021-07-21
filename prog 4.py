# accepts a sequence of comma-separated numbers from the console
# then generate a list and a tuple which contains every number.

#driver code
numbers = input("Enter numbers..\n")

li_no = numbers.split(",")
tp_no = tuple(li_no)

#display o/p
print(li_no)
print(tp_no)
