instructions = [[*line.split(), False]
                for line in open('input.txt', 'r').read().split('\n')]
print(instructions)


commands = {
    'acc': lambda acc, pos, val: [acc + int(val), pos + 1],
    'jmp': lambda acc, pos, val: [acc, pos + int(val)],
    'nop': lambda acc, pos, val: [acc, pos + 1]
}


def boot(instructions, position=0, accumulator=0):
    [command, value, visited] = instructions[position]

    if visited:
        return accumulator
    instructions[position][2] = True

    [accumulator, position] = commands[command](accumulator, position, value)
    return boot(instructions, position, accumulator)


print(boot(instructions))
