a = 'The quick Brow Fox'
def count_case(x):
	up = 0
	low = 0
	for i in x:
		if i.isupper() == True:
			up = up + 1
		elif i == ' ':
			continue
		else:
			low = low + 1
	return f'upper case:  {up}, lower case:  {low}'
print(count_case(a))


a = [1, 2, 3, 3, 3, 3, 4, 5]
b = []
def set_digits(x):
	return list(set(x))
print(set_digits(a))


def set_digits_1(x):
	for i in x:
		if i not in b:
			b.append(i)
	return b
print(set_digits_1(a))


c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = []
def is_even(x):
	for i in c:
		if i % 2 == 0:
			d.append(i)
	return d
print(is_even(c))


string = 'The quick brown fox jumps over the lazy dog'
def panogram(x):
	alfav = 'qwertyuiopasdfghjklzxcvbnm'
	for i in x:
		if i not in alfav:
			return 'not pangram'
	return 'is pangram'

print(panogram(string))


def atlas():
	slovnyk = {}
	slovnyk['name'] = input('enter country:  ')
	slovnyk['capital'] = input('enter capital of the country:  ')
	print(slovnyk)

atlas()


