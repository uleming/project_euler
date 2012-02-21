dd = [10,100,1000,10000,100000,1000000,10000000,100000000]
div = [3,4,5,6]
originalNum = 0
for x in dd:
	lastX = round((x*10)/6)
	for y in range(x, lastX):
		originalNum = y
		nums = list(str(2*y))
		nums.sort()
		for z in div:
			var = list(str(z*y))
			var.sort()
			if (var != nums):
				break
			elif (z == 6 ):
				print(originalNum)
				exit()