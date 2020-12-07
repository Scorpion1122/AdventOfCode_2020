import fileutility
from bag import Bag


def get_or_add_bag(bags, bag_id):
    if bag_id not in bags:
        bags[bag_id] = Bag(bag_id)
    return bags[bag_id]


def add_child_bag(parent, child_id, count):
    if child_id in parent.contains:
        parent.contains[child_id] += count
    else:
        parent.contains[child_id] = count


def parse_bag_rules(bags, rule):
    end_of_first = rule.index("bags contain")
    main_bag_id = rule[0:end_of_first].strip()
    main_bag = get_or_add_bag(bags, main_bag_id)

    sub_rules = rule[end_of_first + len("bags contain"):len(rule)].split(',')
    for sub_rule in sub_rules:
        sub_rule = sub_rule.strip()
        if "no other bags" in sub_rule:
            continue

        try:
            count = int(sub_rule[0])
            bag_id = sub_rule[1:len(sub_rule)].replace('.', '').replace('bags', '').replace('bag', '').strip()
            add_child_bag(main_bag, bag_id, count)
        except:
            print(f"Rule could not be parsed: {sub_rule}")


def does_bag_contain_bag(bags, bag_id, count_id):
    if bag_id not in bags:
        return False

    bag = bags[bag_id]
    for child_id in bag.contains:
        if child_id == count_id:
            return True
        elif does_bag_contain_bag(bags, child_id, count_id):
            return True
    return False


def count_bags_with(bags, count_id):
    result = 0
    for bag_id in bags:
        if does_bag_contain_bag(bags, bag_id, count_id):
            result += 1
    return result


def count_total_bags_in(bags, bag_id):
    if bag_id not in bags:
        return 0

    result = 0
    bag = bags[bag_id]
    for child_id in bag.contains:
        count = bag.contains[child_id]
        child_count = count_total_bags_in(bags, child_id)

        result = result + count + child_count * count
    return result


def solve():
    lines = fileutility.read_lines_file("input_day7.txt")

    bags = dict()
    for line in lines:
        parse_bag_rules(bags, line)

    bags_with_gold = count_bags_with(bags, "shiny gold")
    print(f"Part One, bags that contain gold: {bags_with_gold}")

    bags_in_gold = count_total_bags_in(bags, "shiny gold")
    print(f"Part Two, Shiny Gold bag contains {bags_in_gold} bags")

