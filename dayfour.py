import fileutility


def validate_number(value, min, max):
    try:
        int_value = int(value)
        return int_value <= max and int_value >= min
    except ValueError:
        return False


def validate_birth_year(value):
    return validate_number(value, 1920, 2002)


def validate_issue_year(value):
    return validate_number(value, 2010, 2020)


def validate_experation_year(value):
    return validate_number(value, 2020, 2030)


def validate_height(value):
    if "cm" in value:
        return validate_number(value.replace("cm", ""), 150, 193)
    elif "in" in value:
        return validate_number(value.replace("in", ""), 59, 76)
    else:
        return False


def validate_hair_color(value):
    return value and value[0] is "#" and len(value) is 7


def validate_eye_color(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_passport_id(value):
    return len(value) == 9


def is_valid_passport(passport, required_fields, field_validators=None):
    for required_field in required_fields:
        if required_field not in passport:
            return False

    if not field_validators:
        return True

    for key, value in passport.items():
        if key in field_validators and not field_validators[key](value):
            # print(f"Invalid: {key} - {value}: {field_validators[key]} = {field_validators[key](value)}")
            return False

    return True


def count_valid_passports(lines, required_fields, field_validators=None):
    current_passport = dict()
    valid_passports = 0
    for line in lines:
        if not line:  # end of passport, validate it
            if is_valid_passport(current_passport, required_fields, field_validators):
                valid_passports += 1
            current_passport.clear()
        else:
            fields = line.split(' ')
            for pair in fields:
                value_key_split = pair.split(':')
                current_passport[value_key_split[0]] = value_key_split[1]

    if len(current_passport) is not 0:
        if is_valid_passport(current_passport, required_fields, field_validators):
            valid_passports += 1
        current_passport.clear()

    return valid_passports


def solve():
    lines = fileutility.read_lines_file("input_day4.txt")

    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];
    field_validator = {
        "byr": validate_birth_year,
        "iyr": validate_issue_year,
        "eyr": validate_experation_year,
        "hgt": validate_height,
        "hcl": validate_hair_color,
        "ecl": validate_eye_color,
        "pid": validate_passport_id,
    }

    print(f"Part 1: {count_valid_passports(lines, required_fields)} Valid passports found!")
    print(f"Part 2: {count_valid_passports(lines, required_fields, field_validator)} Valid passports found!")
