import os


def get_execution_path():
    return os.path.dirname(os.path.abspath(__file__))


def get_resource_path(filename):
    return get_execution_path() + "\\resources\\" + filename

def read_numbers_file(fileName):
    filePath = get_resource_path(fileName);
    file = open(filePath, mode='r')
    lines = file.readlines()
    file.close()
    return list(map(int, lines))

