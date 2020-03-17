from random import randint
def cold_hot():
	random_number = randint(1, 100)
	for i in range(1, 11):
		user_input = input('enter your number:  ')
		user_input = int(user_input)
		module = random_number - user_input
		module = abs(module)
		if user_input == random_number:
			print('you are right')
			break
		elif module >= 15:
			print('cold')
		elif module > 5 and module < 15:
			print('varm')
		elif module <= 5:
			print('hot')


cold_hot()