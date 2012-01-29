import math

primes = [2,3]
def fillprimes():
	for x in range(5,1000000):
		last = int(math.sqrt(x))
		for y in primes:
			if x%y == 0:
				break
			elif y> last:
				primes.append(x)
				break

def divisors(var):
	print(var)
	divNums = set()
	rest = var
	x = 0
	while rest != 1:
		div = primes[x]
		if rest % div == 0:
			rest = rest/div
			divNums.add(div)
		else:
			x += 1
	return len(divNums)
	

fillprimes()

x = 2
while True:
	x += 1
	if divisors(x) == 4 and divisors(x+1) == 4 and divisors(x+2) == 4 and divisors(x+3) == 4:
		print(x)
		break
	
	
	
	