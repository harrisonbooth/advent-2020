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


# print(bag_rules_amounts)
def outer_bag_count(bags, dict, containers=[]):
    new_containers = [key for (key, value) in dict.items()
                      for bag in bags if bag in value]
    if (len(new_containers) < 1):
        return set(containers)
    containers.extend(new_containers)
    return outer_bag_count(new_containers, dict, containers)


def internal_bag_count(bags, dict, internal_bags=[]):
    new_bags = [bag_type
                for bag in bags for [bag_type, amount] in dict[bag].items() for i in range(amount)]
    if len(new_bags) < 1:
        return internal_bags
    internal_bags.extend(new_bags)
    return internal_bag_count(new_bags, dict, internal_bags)


print(len(internal_bag_count(["shiny gold bag"], bag_rules_amounts)))
