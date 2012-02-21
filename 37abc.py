length = 100

def clear(primesB, x):
        delta = x 
        x = x + delta
        while (x < length):
                primesB[x] = False
                x = x + delta
    
def next(primesB,x):
        x = x +2
        while (x < length and not primesB[x]):
                x = x +2
        return x
                
                

def getPrimesLessMillion():
        primes = []
        primesB = [True for x in range(0,length)]
        primes.append(2)
        clear(primesB,2)
        z = 3
        while(z < length):
                primes.append(z)
                clear(primesB,z)
                z = next(primesB,z)
        return primes
        
def left(x,primes):
        subList = primes[0:x+1]
        number = str(subList[x])
        for x in range(0:len(number)):
                

def right(x,primes):

def getRoundPrimes();
        primes = getPrimesLessMillion()
        primes = primes[4:]
        roundPrimes = []
        
        for x in range(0:len(primes)):
                if left(x,primes) and right(x,primes):
                        roundPrimes.append(prime[x])
                        if len(roundPrimes) == 11:
                                return roundPrimes

roundPrimes = getRoundPrimes();
print(roundPrimes)
summ = 0
for x in roundPrimes:
        summ = summ + x
print(summ)