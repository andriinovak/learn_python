dtc = {'eggs' : 10}
print(dtc['eggs'])
print(dtc.get('age', 0))
numbers = []
pos_numbers = [10, 5, 22]
for i in numbers:
	if i > 0:
		pos_numbers.append(i)
print(pos_numbers)

print([i for i in range(5, 15) if i <=10])

def print_name(name):
	return f'hello {name}!'


names = ['andrii', 'sergii', 'oleg', 'stepan', 'vasil', 'ira', 'roman']
def print_hello(names):
	for i in names:
		print(print_name(i))
print_hello(names)

def is_even(num):
 	if num % 2 == 0:
 		res = f'{num}  is even'
 	else:
 		res = f'{num}  is odd'
 	return res 

nums = [1, 2, 3, 4, 5]
for i in nums:
	print(is_even(i))


def lucky(x, y):
	if x > y:
		return 'you lucky'
	else:
		return 'you not lucky'

print(lucky(3, 5))


def cycl(x, y):
	for i in range(x, y + 1):
		if i % 3 == 0:
			print(f' {i} : {i * i}')
		else:
			print(f' {i} not ok')

cycl(6, 18)


def cycl_1(x, y):
	return [f'{i} : {i * i}' if i % 3 == 0 else f'{i} not ok' for i in range(x, y + 1)]
	

print(cycl_1(2, 9))


def lucky(x):
	for i in range(1, x + 1):
		if i > 5:
			print(f'digit {i} > 5')
		else:
			print(f'digit {i} < 5')
lucky(10)

spys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
spys_1 = []
def lucky_1(y):
	for i in y:
		if i > 5:
			spys_1.append(f'digit {i} > 5')
		else:
			spys_1.append(f'digit {i} < 5')
	return print(spys_1)

lucky_1(spys)


def print_name(name='anonim'):
	return f'hello {name}'

print(print_name())


def print_name_and_list(name, *args):
	print(f'hello {name}, and here is a list: {args}')

print_name_and_list('ira', 1, 2, 3)
