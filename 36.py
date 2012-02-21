def isPalindrom(num):
	binNum = bin(num)[2:]
	middle = int(len(binNum)/2)
	first = binNum[0:middle]
	if len(binNum) % 2 == 0:
		second = binNum[middle:]
	else:
		second = binNum[middle+1:]
#	print(first,second[::-1],num,first == second[::-1])
	if first == second[::-1]:
		return True
	else:
		return False
	
	
	
palindroms = []

for x in range(999,0,-1):
	num = int(str(x)+str(x)[::-1])
	if isPalindrom(num):
		palindroms.append(num)


for x in range(0,10):
	for y in range(0,100):
		num = int(str(y)+str(x)+str(y)[::-1])
		if isPalindrom(num):
			palindroms.append(num)

print(palindroms)
summ = 0
for x in palindroms:
        summ = summ + x
print(summ)
