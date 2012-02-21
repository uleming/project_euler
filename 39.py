
list = []
top = 0
for p in range(0,1001):
        n = 0
        import math 
        criticalRange = math.ceil(p/3)
        for a in range(1,criticalRange):
                for b in range(a,p):
                        c = p - a - b
                        if c < b :
                                break
                        else:
                                value = math.sqrt(a*a + b*b)
                                #print(value)
                                if (value == c):
                                        n = n + 1
        if n > top:
                top = n
                list.append(p)

print(list[len(list)-1])  