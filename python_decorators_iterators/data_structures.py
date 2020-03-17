def sum_numbers(data):
    result = 0
    for item in data:
        result += item

    return result


def add_numbers(number):
    a = 5
    b = 25
    result = a + b
    for i in range(number):
        result += i
    return result


def add_numbers_twice(numbers):
    result = 0
    for num in numbers:
        for num_2 in numbers:
            result += num + num_2

    return result


if __name__ == '__main__':
    print(sum_numbers([1, 2, 3, 4, 5, 6]))
    print(add_numbers(100500))
