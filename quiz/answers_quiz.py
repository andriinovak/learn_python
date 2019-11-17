letters_to_digit_5v = {
    "a": 0,
    "b": 1,
    "v": 2,
    "g": 3,
    "d": 4,
    "1": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
}

letters_to_digit_4v = {
    "a": 0,
    "b": 1,
    "v": 2,
    "g": 3,
    "1": 0,
    "2": 1,
    "3": 2,
    "4": 3,
}


class UserAnswer:
    def __init__(self, one_question):
        posibil_answers_5v = ["a", "b", "v", "g", "d", "1", "2", "3", "4", "5"]
        posibil_answers_4v = ["a", "b", "v", "g", "1", "2", "3", "4"]
        while True:
            self.user_answer = input("Enter letter or digit of answer:  ")
            if self.user_answer.isalpha():
                self.user_answer = self.user_answer.lower()
            if (
                len(one_question.choices) == 5
                and self.user_answer in posibil_answers_5v
            ):
                print("This is valid answer")
                self.user_answer = letters_to_digit_5v[self.user_answer]
                break
            elif (
                len(one_question.choices) == 4
                and self.user_answer in posibil_answers_4v
            ):
                print("This is valid answer")
                self.user_answer = letters_to_digit_4v[self.user_answer]
                break
            else:
                print("This is not valid answer, try again")

    def verify(self, one_question):
        if one_question.choices[self.user_answer]["is_correct"]:
            return True
        else:
            return False

    def user_answer_display(self, one_question):
        print(
            f"Your choice is {one_question.choices[self.user_answer]['content']}, and this is correct"
        )
