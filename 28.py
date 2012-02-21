summ = 1
n0 = 1
for x in range(3,1002,2):
	pointer = x*x
	delta = (pointer -n0)/4
	
	summ = summ + 4*pointer - 6*delta
	n0 = pointer
print(summ)