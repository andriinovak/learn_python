def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_whee():
    print("Whee!")


# say_whee_dec = my_decorator(say_whee)
# say_whee()
# say_whee_dec()


# def is_correct(value):
#    return value == 2


def assign_if_valid(func):
    def wrapper(value):
        if value not in [1, 2, 3, 4, 5]:
            print('not valid')
            return
        print('checking....')
        return print(func(value))
    return wrapper


# is_correct_dec = assign_if_valid(is_correct)
# is_correct_dec(1)


# @assign_if_valid
# def is_correct(value):
#     return value == 4


# is_correct(4)


@assign_if_valid
def i_print_num(num):
    return f'i print num:  {num}'


# i_print_num(3)


def save_stats(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}  save  {result}')
        return result
    return wrapper


# @assign_if_valid
@save_stats
def is_correct(value, question):
    if question == 'any':
        return True
    return value == 2


is_correct(2, 'any')


import functools


def save_stats(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}  save  {result}')
        return result
    return wrapper