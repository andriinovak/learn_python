from random import randint
import random


slovnyk = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

def print_set_values(data):
	values_list = []
	for i in range(0, len(slovnyk)):
		for item in slovnyk[i].values():
			values_list.append(item)
	values_set = []
	for item in values_list:
		if item not in values_set:
			values_set.append(item)
	print(values_set)


print_set_values(slovnyk)


string = 'beetrootacademy'

def function_noname(data):
	letters = []
	for i in data:
		if i not in letters:
			letters.append(i)
	letters.sort()
	slovnyk_set = {}
	for i in letters:
		slovnyk_set[i] = string.count(i)
	print(slovnyk_set)


function_noname(string)


def counter(a, b):
	ax = []
	bx = []
	if type(a) is int and a > 0:
		a = str(a)
		for i in a:
			if i not in ax:
				ax.append(i)
	if type(b) is int and b > 0:
		b = str(b)
		for i in b:
			if i not in bx:
				bx.append(i)
	count = 0
	for item in bx:
		if item in ax:
			count = count + 1
	print(count)


counter(1233211, 12128)


a = [1, 2, 3, 4, 5]

def peremish(data):
	random.shuffle(data)
	print(data)

peremish(a)



a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
def list_1_list_2(list1, list2):
	for item in list1:
		if item in list2:
			x = True
			break
		else:
			x = False
	return(x)


print(list_1_list_2(a, b))


list_digits = [86,86,85,85,85,83,23,45,84,1,2,0]

def list_max_value(data):
	data = list(set(data))
	max_value_1 = max(data)
	data.remove(max(data))
	max_value_2 = max(data)
	print(max_value_1, max_value_2)

list_max_value(list_digits)


students = {'student1': 10, 'student2': 20, 'student3': 30}

def best_students(data):
	best_scores = []
	for item in data.values():
			best_scores.append(item)
	max_score_1 = max(best_scores)
	best_scores.remove(max(best_scores))
	max_score_2 = max(best_scores)
	print(max_score_1, max_score_2)

best_students(students)


products_with_price = {
		'SMART WATCH': 550,
		'PHONE' : 1000,
		'PLAYSTATION': 500,
		'LAPTOP' : 1550,
		'MUSIC PLAYER' : 600,
		'TABLE' : 400
		}

def products_price(data):
	user_input_price = input('input your price:   ')
	user_input_price = int(user_input_price)
	list_of_prices = []
	products_list = []
	for item in data.keys():
		if data[item] <= user_input_price:
			products_list.append(item)
	print(products_list)


products_price(products_with_price)


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