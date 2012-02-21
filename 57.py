from fractions import Fraction
import sys

sys.setrecursionlimit(2000) 

nums = []

boo = False
def calc(x):
	if x == 1:
		nums.append(Fraction(5,2)-1)
		return Fraction(5,2)
	else:
		val = Fraction(2,1)+Fraction(1,calc(x-1))
		nums.append(val-1)
		return val
		

		

calc(1000)
total = []
for x in nums:
	if len(str(x.numerator)) > len(str(x.denominator)):
		total.append(x)


print(total)
print(len(total))

