from random import randint
import json


class Questions:
    def __init__(self, name_of_file):
        with open(name_of_file) as questions_file:
            data = questions_file.read()
            self.list_of_questions = json.loads(data)

    def get_random_question(self):
        random_number = randint(0, len(self.list_of_questions) - 1)
        return Question(self.list_of_questions[random_number])


class Question:
    def __init__(self, one_dict):
        self.id_num = one_dict["id"]
        self.content = one_dict["content"]
        self.choices = one_dict["choices"]

    def choices(self):
        pass

    def display(self):
        print(self.id_num)
        print(self.content)
        for item in self.choices:
            print(item["is_correct"], item["content"])
