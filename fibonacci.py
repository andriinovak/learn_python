lis = []
for i in range(1, 101):
	a = i * i
	lis.append(a)
print(lis)
print()
a = 0
b = 1
lis1 = []
for n in range(1, 20):
	c = a + b
	lis1.append(c)
	a = b
	b = c
print(lis1)
print()
car = []
while a != 'q':
	a = input('enter name of car or press q to exit:  ')
	if a == 'q':
		break
	car.append(a)
print(car)
le = len(car)
car1 = []
for i in range(-1, -le-1, -1):
	car1.append(car[i])
print(car1)
print()
questions = [
    "2 + 2 =",
    "5 - 3 =",
    "25 * 2 =",
    "18 / 2 =",
    "44 / 4 =",
    "2 + 3 + 5 =",
    "5 * 5 =",
    "17 - 7 =",
    "15 / 5 =",
    "10 * 10 =",
    "50 / 25 =",
]

answers = [4, 2, 50, 9, 11, 10, 25, 10, 3, 100, 2]
import random
a1 = 0
while a1 != 'q':
	ind = random.randint(1, 11)
	print('Your question:  ', questions[ind])
	a1 = input('Your answer, or press q to exit: ')
	if a1 == 'q':
		break
	elif int(a1) == answers[ind]:
		print('You right')
	else:
		while int(a1) != answers[ind]:
			print('You wrong, try once more. Your question:  ', questions[ind])
			a1 = input('Your answer, or press q to exit: ')
			if a1 == 'q':
				break
			elif int(a1) == answers[ind]:
				print('You right')
