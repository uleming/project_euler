max = 0
maxValue = 0


	
	
def getCircle(var):
	print(var)
	s = "0."
	n = 0
	rest = 1
	while True:
		print(s)
		save  = rest
		while rest < var:
			rest = rest * 10
	
		rest = rest%var
		n = n + 1
		if rest == 0:
			break
		if save == rest:
			break
	return n
		
			
	
for x in range(2,10):
	z = getCircle(x)
	if z > max:
		max = z
		maxValue = x
print(maxValue)
	