min = 1000000000
for k in range(100,-1,-1):
	for j in range(100,-1,-1):
		delta = abs(3*k*k+j-3*j*j+k)
		if delta < min:
			min = delta
			print(k,j,delta)
		