#Problem N6

#Description:
#    get difference between (1^2 + 2^2 + 3^2 + ... + 100^2) and (1 + 2 +3 + ... +100)^2

summ = 0
x = 1
y = x + 1
print(x,y)
for x in range(x,101):
    for y in range(x+1,101):
        summ += x*y
summ_total = summ * 2
print (x,y)
print summ_total

