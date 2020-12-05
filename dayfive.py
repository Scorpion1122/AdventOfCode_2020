import fileutility


def binary_space_solver(value, operations):
    min = 0
    max = value
    for operation in operations:
        if operation is 'L':
            max = max - (max - min) / 2
        elif operation is "R":
            min = min + (max - min) / 2

        if min is max:
            return min
    return int(min)


def get_boarding_id(row, column):
    return row * 8 + column


def solve_part_one(lines):
    #lines = ["FBFBBFFRLR"] # 44 - 5

    highest_boarding_id = 0
    for line in lines:
        if not line:
            continue

        row = binary_space_solver(128, line[0:7].replace('F', 'L').replace('B', 'R'))
        column = binary_space_solver(8, line[7:10])
        boarding_id = get_boarding_id(row, column)
        print (f"Solving: {line[0:7]} - {line[7:10]} = ({row}, {column}):{boarding_id}")

        if boarding_id > highest_boarding_id:
            highest_boarding_id = boarding_id

    print (f"Solution Part 1: {highest_boarding_id}")


def solve_part_two(lines):

    boarding_ids = []
    for line in lines:
        if not line:
            continue

        row = binary_space_solver(128, line[0:7].replace('F', 'L').replace('B', 'R'))
        column = binary_space_solver(8, line[7:10])
        new_boarding_id = get_boarding_id(row, column)
        boarding_ids.append(new_boarding_id)

    boarding_ids.sort()
    previous_id = 0
    for boarding_id in boarding_ids:
        if (boarding_id - previous_id) is 2 and previous_id is not 0:
            print(f"Found an empty spot {previous_id + 1}")
        previous_id = boarding_id


# 127 rows
# 8 columns
def solve():
    lines = fileutility.read_lines_file("input_day5.txt")
    solve_part_one(lines)
    solve_part_two(lines)
