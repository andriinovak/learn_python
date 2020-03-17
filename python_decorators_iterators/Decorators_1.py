import functools
import time


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


class Person:

    def __init__(self, first_name, last_name, age=1):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.domen_email = None
        self.age = self.person_age(age)

    @property
    def full_name(self):
        return self.first_name.title() + ' ' + self.last_name.title()

    @property
    def initials(self):
        return self.first_name[0].upper() + self.last_name[0].upper()

    @property
    def email(self):
        return self.first_name.lower() + '.' + self.last_name.lower() + 'gmail.com'

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first.title()
        self.last_name = last.title()

    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None
        print('Deleted')

    @email.setter
    def email(self, person_email):
        first_last_name, mail = person_email.split('@')
        first, last = first_last_name.split('.')
        self.first_name = first.title()
        self.last_name = last.title()
        self.domen_email = mail

    @staticmethod
    def person_age(age):
        if age < 5:
            print('child')
        else:
            print('etle')
        return age


# an_no = Person('andrii', 'novak')
# print(an_no.full_name)
# print(an_no.email)
# print(an_no.initials)
# an_no.email = 'ira.deptak@mail.ru'
# print(an_no.first_name, an_no.last_name, an_no.domen_email)

person_1 = Person('andrii', 'novak', 28)
print(person_1.age)
Person.person_age(3)
person_1.person_age(45)
print(person_1.age)
