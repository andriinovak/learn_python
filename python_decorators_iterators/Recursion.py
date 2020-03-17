def print_iter(number):
    for i in range(number, 0, -1):
        print(i)


def print_rec(number):
    if number <= 0:
        return

    print(number)
    print_rec(number - 1)


def factorial(number):
    if number < 0:
        raise NotImplementedError

    if number <= 1:
        return 1
    return factorial(number - 1) * number


RESULTS = {
    1: 0,
    2: 1
}


def fibonachi(index):
    if index in RESULTS:
        return RESULTS[index]

    value = fibonachi(index - 1) + fibonachi(index - 2)
    RESULTS[index] = value
    return value


folders = [[[[["okay.txt"], "ira.txt"], "bogdan.txt"]], ["volodya.txt"], [["kolya.txt"]], "panda.txt", "howto.txt"]


def folder_rec(data, level=1):
    for i in data:
        if type(i) == str:
            print(f'level: {level} - {i}')
        else:
            folder_rec(i, level + 1)


# folder_rec(folders)

# if __name__ == '__main__':
    # print_iter(10)
    # print_rec(5)
    # print(factorial(5))
    # print(fibonachi(10))



def simplify(dict):
    return {
        "foo.bar.value": 25,
        "foo.bar2.value": 36,
        "foo.serhii": 15,
        "foo2": 30,
        "ira": 20
    }


initial_data = {
    "foo": {
        "bar": {
            "value": 25
        },
        "bar2": {
            "value": 36
        },
        "serhii": 15,
    }, "foo2": 30,
    "ira": 20
}

print(initial_data)
result = {}


def full_path(data_dict, fullkey=''):
    for key, item in data_dict.items():
        key = fullkey + key + '.'

        if type(item) == dict:
            full_path(item, key)
        else:
            key = key[:-1]
            result[key] = item


def full_path_2(data):
    result = {}
    for key, value in data.items():
        if type(value) is dict:
            inner_result = full_path_2(value)
            for key_1, value_1 in inner_result.items():
                result[f'{key}.{key_1}'] = value_1

        else:
            result[key] = value

    return result


if __name__ == '__main__':
    print(full_path_2(initial_data))
