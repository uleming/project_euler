maxNum = int(str(999*999)[0:3])
for x in range(maxNum,100,-1):
	var = int(str(x)+(str(x)[::-1]))
	for y in range(999,100,-1):
		if var%y == 0:
			if len(str(int(var/y))) == 3:
				print("var = ",var, "y = ", y)
				exit()

