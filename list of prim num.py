def prim(no):
    for i in range(2,no):
        if no%i==0:
            return False
    else:
        return True

num = int(input("Enter num:"))
prim_lst = filter(prim, range(0,num))

print("list of prim numbers is\n")
for temp in prim_lst:print(temp)