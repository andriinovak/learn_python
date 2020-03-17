def code_lines(file_name):
    with open(file_name, 'r') as f:
        for line in f.readlines():
            if line.strip() == '' or line.startswith('#'):
                continue
            yield line


def count_program_lines(file_name):
    # return len(list(code_lines(file_name)))
    for line in code_lines(file_name):
        print(line, end='')


count_program_lines('iterators_generators.py')
