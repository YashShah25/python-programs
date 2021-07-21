#computes the net amount of a bank account based a transaction log from console input.

import sys

#driver code
print("format should be like..\n D 300\n W 200")
tran_log = sys.stdin.readlines()
tot_d = 0
tot_w = 0


for log in tran_log:

	if log[0] == "D":
		temp = log.split(" ")
		tot_d += int(temp[1])

	elif log[0] == "W":
		temp = log.split(" ")
		tot_w += int(temp[1])

#display o/p
print("balance is: ",tot_d - tot_w)
