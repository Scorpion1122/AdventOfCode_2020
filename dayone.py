import fileutility


def find_entries_that_sum_to(target_number, numbers, count, current_entries, current_total=0, offset=0):
    for i in range(offset, len(numbers)):
        number = numbers[i]
        new_total = number + current_total
        at_last_element = len(current_entries) == count - 1

        if new_total == target_number and at_last_element:
            current_entries.append(number)
            return

        if new_total < target_number and not at_last_element:
            current_entries.append(number)
            find_entries_that_sum_to(target_number, numbers, count, current_entries, new_total, i + 1)

            if len(current_entries) >= count:
                return
            else:
                del current_entries[len(current_entries) - 1]


def solve():
    numbers = fileutility.read_numbers_file("input_day1.txt")

    result_part_one = []
    find_entries_that_sum_to(2020, numbers, 2, result_part_one)
    if len(result_part_one) == 2:
        print(f"First Result: {result_part_one[0]} + {result_part_one[1]} = {2020}, Result = {result_part_one[0] * result_part_one[1]}")

    result_part_two = []
    find_entries_that_sum_to(2020, numbers, 3, result_part_two)
    if len(result_part_two) == 3:
        print(
            f"First Result: {result_part_two[0]} + {result_part_two[1]} + {result_part_two[2]} = {2020}, Result = {result_part_two[0] * result_part_two[1] * result_part_two[2]}")
