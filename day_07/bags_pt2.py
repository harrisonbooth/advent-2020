import re

bag_re = 's*,+\s*'
bag_rules_pairs = [pair.split('s contain ') for pair in open(
    'input.txt', 'r').read().replace('s.', '').replace('.', '').split('\n')]

bag_rules_lists = [[outer, list(
    filter(lambda a: a != '', re.split(bag_re, inner)))] for [outer, inner] in bag_rules_pairs]

bag_rules_amounts = {outer: {bag_type: int(number) for [(number, bag_type)] in [
    re.findall('([1-9])\s{1}(.*)', bag) for bag in inner if "no other bag" not in bag]}
    for [outer, inner] in bag_rules_lists}

bag_rules_dicts = {outer: list(filter(lambda a: a != '', re.split(
    bag_re, inner))) for [outer, inner] in bag_rules_pairs}


def internal_bag_count(bags_to_check, dict, bags={}):
    new_bags = {}
    for [bag, amount] in bags_to_check.items():
        for [new_bag, new_amount] in dict[bag].items():
            new_bags[new_bag] = new_bags.get(
                new_bag, 0) + new_amount * amount

    for [new_bag, amount] in new_bags.items():
        bags[new_bag] = bags.get(new_bag, 0) + amount

    if len(bags_to_check) < 1:
        return bags
    return internal_bag_count(new_bags, dict, bags)


print(sum(internal_bag_count(
    {"shiny gold bag": 1}, bag_rules_amounts).values()))
