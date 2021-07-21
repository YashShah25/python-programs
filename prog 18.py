#sentences where
# subject is in ["I", "You"]
# verb is in ["Play", "Love"]
# the object is in ["Hockey","Football"].

#driver code
subjects = input("Enter subjects\n")
verbs = input("Enter verbs\n")
objects = input("Enter objects\n")

sub = subjects.split(",")
ver = verbs.split(",")
obj = objects.split(",")

#display o/p
for x in sub:
    for y in ver:
        for z in obj:
            print("{} {} {}".format(x , y , z) )