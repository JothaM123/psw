#!/usr/bin/python3
import re

print("Psw v1.0\n")

while 1:
	psw = input("Psw$ ")

	if len(psw) >= 8 and re.match("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]+$", psw):
		print("{} is ✅".format(psw))

	else:
		print("{} is ❌".format(psw))

	print("\n")
