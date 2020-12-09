def get_row(boarding_pass):
    row_binary = boarding_pass[:7].replace("F", "0").replace("B", "1")
    return int(int(row_binary, base=2))


def get_column(boarding_pass):
    column_binary = boarding_pass[7:].replace("L", "0").replace("R", "1")
    return int(int(column_binary, base=2))


def get_id(boarding_pass):
    row = get_row(boarding_pass)
    column = get_column(boarding_pass)
    return (8 * row) + column


passes = open('input.txt', 'r').read().split('\n')
ids = sorted([get_id(boarding_pass) for boarding_pass in passes])

for i in range(len(ids) - 1):
    if ids[i + 1] - ids[i] > 1:
        print(ids[i] + 1)
