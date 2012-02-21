value = [362880,40320,5040,720,120,24,6,2,1]
list = []
var = 1000000
print("var ",var)
for x in value:
	list.append(int(var/x))
	var = var%x


print(list)



z = ['0','1','2','3','4','5','6','7','8','9']
def getNew(list):

	temp = []
	for x in range(0,9):
		var = z[x+list[x]]
		first = z[0:x]
		second = z[x:x+list[x]]
		rest = z[x+list[x]+1:]

		temp = z[0:x]
		temp = temp + [z[x+list[x]]]
		temp = temp + z[x:x+list[x]]
		temp = temp + z[x+list[x]+1:]
		print("list[x]",list[x],"  temp  ",temp)
	return temp
	
z = getNew(list)

p = ""	
for x in z:
	p = p + x

print(p)