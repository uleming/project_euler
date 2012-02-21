set = []
length = 101
for a in range(2,length):
	for b in range(2,length):
		z= a**b
		set.append(z)

set.sort()
length = len(set)
x = 1
while (x<length):
	var = set[x]
	if var == set[x-1]:
		set.remove(var)
	x = x + 1
	length = len(set)

print(len(set))
