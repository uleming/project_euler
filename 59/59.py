#!/usr/bin/env python
def getText():
	'''Read file and make list of encrypted symbols'''
	f = open('cipher1.txt','r')
	text = f.readline()
	f.close()
	text= text.split(',')
	text = map(int,text)
	return text

def getCodes():
	'''Generate list of all combination of codes'''
	from string import ascii_lowercase
	lst = list(ascii_lowercase)
	codes = []
	for x in lst[:]:
		for y in lst[:]:
			for z in lst[:]:
				codes.append([ord(x),ord(y),ord(z)])
	return codes

def decode(code):
	delimiter = 1 + len(text) // 3
	code = delimiter * code
	for i in range(len(text)-1):
		code[i] = code[i] ^ text[i]
	code = code[:len(text)-1]
	return "".join(map(chr,code))

text = getText()
codes = getCodes()
file = open('result.txt','w')
for x in range(len(codes)-1):
	s=decode(codes[x])
	file.write(str(codes[x]))
	file.write(s)
	file.write('\n\n')
	print x
file.close()
