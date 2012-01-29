
nums = set()


def goodNumber(value):
	digits = set(['1','2','3','4','5','6','7','8','9'])
	for var in digits:
		if var not in value:
			return False
	return True
	
for x in range(1,999):
	#print(x)
	for y in range(x,9999):
		value = x * y
		strValue = str(x)+str(y)+str(value)
		#print(strValue)
		if len(strValue) !=9:
			continue
		
		if goodNumber(strValue):
			#print(str(x)+" x "+str(y)+" = "+str(value))
			nums.add(value)
		
summ = 0
for s in nums:
	summ+=int(s)
print("result is: "+summ)