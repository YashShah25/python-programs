#computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

#driver code
value = int( input("Enter value: ") )

ans = lambda a : a + (a * 10 + a) + (a * 100 + a * 10 + a) + (a * 1000 + a * 100 + a * 10 + a)

#display o/p
print(ans(value))