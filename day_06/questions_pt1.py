groups = [group.split('\n') for group in open('input.txt', 'r').read().split('\n\n')]
uniques = [set().union(*group) for group in groups]
counts = [len(group_answers) for group_answers in uniques]
print(sum(counts))