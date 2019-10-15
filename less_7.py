import random      #use list!!!!
a = random.randint(1, 10)
c = random.randint(1, 10)
d = random.randint(1, 10)
print(a, c, d)
b = input('vvedit chyslo:  ')
b = int(b)
if a == b or c == b or d == b:
	print('happy number')
else:
	print('is not happy number')

names = ['oleg', 'roman', 'ira', 'stepan', 'andrii']
print(names)
for item in names:
	print(f'hello {item}')
print()
room = 'beetroot'
for name in names:
	if name == 'oleg' or name == 'roman':
		print(f'hello {name}! i in {room}')

for index, name in enumerate(names):
	if index == 2 or index == 3:
		continue
		print(name)


x = int(input('enter number:  '))
a = 1
for ind in range(2, x + 1):
	a = a + ind
print(a)

