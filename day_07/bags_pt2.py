import re

bag_re = 's*,+\s*'
bag_rules_pairs = [pair.split('s contain ') for pair in open(
    'input.txt', 'r').read().replace('s.', '').replace('.', '').split('\n')]
# bag_rules_dicts = {outer: {'a': re.split('[1-9]\s{1}', inner_bag) for inner_bag in list(
#     filter(lambda a: a != '', re.split(bag_re, inner)))} for [outer, inner] in bag_rules_pairs}

bag_rules_lists = [[outer, list(
    filter(lambda a: a != '', re.split(bag_re, inner)))] for [outer, inner] in bag_rules_pairs]


# print(bag_rules_lists)
# bag_rules_dicts = {outer: {'bag_type': '1' for inner_bag in re.split(
#     '([1-9]\s){1}', inner_bag)} for [outer, inner] in bag_rules_lists}

# [['bright purple bag', ['4 shiny chartreuse bag', '5 plaid lime bag', '2 dim magenta bag']]]

bag_rules_dicts = [{outer: {bag_type: number for [(number, bag_type)] in [re.findall('([1-9])\s{1}(.*)', bag) for bag in inner if "no other bag" not in bag]}}
                   for [outer, inner] in bag_rules_lists]

print(bag_rules_dicts)

# def outer_bag_count(bags, dict, containers=[]):
#     new_containers = [key for (key, value) in dict.items() for bag in bags if bag in value]
#     if (len(new_containers) < 1):
#         return set(containers)
#     containers.extend(new_containers)
#     return outer_bag_count(new_containers, dict, containers)


# print(len(outer_bag_count(["shiny gold bag"], bag_rules_dicts)))
