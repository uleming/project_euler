primes = [2,3]     

def getNext():
        var = primes[len(primes)-1]
        return var + 2


def isPrime(number):
        for x in primes:
                if number%x == 0:
                        return False
        return True


while len(primes) < 101:
        var = getNext()
        if isPrime(var):
                primes.append(var)
                print(primes)


print("\n")
print(primes)
