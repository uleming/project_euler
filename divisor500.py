def divisors(x):
	tuple={}
	y =3
	tuple[2] = 0
	while x%2 !=1:
		x= x/2
		tuple[2] = tuple[2] + 1
	
	tuple[y] = 0
	while x!=1:
		if x%y == 0:
			tuple[y] = tuple[y] + 1
			x = x/y
			continue
		y = y+2
		tuple[y] = 0
	return tuple

def numDiv(t):
        result = 1
        for x in t.keys():
                result = result * (t[x]+1)
        return result

x = 2
current = 1
divNum = 0
while True:
        current = current + x
        x = x + 1
        divNum = numDiv(divisors(current))
        if divNum>500:
                  break
        if divNum>200:
                print(current,"   ",divNum)
print("current: ",current, "divNum: ", divNum)
	
