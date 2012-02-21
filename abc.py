list = []
for b in range(1,999):
    a = (500000-1000*b)/(1000-b)
    if a>0:
        if a-round(a) == 0:
            list.append([a,b])

                
print (list)
