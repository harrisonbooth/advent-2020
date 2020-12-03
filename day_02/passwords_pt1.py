passwords = open('input.txt', 'r').read().split('\n')


def check_letters(letter, min, max, str):
    return min <= str.count(letter) <= max


passwords = [([int(limit) for limit in limits.split('-')], letter[0], password)
             for (limits, letter, password)
             in [line.split(' ') for line in passwords]]

valid = [password
         for ((min, max), letter, password) in passwords
         if check_letters(letter, min, max, password)]

print(len(valid))
