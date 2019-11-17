from questions_quiz import Questions
from answers_quiz import UserAnswer

question_list = Questions("questions.json")


def run_quiz():
    quit_code = ''
    while quit_code != 'q':
        one_random_question = question_list.get_random_question()
        one_random_question.display()
        while True:
            answer = UserAnswer(one_random_question)
            if answer.verify(one_random_question):
                break
            else:
                print("You are wrong, try again")

        answer.user_answer_display(one_random_question)
        quit_code = input("Press 'q' to quit or press any key to continue:  ")


if __name__ == "__main__":
    run_quiz()
