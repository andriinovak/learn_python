import random
names = ['oleg', 'roman', 'ira', 'stepan', 'andrii', 'vasyl']
index = 0
while index < len(names):
	print(names[index])
	index = index + 2

number = int(input('enter:  '))
while number != 1:
	print(int(number))
	if number % 2 == 0:
		number /= 2
	else:
		number = number * 3 + 1
print(int(number))

tic = (input('number of ticket:  '))
tic1 = int(tic[0]) + int(tic[1]) + int(tic[2])
tic2 = int(tic[-3]) + int(tic[-2]) + int(tic[-1])
if tic1 == tic2:
	print('happy ticket')
else:
	print('not happy ticket')

tic = (input('number of ticket:  '))
tic1 = 0
tic2 = 0
for i in range(5):
	tic1 = tic1 + int(tic[i]) 
for i in range(-5, 0):
	tic2 = tic2 + int(tic[i])
if tic1 == tic2:
	print('happy ticket')
else:
	print('not happy ticket')

