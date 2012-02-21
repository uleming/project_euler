def triangle():
	lst = []
	n = 0
	while True:
		n+=1
		p = n*(n+1)/2
		if p>9999:
			return lst
		if 999<p:
			lst.append(p)
def square():
	return [x*x for x in range(32,100) ]

def pentagonal():
	lst = []
	n = 0
	while True:
		n+=1
		p = n*(3*n-1)/2
		if p>9999:
			return lst
		if 999<p:
			lst.append(p)
def hexagonal():
	lst = []
	n = 0
	while True:
		n+=1
		p = n*(2*n-1)
		if p>9999:
			return lst
		if 999<p:
			lst.append(p)
def heptagonal ():
	lst = []
	n = 0
	while True:
		n+=1
		p = n*(5*n-3)/2
		if p>9999:
			return lst
		if 999<p:
			lst.append(p)
def octagonal():
	lst = []
	n = 0
	while True:
		n+=1
		p = n*(3*n-2)
		if p>9999:
			return lst
		if 999<p:
			lst.append(p)
triangle = triangle()
square = square()
pentagonal = pentagonal()
hexagonal = hexagonal()
heptagonal = heptagonal()
octagonal = octagonal()

numbers = [square,pentagonal,hexagonal,heptagonal,octagonal]
for num in triangle:
	ch = str(num)[-2:]
	clone = numbers[:]
	for z in clone:
		for c in z:
			if str(c)[:2] == ch:
				print num,ch
				ch = c
				clone.remove(z)
				break
	if len(clone) == 0:
		print "hello"
