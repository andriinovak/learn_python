questions = [
    {
        "content": "2 + 2 - 4 = ",
        "choices": [
            {"content": "0", "is_correct": True},
            {"content": "24", "is_correct": False},
        ],
    },
    {
        "content": "18 / 2 = ",
        "choices": [
            {"content": "5", "is_correct": False},
            {"content": "9", "is_correct": True},
        ],
    },
]

from random import randint
def print_question():
	quest = randint(0, 1)
	print('your question:  ', questions[quest]['content'])

print_question()

def enter_answer():
	answer = input('enter your answer:  ')
	