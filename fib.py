list = [0,1,1]
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        
        return fib(n - 1) + fib(n-2)
    

summ = 0
for x in range (1,5000):
    var = fib(x)
    if var > 4000000:
        break
    if var%2 == 0:
        summ = summ + var
        print(summ)
print(summ)
