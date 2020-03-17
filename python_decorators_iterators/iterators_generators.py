# x = iter([1, 2, 3])
# print(next(x))
# print(next(x))
# print(next(x))

# for i in list_of_numbers:
#     print(i)

list_of_numbers = [1, 2, 3, 4, 5, 6]


class ReversedList:
    def __init__(self, data):
        self.data = data
        self.x = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        self.x = self.x - 1
        if self.x < 0:
            raise StopIteration
        return self.data[self.x]


reversed_list = ReversedList(list_of_numbers)
# for i in reversed_list:
#     print(i)


def reversed_list(data):
    x = len(data)
    while x > 0:
        x = x - 1
        yield data[x]
        yield data[x] * data[x]


gen_list = reversed_list(list_of_numbers)
# for i in gen_list:
#     print(i)

pages = [['ira', 'bohdan'], ['andrii', 'sasha'], ['roman', 'vasyl']]


def all_names(pages):
    for page in pages:
        for profile in page:
            yield profile


# for i in all_names(pages):
#     print(i)

list_numbers = [1, 2, 3, 4, 5]


def enumerate_1(data):
    index = 0
    for item in data:
        index = index - 1
        yield index, item * item


# for i in enumerate_1(list_of_numbers):
#     print(i)
list_iter = enumerate_1(list_numbers)


def generator(start, stop):
    while start <= stop:
        yield start * start
        start += 1


list_gen = generator(1, 5)
for i in generator(1, 5):
    print(i)
