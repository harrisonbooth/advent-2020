passwords = open('input.txt', 'r').read().split('\n')
valid_passwords = []

for password in passwords:
    parts = password.split(' ')
    [pos1, pos2] = parts[0].split('-')
    letter = parts[1][0]
    password_string = parts[2]

    if (password_string[int(pos1) - 1] == letter) ^ (password_string[int(pos2) - 1] == letter):
        valid_passwords.append(password_string)

print(len(valid_passwords))


# def check_letters(letter, pos1, pos2, str):
#     return (str[pos1] == letter) ^ (str[pos2] == letter)


# passwords = [([int(limit) for limit in limits.split('-')], letter[0], password)
#              for (limits, letter, password)
#              in [line.split(' ') for line in passwords]]


# valid = [password
#          for ((pos1, pos2), letter, password) in passwords
#          if check_letters(letter, pos1 - 1, pos2 - 1, password)]

# print(len(valid))


