import math
a = 265
while True:
	a = a + 1
	c = math.sqrt(4 + 16*a*(a+1))
	b = math.sqrt(1 + 12*a*(a+1))
	if (float.is_integer(c) and float.is_integer(b)):
		c = (c+2)/8
		b = (1+b)/6
		if (float.is_integer(c) and float.is_integer(b)):
			print(a,b,c)