result = 0
for x in range(1,1001):
	var = 1
	for y in range(0,x):
		var = var * x
		var = int(str(var)[-10:]) 
	result =  result + var
	
print(str(result)[-10:])
	