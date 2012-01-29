import math
def isTriangle(var):
	if math.sqrt(1 + 8 * var) == int(math.sqrt(1 + 8 * var)):
		return True
	else:
		return False


alpabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
f = open('words.txt','r')
a=f.readline()
f.close()
a=a.split(",")
words = []
for x in a:
	words.append(x[1:len(x)-1])
count = 0


for var in words:
	var = str.upper(var)
	wordNum = 0
	for x in var:
		wordNum = wordNum + alpabet.index(x)+1
	if isTriangle(wordNum):
		print(var)
		count += 1
	
	
print(count)