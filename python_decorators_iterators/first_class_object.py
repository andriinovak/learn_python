import math


def add_five(x):
    return x + 5


def do_twice(some_funk):
    def resul_funk(x):
        return some_funk(some_funk(x))
    return resul_funk


# result = do_twice(add_five)
# print(result(5))


def make_cylinder_volume_funk(r):
    def volume(h):
        return math.pi * r**2 * h
    return volume


# volume_of_r10 = make_cylinder_volume_funk(10)
# print(volume_of_r10(30))


def first_plus_first_second_minus_second(a, b):
    def next_funk(x, y):
        return a + x, b - y
    return next_funk


# function_numbers_1_2 = first_plus_first_second_minus_second(1, 2)
# print(function_numbers_1_2(3, 4))

def yell(text):
    return text.upper() + "!"


print(yell('hello'))

func_list = [yell, do_twice, add_five]


def add_nums(a, b):
    return a + b


print(list(map(add_nums, {1, 2}, [3, 4])))
print(list(map(lambda *a: sum(a), (1, 2), (3, 4))))


print(list(filter(lambda a: bool(a) is False, [1 == 0, '', 0, False, True, 1])))


def speak_func(volume):
    def whisper(text):
        return text.lower() + "..."
    def yell(text):
        return text.upper() + "!"
    if volume > 0:
        return yell
    else:
        return whisper


print(speak_func(-2)('hello'))


def speak_func(text, volume):
    def whisper():
        return text.lower() + "..."
    def yell():
        return text.upper() + "!"
    if volume > 0.5:
        return yell
    else:
        return whisper


print(speak_func('Hello', 2)())


def make_adder(n):
    def add(x):
        return n + x
    return add


plus_3 = make_adder(3)
print(plus_3(4))
