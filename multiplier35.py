#!/usr/bin/env python
#-*- coding:utf-8 -*-


summ = 0
sequence = [3,3,2,1,3,1,2] 
all_numbers = [3,5,6,9,10,12]

def getNext():
	for x in sequence:
		if (all_numbers[len(all_numbers)-1] < 999):
			all_numbers.append(all_numbers[len(all_numbers)-1] + x)
		else:
			return
	getNext()	
		
getNext()

summ = 0
for x in all_numbers:
	summ += x
print summ
