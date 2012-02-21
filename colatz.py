
def getSeq(var):
	iter = 1
	while var != 1:
		if var%2 == 0:
			var = var/2
			iter = iter + 1
		else:
			var = 3*var + 1
			iter = iter + 1
	return iter

number = 1
max = 0
for x in range(1000000,-1,-1):
	value = getSeq(x)
	if (value >= max):
		max = value
		number = x
		print("number: ", x, "sequence length: ", value)

print("number: " + number)

