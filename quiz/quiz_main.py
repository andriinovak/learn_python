from questions_quiz import Questions
from answers_quiz import input_user_answer, verify, print_user_answer

question_list = Questions('questions.json')

def run_quiz():
	one_random_question = question_list.get_random_question()	
	one_random_question.display()
	answer = input_user_answer()
	print(answer)
	is_correct = verify(one_random_question, answer)
	print(is_correct)
	print_user_answer(one_random_question, answer, is_correct)


if __name__ == '__main__':
	run_quiz()

