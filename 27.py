nMax = 0
aM = 0
bM = 0
primes = []
primes1000 = []
length = 1000000
z = [True for x in range(length)]
z[0] = False
z[1] = False
current = 5

def clear(var):
	delta = var
	var = var + delta
	while (var < length):
		z[var] = False
		var = var + delta
		
		

def next(var):
	var = var + 2
	while(not z[var]):
		var = var + 2
		if var > length:
			return 1000111
	return var
	

clear(2)
primes.append(2)
clear(3)
primes.append(3)

while (current < length):
	primes.append(current)
	clear(current)
	current = next(current)


n = 0
while (primes[n] < 1000):
	primes1000.append(primes[n])
	n = n + 1
print(primes1000)
for x in (-1,1):
	for b in primes1000:
		b = b*x
		for a in range(-1000,1001):
			n = 0
			while(True):
				var = n*n + a * n + b
				varIsPrime = z[var]
				if not varIsPrime:
					if n > nMax:
						nMax = n
						aM = a
						bM = b
						print(a*b)
					break
				n = n+1


		
		