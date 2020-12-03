import os


def get_execution_path():
    return os.path.dirname(os.path.abspath(__file__))


def get_resource_path(filename):
    return get_execution_path() + "\\resources\\" + filename


def read_lines_file(filename):
    file_path = get_resource_path(filename);
    file = open(file_path, mode='r')
    lines = file.readlines()
    for i, line in enumerate(lines):
        lines[i] = line.replace("\n", "")
    file.close()
    return lines


def read_numbers_file(filename):
    lines = read_lines_file(filename)
    return list(map(int, lines))

