megaX = 1
megaY = 1
result = 1
for x in range(10,100):
	for y in range(x,100):
		firstX = int(str(x)[0])		
		lastY = int(str(y)[1])
		if lastY != 0:
			if x != y:
				if str(x)[1] == str(y)[0]:
					diff = abs(x/y - firstX/lastY)
					if  diff < 0.0001:
						result = result * lastY
						megaX = megaX*x
						megaY = megaY *y
						
print(result)
