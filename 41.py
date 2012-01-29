import math

primes = [2,3]
maxPan = 2

def isPrime(var):
	last = int(math.sqrt(x))
	for z in primes:
		if var%z == 0:
			return False
		if z>=last:
			return True

def isPan(var):
	strVar = str(var)
	for x in range(1,len(strVar)+1):
		if str(x) not in strVar:
			return False
	return True

length = 987654321
for x in range(5,length,2):
	if isPrime(x):
		primes.append(x)
		print(x)
		if isPan(x):
			maxPan = x


print(max)