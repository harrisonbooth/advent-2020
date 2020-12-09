import re

bag_re = 's*,*\s*[1-9]\s'
bag_rules_pairs = [pair.split('s contain ') for pair in open('input.txt', 'r').read().replace('s.', '').replace('.', '').split('\n')]
bag_rules_dicts = {outer: list(filter(lambda a: a != '', re.split(bag_re, inner))) for [outer, inner] in bag_rules_pairs}


def outer_bag_count(bags, dict, containers=[]):
    new_containers = [key for (key, value) in dict.items() for bag in bags if bag in value]
    if (len(new_containers) < 1):
        return set(containers)
    containers.extend(new_containers)
    return outer_bag_count(new_containers, dict, containers)


print(len(outer_bag_count(["shiny gold bag"], bag_rules_dicts)))
