
n_2 = 0
n_1 = 1
x = 1
while (len(str(n_1))<1000):
	x = x+1
	res = n_1 + n_2
	n_2 = n_1
	n_1 = res
	print("fib(",x,")",str(n_1))
