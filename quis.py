import json
with open('questions.json') as questions_file:
	data = questions_file.read()
	questions = json.loads(data)

from random import randint

def get_random_number():
	random_number = randint(0, len(questions))
	return random_number


def render_question(rand_numb):
	print(questions[rand_numb]['id'])
	print(questions[rand_numb]['content'])
	for index in range(0, len(questions[rand_numb]['choices'])):
		print(questions[rand_numb]['choices'][index]['content'])


def input_answer(random_number):
	while True:
		user_answer = input('enter number of answer:  ')
		if user_answer.isdigit() and questions[random_number]['choices'][int(user_answer) - 1]['is_correct']:
			print('you are right, next question')
			break
		else:
			print('you are wrong, try again')


user_input = ''
while user_input != 'q':
	random_number = get_random_number()
	render_question(random_number)
	try:
		input_answer(random_number)
	except IndexError:
		print('you are wrong, try again ""list index out of range""')
	user_input = input('Press any key to continue, or press "q" to quit:  ')


