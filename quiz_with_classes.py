import json
import random


def read_from_file(name_of_file):
	with open(name_of_file) as questions_file:
		data = questions_file.read()
		list_of_questions = json.loads(data)
		return list_of_questions

questions_list = read_from_file('questions.json')

def get_random_number():
	random_number = random.randint(0, len(questions_list))
	return random_number


#class Questions:
#
#	def __init__(self, data):
#		self.questions_list = data
#
#	def get_random_number(self):
#		random_number = random.randint(0, len(self.questions_list))
#		return random_number
#
#	def get_by_id(self, number):
#		print(self.questions_list[number]['id'])
#		print(self.questions_list[number]['content'])
#		for index in range(0, len(self.questions_list[number]['choices'])):
#			print(self.questions_list[number]['choices'][index]['content'])


class User:

	def __init__(self, name, password, score = 0):
		self.name = name
		self.password = password
		self.score = score

	def count_score(self):
		pass

class OneQuestion:

	def __init__(self, data, number):
		self.questions_list = data
		self.id = number
		self.content = self.questions_list[number]['content']
		self.choices = self.questions_list[number]['choices']
		for index in range(0, len(self.choices)):
			if self.choices[index]['is_correct']:
				self.correct_choice = self.choices[index]



test_user = User('andrii', 1234567890)
test_question = OneQuestion(questions_list, get_random_number())

def run_quiz(question_obj, user_obj):
	pass



