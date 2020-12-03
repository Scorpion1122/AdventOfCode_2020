import fileutility


def solve_part_one(lines):
    valid_password = 0
    for line in lines:
        split = line.split(' ')
        password = split[2]

        policy_character = split[1].replace(':', '')
        policy_range_split = split[0].split('-')
        policy_min = int(policy_range_split[0])
        policy_max = int(policy_range_split[1])

        character_count = password.count(policy_character)
        if character_count >= policy_min and character_count <= policy_max:
            valid_password += 1

    print(f"Part One: {valid_password} Valid Passwords Detected!")


def solve_part_two(lines):
    valid_password = 0
    for line in lines:
        split = line.split(' ')
        password = split[2]
        password_length = len(password)

        policy_character = split[1].replace(':', '')
        policy_range_split = split[0].split('-')
        policy_position_one = int(policy_range_split[0]) - 1
        policy_position_two = int(policy_range_split[1]) - 1

        character_on_position_1 = False
        if policy_position_one < password_length and password[policy_position_one] == policy_character:
            character_on_position_1 = True

        character_on_position_2 = False
        if policy_position_two < password_length and password[policy_position_two] == policy_character:
            character_on_position_2 = True

        if character_on_position_1 and not character_on_position_2 or character_on_position_2 and not character_on_position_1:
            valid_password += 1

    print(f"Part Two: {valid_password} Valid Passwords Detected!")


def solve():
    lines = fileutility.read_lines_file("input_day2.txt")
    solve_part_one(lines)
    solve_part_two(lines)
