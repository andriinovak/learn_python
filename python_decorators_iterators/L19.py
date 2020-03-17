def add_five(x):
    return x + 5


def do_twice(some_funk):
    def resul_funk(x):
        return some_funk(some_funk(x))
    return resul_funk


result = do_twice(add_five)
print('result(5) =', result(5))


def yell(text):
    return text.upper() + '!'


print('yell =', yell)


bark = yell

print('bark("woof"), bark.__name__ =', bark('woof'), bark.__name__)


func_list = [yell, do_twice, add_five]

print('func_list[0] =', func_list[0])

yell_func_obj = func_list[0]


print('yell_func_obj.__name__, func_list[0]("functions are awesome") = ', yell_func_obj.__name__, func_list[0]('functions are awesome'))


def greet(func):
    greeting = func('Hi, I am a Python program')
    print('greeting =', greeting)


print('greet(yell) =', greet(yell))


def whisper(text):
    return text.capitalize()


print('greet(whisper) =', greet(whisper))


def say_titled(text):
    return text.title()


print('greet(say_titled) = ', greet(say_titled))


print('map(add_five, [2, 3, 4]) =', map(add_five, [2, 3, 4]))
print('list(map(add_five, [2, 3, 4])) =', list(map(add_five, [2, 3, 4])))


for i in map(add_five, [2, 3, 4]):
    print('i in map(add_five, [2, 3, 4]) =', i)

print('list(map(greet, [say_titled, yell])) =', list(map(greet, [say_titled, yell])))


def add_nums(a, b):
    return a + b


print('list(map(add_nums, (1, 2), (20, 30))) =', list(map(add_nums, (1, 2), (20, 30))))
print('list(map(lambda *a: sum(a), (1, 2), (20, 30, 40))) =', list(map(lambda *a: sum(a), (1, 2), (20, 30, 40))))
print('[1 == 0,] =', [1 == 0,])
print('filter(None, [1 == 0, "", 0, False, True, 5]) =', filter(None, [1 == 0, '', 0, False, True, 5]))
print('list(filter(None, [1 == 0, '', 0, False, True, 5])) =', list(filter(None, [1 == 0, '', 0, False, True, 5])))
print('list(filter(lambda a: bool(a) is False, [1 == 0, '', 0, False, True, 5])) =', list(filter(lambda a: bool(a) is False, [1 == 0, '', 0, False, True, 5])))
print('list(filter(lambda a: a > 0, [-1, 0, 3, 5])) =', list(filter(lambda a: a > 0, [-1, 0, 3, 5])))


def get_speek_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

print('get_speek_func(0) =', get_speek_func(0))
print('get_speek_func(0)("get there") =', get_speek_func(0)('get there'))
print('get_speek_func(0.9)("get there") =', get_speek_func(0.9)('get there'))


def get_speek_func(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

print('get_speek_func("scopes are awesome", 0.9)() =', get_speek_func('scopes are awesome', 0.9)())


class ShapeCreator():
    def draw_circle(radius):
        return f'this is circle with radius {radius}'

    def draw_cat(size):
        return f'The Cat weight {size} kg'


def some_fabric(shape_name, value):
    if shape_name == 'cirle':
        return ShapeCreator.draw_circle(value)
    elif shape_name == 'cat':
        return ShapeCreator.draw_cat(value)

print('some_fabric("cat", 5) =', some_fabric('cat', 5))


def some_fabric(creator, shape_name, value):
    if shape_name == 'cirle':
        return creator.draw_circle(value)
    elif shape_name == 'cat':
        return creator.draw_cat(value)

print('some_fabric(ShapeCreator, "cat", 5) =', some_fabric(ShapeCreator, 'cat', 5))


print('hasattr(ShapeCreator, "draw_cat") =', hasattr(ShapeCreator, 'draw_cat'))
print('getattr(ShapeCreator, "draw_cat") =', getattr(ShapeCreator, 'draw_cat'))

def draw_smth(creator, shape_name, size):
    if hasattr(creator, shape_name):
        return getattr(creator, shape_name)(size)
    else:
        return f'no {shape_name} in {creator}'


print('draw_smth(ShapeCreator, "draw_cat", 7) = ', draw_smth(ShapeCreator, 'draw_cat', 7))
print('draw_smth(ShapeCreator, "draw_dog", 7) = ', draw_smth(ShapeCreator, 'draw_dog', 7))
