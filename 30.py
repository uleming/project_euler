nums = []
for x in range(2,500000):
	y = str(x)
	summ = 0
	for z in y:
		summ = summ + int(z)**5
	if summ == x:
		nums.append(x)
		print(x)
result = 0
for x in nums:
	result = result + x
print(result)