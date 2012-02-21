import math
primes = [2,3]
def isPrime(num):
	border = math.ceil(math.sqrt(num))
	for x in primes:
		if x == num:
			return True
		if num%x == 0:
			return False
		if x >= border:
			return True

def isValid(num):
	print("num ",num)
	circle = len(str(num))-1
	divisor = pow(10,circle)
	for x in range(0,circle):
		num = 10*(num%divisor) + math.floor(num/divisor)
		#print("var ",var)
		if not isPrime(num):
			return False
	return True


circleNums = []

for z in range(5,10000000,2):
	if isPrime(z):
		primes.append(z)

for p in primes:
	if p<1000000 and isValid(p):
		circleNums.append(p)

#print(primes)
print(circleNums)
print("Numbers of round ",len(circleNums))