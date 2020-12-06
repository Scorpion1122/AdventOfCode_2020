import fileutility


def solve_part_one(lines):
    total_yes_answers = 0
    current_set = set()
    for line in lines:
        if not line:
            total_yes_answers += len(current_set)
            current_set.clear()
            continue

        for character in line:
            if character not in current_set:
                current_set.add(character)

    if len(current_set) is not 0:
        total_yes_answers += len(current_set)
        current_set.clear()

    print (f"Solution to Part 1: {total_yes_answers}")


def count_shared_answers(answers, group_size):
    result = 0
    for key in answers:
        if answers[key] is group_size:
            result += 1
    return result


def solve_part_two(lines):
    total_yes_answers = 0

    current_dict = dict()
    current_group_size = 0
    for line in lines:
        if not line:
            total_yes_answers += count_shared_answers(current_dict, current_group_size)
            current_dict.clear()
            current_group_size = 0
            continue

        current_group_size += 1
        for character in line:
            if character not in current_dict:
                current_dict[character] = 1
            else:
                current_dict[character] += 1

    if len(current_dict) is not 0:
        total_yes_answers += count_shared_answers(current_dict, current_group_size)

    print (f"Solution to Part 2: {total_yes_answers}")


def solve():
    lines = fileutility.read_lines_file("input_day6.txt")

    solve_part_one(lines)
    solve_part_two(lines)

