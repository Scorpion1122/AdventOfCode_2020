import fileutility


def is_valid_number(numbers, preamble, offset):
    number = numbers[offset]

    index_range = range(preamble)
    for index in index_range:
        number_one = numbers[offset - (index + 1)]

        for index2 in index_range[index:preamble]:
            number_two = numbers[offset - (index2 + 1)]

            if number_one + number_two == number and number_one != number_two:
                return True
    return False


def find_encryption_weakness(numbers, invalid_index):
    invalid_number = numbers[invalid_index]

    numbers_range = range(len(numbers))
    for index in numbers_range:
        if index == invalid_index:
            continue;

        total = numbers[index]
        smallest = numbers[index]
        largest = numbers[index]
        for index2 in numbers_range[index + 1:len(numbers)]:
            if index2 == invalid_index:
                break;

            number = numbers[index2]
            total += number

            if total > invalid_number:
                break;

            if number < smallest:
                smallest = number
            elif number > largest:
                largest = number

            if total == invalid_number:
                return smallest + largest
    return -1


def solve():
    numbers = fileutility.read_numbers_file("input_day9.txt")
    numbers_size = len(numbers)
    preamble = 25

    index_range = range(numbers_size)[preamble:numbers_size]
    for index in index_range:
        if not is_valid_number(numbers, preamble, index):
            print(f"Part 1: {numbers[index]}: Is the first invalid number!")
            print(f"Part 2: {find_encryption_weakness(numbers, index)}")




