answer = "2"

def multiply(number):
	result = ""
	add = 0
	for x in number[::-1]:
		var = int(x)*2 + add
		result = result + str(var%10)
		add = int(var/10)
	if add == 1:
                result = result + str(add)
	return result[::-1]


f = open("result.txt",'w')

for x in range(2,1001):
	answer = multiply(answer)
	f.write("number: " + str(x) + "     result: " + answer + "\n")

summ = 0

for x in answer:
	summ = summ + int(x)

f.write("summ:   "+str(summ))
f.close()
	
