result = []
list = []
def fac(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n* fac(n-1)
		
for x in range(0,10):
	list.append(fac(x))

for x in range(3,9999999):
	var = str(x)
	summ = 0
	for y in var:
		summ = summ + list[int(y)]
	if x == summ:
		result.append(x)
		print(x)
sammary = 0
for z in result:
	sammary  = sammary + z
print(sammary)