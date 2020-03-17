import random


def sort_arr_alex(array):
    sorted_arr = []
    while len(array) > 0:
        max_index = 0
        for index, value in enumerate(array):
            if array[max_index] < value:
                max_index = index
        max_value = array.pop(max_index)
        sorted_arr.append(max_value)

    return sorted_arr


arr = [1, 4, 3, 5, 2]
result = sort_arr_alex(arr)
# print(result)


min_range, max_range = 1, 10
array = [random.randint(min_range, max_range) for i in range(10)]


def optimized_sort(arr):
    container = {}

    for key in range(min_range, max_range + 1):
        container[key] = 0

    for value in arr:
        container[value] += 1

    result = []
    for key, value in container.items():
        for i in range(value):
            result.append(key)

    return result


# print(optimized_sort(array))

a = [1, 2, 3, 4]


class Stack:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def remove(self):
        self.data.pop()

    def __str__(self):
        return ','.join([str(i) for i in self.data])


s = Stack()
s.add(1)
s.add(2)
s.add(3)

print(s)
s.remove()
print(s)


expression = '()(())((()))(((())))'


class Queue:
    pass


class LinkedList:
    def __init__(self, root):
        self.root = root


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


a = Node(1)
b = Node(2, a)
c = Node(3, b)


def iterate_linked_list(node):
    while node:
        print(node.data)
        node = node.next


iterate_linked_list(c)
