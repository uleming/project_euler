import math
primes = [2,3,5,7]

def isPrime(num):
        border = math.ceil(math.sqrt(num))
        for x in primes:
                if num == x:
                        return True
                if num%x == 0:
                        return False
                if x > border:
                        return True


def isRoundPrime(num):
	var = 10
	if num%var == 1 or str(num)[0] == "1":
			return False
	while(num%var != num):
		
		if not isPrime(num%var):
			return False
		if not isPrime(math.floor(num/var)):
			return False
		var = var * 10
	return True

z = 7
roundPrimes = []
while z<800000:
	z = z + 2 
	if isPrime(z):
		primes.append(z)
		if isRoundPrime(z):
			roundPrimes.append(z)
	if len(roundPrimes) == 11:
		break
		
print(roundPrimes)
summ = 0
for x in roundPrimes:
        summ = summ+x
print("summ: ",summ)
