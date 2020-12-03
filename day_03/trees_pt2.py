rows = open('input.txt', 'r').read().split('\n')

pos = (0, 0)


def count_trees(pos, step_sizes, rows, tree_count=0):
    x, y = pos
    dx, dy = step_sizes
    if (rows[y][x] == '#'):
        tree_count += 1
    if (y >= (len(rows) - 1)):
        return tree_count

    new_x = x + dx
    new_y = y + dy
    if new_x > (len(rows[0]) - 1):
        new_x = new_x - len(rows[0])

    return count_trees((new_x, new_y), step_sizes, rows, tree_count)


step_sizes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
results = [count_trees((0, 0), step_size, rows) for step_size in step_sizes]

product = 1
for result in results:
    product *= result

print(product)
