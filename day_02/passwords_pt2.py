passwords = open('input.txt', 'r').read().split('\n')


def check_letters(letter, pos1, pos2, str):
    return ((str[pos1] == letter or str[pos2] == letter)
            and not (str[pos1] == letter and str[pos2] == letter))


passwords = [([int(limit) for limit in limits.split('-')], letter[0], password)
             for (limits, letter, password)
             in [line.split(' ') for line in passwords]]

valid = [password
         for ((pos1, pos2), letter, password) in passwords
         if check_letters(letter, pos1 - 1, pos2 - 1, password)]

print(len(valid))
