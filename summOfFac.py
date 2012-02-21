def fac(n):
	if n == 1 or n == 0:
		return 1
	else:
		return n*fac(n-1)

num = fac(100)
print(num)
summ = 0
for x in str(num):
	summ = summ + int(x)
print(summ)