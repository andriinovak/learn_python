def input_user_answer():
	answers_letters = set(['a', 'b', 'v', 'g', 'd', '1', '2', '3', '4', '5'])
	while True:
		user_answer = input('Enter letter or digit of answer:  ')
		if user_answer in answers_letters:
			print('this is valid answer')
			return user_answer
		else:
			print('this is not valid answer, try again')

letters_to_digit = {'a': 0, 'b': 1, 'v': 2, 'g': 3, 'd': 4, '1': 0, '2': 1, '3': 2, '4': 3, '5': 4}

def verify(question, answer):
	""""""

	choice_index = letters_to_digit[answer]
	
	try:
		return question.choices[choice_index]['is_correct']
	except IndexError:
		return False

def print_user_answer(question, answer, is_answer_correct):
	choice_index = letters_to_digit[answer]
	try:
		print(f'You enter:  {question.choices[choice_index]["content"]}')
	except IndexError:
		pass
	if is_answer_correct:
		print('You are right')
	else:
		print('You are wrong')





