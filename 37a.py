import math
primes = [2,3,5,7,11]
def isPrime(num):
    lastCheck = math.ceil(math.sqrt(num))
    for x in primes:
        if x > lastCheck:
            return True
        if num%x == 0:
            return False
    return True

def checkPrimes(num):
    for x in primes:
        if x == num:
            return True
    return False





def valid(s):
    for x in range(1,len(s)+1):
#        print(int(s[0:x]),int(s[len(s)-x:len(s)]))
        if not checkPrimes(int(s[0:x])):
            return False
        if not checkPrimes(int(s[len(s)-x:len(s)])):
            return False
    return True


roundPrimes = []
z = 13
while len(roundPrimes) < 100:
    z = z + 2
    if isPrime(z):
        primes.append(z)
    strZ = str(z)
    if strZ[0] != "3" and strZ[0] != "7":
        continue
    if strZ[len(strZ)-1] != "3" and strZ[len(strZ)-1] != "7":
        continue
    if valid(strZ):
        roundPrimes.append(z)
        print(z)
    if z> 1000000:
        break





summ = 0
for a in roundPrimes:
    summ = summ + a

#print("primes",primes)
print("roundPrimes",roundPrimes)
print("summ",summ)

