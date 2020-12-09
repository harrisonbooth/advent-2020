groups = [group.split('\n') for group in open('input.txt', 'r').read().split('\n\n')]

people_uniques = [[set(person) for person in group] for group in groups]
group_uniques = [set().union(*group) for group in groups]

counts = [len(group_uniques[i].intersection(*people_uniques[i])) for i in range(len(group_uniques))]
print(sum(counts))